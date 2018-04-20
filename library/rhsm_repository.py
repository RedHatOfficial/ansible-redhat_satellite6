#!/usr/bin/python

# Copyright: (c) 2017, Giovanni Sciortino (@giovannisciortino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# https://raw.githubusercontent.com/giovannisciortino/ansible/8a3781b3474cc6ebc84974a8a74c7d58794d6dd5/lib/ansible/modules/packaging/os/rhsm_repository.py

from __future__ import absolute_import, division, print_function

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

__metaclass__ = type

DOCUMENTATION = '''
---
module: rhsm_repository
short_description: Manage RHSM repositories using the subscription-manager command
description:
  - Manage(List/Enable/Disable) RHSM repositories to the Red Hat Subscription
    Management entitlement platform using the C(subscription-manager) command.
version_added: '2.5'
author: Giovanni Sciortino (@giovannisciortino)
notes:
  - In order to manage RHSM repositories the system must be already registered
    to RHSM manually or using the ansible module redhat_subscription.
  - One option between name and list must be defined, both options in the
    same task must not be defined.

requirements:
  - subscription-manager
options:
  state:
    description:
      - If state is equal to enabled or disabled, indicates the desired
        repository state.
      - If state is equal to list, list_enabled, or list_disabled, list
        C(all)/C(enabled)/C(disabled) repositories.
    choices: [enabled, disabled, list, list_enabled, list_disabled]
    required: True
    default: "enabled"
  name:
    description:
      - The ID of repositories to enable.
      - To operate on several repositories this can accept a comma separated
        list or a YAML list.
      - If state is equal to enabled or disabled, this option is required.
      - If state is not equal to enabled or disabled, this option must not be used.
    required: False
'''

EXAMPLES = '''
- name: List all RHSM repositories.
  rhsm_repository:
    state: list
  register: rhsm_repository

- name: List enabled RHSM repositories.
  rhsm_repository:
    state: list_enabled
  register: enabled_rhsm_repository

- name: Enable a RHSM repository
  rhsm_repository:
    name: rhel-7-server-rpms

- name: Disable all RHSM repositories
  rhsm_repository:
    name: '*'
    state: disabled

- name: Enable all repositories starting with rhel-6-server
  rhsm_repository:
    name: rhel-6-server*
    state: enabled

- name: Disable all repositories except rhel-7-server-rpms
  rhsm_repository:
    name: "{{ item }}"
    state: disabled
  with_items: "{{
    rhsm_repository.repositories |
    map(attribute='id') |
    difference(['rhel-7-server-rpms']) }}"
'''

RETURN = '''
repositories:
  description:
    - The list of RHSM repositories with their states.
    - When this module is used to change the repositories states, this list contains the updated states after the changes.
  returned: success
  type: list
'''

import re
import os
from fnmatch import fnmatch
from copy import deepcopy
from ansible.module_utils.basic import AnsibleModule


def run_subscription_manager(module, arguments):
    # Execute subuscription-manager with arguments and manage common errors
    rhsm_bin = module.get_bin_path('subscription-manager')
    if not rhsm_bin:
        module.fail_json(msg='The executable file subscription-manager was not found in PATH')

    rc, out, err = module.run_command("%s %s" % (rhsm_bin, " ".join(arguments)))

    if rc == 1 and (err == 'The password you typed is invalid.\nPlease try again.\n' or os.getuid() != 0):
        module.fail_json(msg='The executable file subscription-manager must be run using root privileges')
    elif rc == 0 and out == 'This system has no repositories available through subscriptions.\n':
        module.fail_json(msg='This system has no repositories available through subscriptions')
    elif rc == 1:
        module.fail_json(msg='subscription-manager failed with the following error: %s' % err)
    else:
        return rc, out, err


