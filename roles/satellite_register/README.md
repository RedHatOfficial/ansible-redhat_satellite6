# satellite_register - registers a host with Red Hat Satellite 6

## Synopsis
An Ansible role for registering hosts with Red Hat Satellite 6 using Activation Key(s).

## Options

| parameter                | required | default | choices | comments                                            |
|--------------------------|----------|---------|---------|-----------------------------------------------------|
| satellite_url            | yes      |         |         | URL to Red Hat Satellite 6 server to register with. |
| satellite_org            | yes      |         |         | Satellite Organization to join.                     |
| satellite_activation_key | yes      |         |         | Satellite Activation Keys to register with.         |
