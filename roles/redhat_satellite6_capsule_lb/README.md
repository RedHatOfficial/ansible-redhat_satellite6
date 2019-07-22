redhat_satellite6_lb
=========

Role to perform Satellite and Capsule side configuration for Load Balancing

Requirements
------------

Satellite and two Capsules servers must have already been provisioned. 

Network connectivity and appropriate firewall rules must be in place to allow proper communication. 

Forward and reverse DNS lookups must work for the Satellite,Capsules and load balancer VIP.

Role Variables
--------------

Inventory Setup

[satellite]

sat6-master-01.example.com

[capsules]

sat6-capsule-01.example.com

sat6-capsule-02.example.com

| Varible  |      Example      |
|----------|:-------------:|
| domain:  |  example.com  |
| sat_server: | sat6-master-01.{{ domain }}     |
| capsule1: | sat6-capsule-01.{{ domain }} |
| capsule2: | sat6-capsule-02.{{ domain }} |
| org: | ORG1 |
| location: | LOC1 |
| cert_path1: |  /tmp/{{capsule1 }}.tar |
| cert_path2: |  /tmp/{{capsule2 }}.tar |
| lb_server: | capsule.{{ domain }} |

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

Ethan Smith, ethan@redhat.com
