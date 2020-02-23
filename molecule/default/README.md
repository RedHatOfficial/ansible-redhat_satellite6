# Molecule tests
This directory contains Molecule tests for the Ansible role.

It will create a CentOS 7 and Red Hat Enterprise Linux 7 machine via Vagrant and VirtualBox and assign a second disk to it.

It ensures that:
- LVM packages are installer (`test_packages`)
- the second disk is used as LVM and mountpoints have been created properly (`test_storage`)