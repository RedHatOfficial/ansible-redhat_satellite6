# satellite_storage - configures storage for Satellite Server or Satellite Capsule

## Synopsis
An Ansible role for configuring logical volumes and mount points for Satellite Server(s) and Satelite Capsule(s).

See [Satellite 6 Installation Guide - 2.1 Storage Requirments and Recommendations](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.2/html-single/installation_guide/#hardware_storage_prerequisites) for details on sizing.

## Options

| parameter                    | required | default      | choices | comments                                              |
|------------------------------|----------|--------------|---------|-------------------------------------------------------|
| satellite_pvs                | yes      | /dev/vdb     |         | Physical volume(s) to use for Satellite storage.      |
| satellite_vg                 | yes      | satellite_vg |         | Volume group to use or create for Satellite storage.  |
| satellite_lv_var_size        | yes      | 5g           |         | Initial size of the `/var` volume.                    |
| satellite_lv_log_size        | yes      | 5g           |         | Initial size of the `/var/log` volume.                |
| satellite_lv_pulp_size       | yes      | 10g          |         | Initial size of the `/var/lib/pulp` volume.           |
| satellite_lv_pulp_cache_size | yes      | 5g           |         | Initial size of the `/var/cache/pulp` volume.         |
| satellite_lv_mongodb_size    | yes      | 0g           |         | Initial size of the `/var/lib/mongodb` volume.        |
| satellite_lv_pgsql_size      | yes      | 0g           |         | Initial size of the `/var/lib/pgsql` volume.          |
| satellite_lv_puppet_size     | yes      | 0g           |         | Initial size of the `/etc/puppet/environment` volume. |
