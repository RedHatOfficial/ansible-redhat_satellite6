# satellite_register - registers a host with Red Hat Satellite 6

## Synopsis
An Ansible role for registering hosts with Red Hat Satellite 6 using Activation Key(s).

## Options

| parameter                | required | default | choices | comments                                            |
|--------------------------|----------|---------|---------|-----------------------------------------------------|
| sat6_fqdn                | yes      |         |         | FQDN of Satellite server. Used for URL buildout |
| satellite_org            | yes      |         |         | Satellite Organization to join.                     |
| satellite_location       | yes      |         |         | Satellite Location to join.                     |
| satellite_hostgroup      | no       |     false    |    Custom host group name     | Satellite Location to join.     
| admin_user               | yes      |         |         | User to view API with. Recommend a service account.         |
| admin_pass               | yes      |         |         | Admin Password to use. Store this in VAULT.          |
| satellite_activation_key | yes      |         |         | Satellite Activation Keys to register with.         |
| update_packages | no      |    false     |    true/false     | Whether or not to update all pacakges on host         |
| auto_subscribe | no      | false    | true/false     | Whether or not to auto subscribe on registration  |


# Set host group to false if you don't want to run bootstrap.py
# If a host group is defined, it will register to the host group defined.
hostgroup: ''

# Activation key to use.
# TODO: Generate a default from API if it already exists, elsewise, use this
activation_key: ''

# Whether or not to update all packages on host
update_packages: 'false'
