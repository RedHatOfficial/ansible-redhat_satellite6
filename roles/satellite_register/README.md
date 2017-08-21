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