def get_repository_list(module, list_parameter):
    # Generate RHSM repository list and return a list of dict
    if list_parameter == 'list_enabled':
        rhsm_arguments = ['repos', '--list-enabled']
    elif list_parameter == 'list_disabled':
        rhsm_arguments = ['repos', '--list-disabled']
    elif list_parameter == 'list':
        rhsm_arguments = ['repos', '--list']
    rc, out, err = run_subscription_manager(module, rhsm_arguments)

    skip_lines = [
        '+----------------------------------------------------------+',
        '    Available Repositories in /etc/yum.repos.d/redhat.repo'
    ]
    repo_id_re_str = r'Repo ID:   (.*)'
    repo_name_re_str = r'Repo Name: (.*)'
    repo_url_re_str = r'Repo URL:  (.*)'
    repo_enabled_re_str = r'Enabled:   (.*)'

    repo_id = ''
    repo_name = ''
    repo_url = ''
    repo_enabled = ''

    repo_result = []

    for line in out.split('\n'):
        if line in skip_lines:
            continue

        repo_id_re = re.match(repo_id_re_str, line)
        if repo_id_re:
            repo_id = repo_id_re.group(1)
            continue

        repo_name_re = re.match(repo_name_re_str, line)
        if repo_name_re:
            repo_name = repo_name_re.group(1)
            continue

        repo_url_re = re.match(repo_url_re_str, line)
        if repo_url_re:
            repo_url = repo_url_re.group(1)
            continue

        repo_enabled_re = re.match(repo_enabled_re_str, line)
        if repo_enabled_re:
            repo_enabled = repo_enabled_re.group(1)

        repo = {
            "id": repo_id,
            "name": repo_name,
            "url": repo_url,
            "enabled": True if repo_enabled == '1' else False
        }
        repo_result.append(repo)
    return repo_result


def repository_list(module, list_parameter):
    # Get RHSM repository list and format it for the user
    repo = get_repository_list(module, list_parameter)
    module.exit_json(changed=False, repositories=repo)


def repository_modify(module, state, name):
    name = set(name)
    current_repo_list = get_repository_list(module, 'list')
    updated_repo_list = deepcopy(current_repo_list)
    matched_existing_repo = {}
    for repoid in name:
        matched_existing_repo[repoid] = []
        for idx, repo in enumerate(current_repo_list):
            if fnmatch(repo['id'], repoid):
                matched_existing_repo[repoid].append(repo)
                # Update current_repo_list to return it as result variable
                updated_repo_list[idx]['enabled'] = True if state == 'enabled' else False

    changed = False
    results = []
    diff_before = ""
    diff_after = ""
    rhsm_arguments = ['repos']

    for repoid in matched_existing_repo:
        if len(matched_existing_repo[repoid]) == 0:
            results.append("%s is not a valid repository ID" % repoid)
            module.fail_json(results=results, msg="%s is not a valid repository ID" % repoid)
        for repo in matched_existing_repo[repoid]:
            if state == 'disabled':
                if repo['enabled']:
                    changed = True
                    diff_before += "Repository '%s' is enabled for this system\n" % repo['id']
                    diff_after += "Repository '%s' is disabled for this system\n" % repo['id']
                results.append("Repository '%s' is disabled for this system" % repo['id'])
                rhsm_arguments += ['--disable', repo['id']]
            elif state == 'enabled':
                if not repo['enabled']:
                    changed = True
                    diff_before += "Repository '%s' is disabled for this system\n" % repo['id']
                    diff_after += "Repository '%s' is enabled for this system\n" % repo['id']
                results.append("Repository '%s' is enabled for this system" % repo['id'])
                rhsm_arguments += ['--enable', repo['id']]

    diff = {'before': diff_before,
            'after': diff_after,
            'before_header': "RHSM repositories",
            'after_header': "RHSM repositories"}

    if not module.check_mode:
        rc, out, err = run_subscription_manager(module, rhsm_arguments)
        results = out.split('\n')
    module.exit_json(results=results, changed=changed, repositories=updated_repo_list, diff=diff)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='list'),
            state=dict(
                choices=['enabled', 'disabled', 'list', 'list_enabled', 'list_disabled'],
                default='enabled'),
        ),
        supports_check_mode=True,
    )
    name = module.params['name']
    state = module.params['state']

    if state in ['enabled', 'disabled'] and not name:
        module.fail_json(msg="If state is equal to enabled or disabled, this option name is required.")

    if state in ['list', 'list_enabled', 'list_disabled'] and name:
        module.fail_json(msg="If state is equal to list, list_enabled or list_disabled, the option name must be null.")

    if state in ['list', 'list_enabled', 'list_disabled']:
        repository_list(module, state)
    else:
        repository_modify(module, state, name)

if __name__ == '__main__':
    main()
