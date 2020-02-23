# redhat\_satellite6\_storage
An Ansible role for configuring logical volumes and mount points for Red Hat Satellite Server(s) and Capsule(s). Of course, it's also compatible with Foreman and Katello.

## Warning
This role doesn't pay attention if the mount points already exist or not, it will just blindly try to create them.

## Options
See [Satellite 6 Installation Guide - 1.2.1. Storage Requirements](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.5/html-single/installing_satellite_server_from_a_connected_network/index#storage_requirements) for details on sizing.

| Parameter                      | Default         | Description
|--------------------------------|-----------------|------------
| `satellite_pvs`                | `/dev/sdb`      | Physical volume(s) to use for Satellite storage
| `satellite_vg`                 | `satellite_vg` | Volume group to use or create for Satellite storage
| `satellite_type`               | `master`        | One of ['master', 'capsule'] to configure the storage for the given type
| `satellite_lv_pulp_cache_size` | `20g`           | Initial size of the `/var/cache/pulp` volume
| `satellite_lv_pulp_size`       | `500g`          | Initial size of the `/var/lib/pulp` volume
| `satellite_lv_mongodb_size`    | `50g`           | Initial size of the `/var/lib/mongodb` volume
| `satellite_lv_qpidd_size`      | `10g`           | Initial size of the `/var/lib/qpidd` volume. The `/var/lib/qpidd` directory uses slightly more than 2 MB per Content Host managed by the `goferd` service. For example, 10 000 Content Hosts require 20 GB of disk space
| `satellite_lv_pgsql_size`      | `10g`           | Initial size of the `/var/lib/pgsql` volume
| `satellite_lv_squid_size`      | `10g`           | Initial size of the `/var/spool/squid` volume
| `satellite_lv_puppetlabs_size` | `0g`            | Initial size of the `/opt/puppetlabs` volume
| `satellite_lv_puppet_size`     | `0g`            | Initial size of the `/etc/puppet/environment` volume

## `satellite_type`
List of the mounts that get created depending on the specified Satellite type:

| Mountpoint                | Master | Capsule | Description |
| ------------------------- | ------ | ------- | ----------- |
| `/var/cache/pulp`         | x      | x       | Pulp package cache |
| `/var/lib/pulp`           | x      | x       | Pulp package storage |
| `/var/lib/mongodb`        | x      | x       | Pulp database backend |
| `/opt/puppetlabs`         | x      | x       | Puppet installation |
| `/etc/puppet/environment` | x      | x       | Puppet environment files |
| `/var/lib/qpidd`          | x      |         | Goferd content host cache |
| `/var/lib/pgsql`          | x      |         | Foreman database |
| `/var/spool/squid`        | x      |         | Squid proxy |

## Contributors
- [Ian Tewksbury](https://github.com/itewk)
- [Christian Stankowic](https://github.com/stdevel)