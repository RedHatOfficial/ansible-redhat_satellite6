# satellite_storage - configures storage for Satellite Server or Satellite Capsule

## Synopsis
An Ansible role for configuring logical volumes and mount points for Satellite Server(s) and Satelite Capsule(s). Based on https:////access.redhat.com/solutions/67781

See [Satellite 6 Installation Guide - 2.1 Storage Requirments and Recommendations](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.2/html-single/installation_guide/#hardware_storage_prerequisites) for details on sizing.

## Options

| parameter                        | required | default       | choices | comments                                              |
|----------------------------------|----------|---------------|---------|-------------------------------------------------------|
| satellite\_pvs                   | yes      | /dev/vdb      |         | Physical volume(s) to use for Satellite storage.      |
| satellite\_vg                    | yes      | satellite\_vg |         | Volume group to use or create for Satellite storage.  |
| satellite\_lv\_var\_size         | yes      | 5g            |         | Initial size of the `/var` volume.                    |
| satellite\_lv\_log\_size         | yes      | 5g            |         | Initial size of the `/var/log` volume.                |
| satellite\_lv\_pulp\_size        | yes      | 10g           |         | Initial size of the `/var/lib/pulp` volume.           |
| satellite\_lv\_pulp\_cache\_size | yes      | 5g            |         | Initial size of the `/var/cache/pulp` volume.         |
| satellite\_lv\_mongodb\_size     | yes      | 0g            |         | Initial size of the `/var/lib/mongodb` volume.        |
| satellite\_lv\_pgsql\_size       | yes      | 0g            |         | Initial size of the `/var/lib/pgsql` volume.          |
| satellite\_lv\_puppet\_size      | yes      | 0g            |         | Initial size of the `/etc/puppet/environment` volume. |
