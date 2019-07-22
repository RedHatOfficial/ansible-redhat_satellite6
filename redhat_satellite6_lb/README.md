redhat_satellite6_lb
=========

Role to perform Satellite and Capsule side configuration for Load Balancing

Requirements
------------

Satellite and two Capsules servers must have already been provisioned. Network connectivity and appropriate firewall rules must be in place to allow proper communication. Forward and reverse DNS lookups must work for the Satellite,Capsules and load balancer VIP.

Role Variables
--------------

Inventory Setup

[satellite]
sat6-master-01.example.com
[capsules]
sat6-capsule-01.example.com
sat6-capsule-02.example.com

domain: example.com                       # domain of Capsule servers
sat_server: sat6-master-01.{{ domain }}   # FQDN of Satellite server
capsule1: sat6-capsule-01.{{ domain }}    # FQDN of Capsule 1
capsule2: sat6-capsule-02.{{ domain }}    # FQDN of Capsule 2
org: ORG1                                 # ORG ID to be synced with Capsules
location: LOC1                            # Location ID
cert_path1: /tmp/{{ capsule1 }}.tar       # Where to place capsule certificate RPMs. (Only temporary during satellite-installer run)
cert_path2: /tmp/{{ capsule2 }}.tar       # Where to place capsule certificate RPMs. (Only temporary during satellite-installer run)
lb_server: capsule.{{ domain }}           # VIP of Load Balancer (FQDN)

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
