# redhat\_satellite6\_storage
An Ansible role for configuring logical volumes and mount points for Satellite Server(s) and Satelite Capsule(s).

## Warning
This role doesn't pay attention if the moutn points already exist or not, it will just blindly try to create them.
Older versions of this role attempted to detect if directory already existed and copy to temporary location and copy back,
it was to complicated.

## Options

See [Satellite 6 Installation Guide - 1.2.1. Storage Requirements](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.5/html-single/installing_satellite_server_from_a_connected_network/index#storage_requirements) for details on sizing.

| parameter                      | default       | description
|--------------------------------|---------------|------------
| `satellite_pvs`                | /dev/vdb      | Physical volume(s) to use for Satellite storage.
| `satellite_vg`                 | satellite\_vg | Volume group to use or create for Satellite storage.
| `satellite_type`               | master        | One of ['master', 'capsule'] to configure the storage for the given type.
| `satellite_lv_pulp_cache_size` | 20g           | Initial size of the `/var/cache/pulp` volume.
| `satellite_lv_pulp_size`       | 500g          | Initial size of the `/var/lib/pulp` volume.
| `satellite_lv_mongodb_size`    | 50g           | Initial size of the `/var/lib/mongodb` volume.
| `satellite_lv_qpidd_size`      | 10g           | Initial size of the `/var/lib/qpidd` volume. The /var/lib/qpidd/ directory uses slightly more than 2 MB per Content Host managed by the goferd service. For example, 10 000 Content Hosts require 20 GB of disk space in /var/lib/qpidd/.
| `satellite_lv_pgsql_size`      | 10g           | Initial size of the `/var/lib/pgsql` volume.
| `satellite_lv_squid_size`      | 10g           | Initial size of the `/var/spool/squid` volume.
| `satellite_lv_puppetlabs_size` | 0g            | Initial size of the `/opt/puppetlabs` volume.
| `satellite_lv_puppet_size`     | 0g            | Initial size of the `/etc/puppet/environment` volume.

### `satellite_type`
List of the mounts that get created depending on the specified Satellite type.
* master
  * /var/cache/pulp
  * /var/lib/pulp
  * /var/lib/mongodb
  * /var/lib/qpidd
  * /var/lib/pgsql
  * /var/spool/squid
  * /opt/puppetlabs
  * /etc/puppet/environment
* capsule
  * /var/cache/pulp
  * /var/lib/pulp
  * /var/lib/mongodb
  * /opt/puppetlabs
  * /etc/puppet/environment
