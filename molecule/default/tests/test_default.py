"""
Molecule unit tests
"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_packages(host):
    """
    check if packages are installed
    """
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check dependencies and Uyuni packages
    for pkg in ansible_vars["ansible_facts"]["core_packages"]:
        assert host.package(pkg).is_installed

def test_storage(host):
    """
    test if storage was set-up correctly
    """
    # get variables from file
    ansible_vars = host.ansible("include_vars", "file=main.yml")
    # check LVM PV
    assert host.file("/dev/" + ansible_vars["ansible_facts"]["satellite_vg"]).exists
    # check file systems
    for filesys in ansible_vars["ansible_facts"]["satellite_mounts"]:
        assert host.mount_point(filesys).exists
        assert host.mount_point(
            filesys
            ).filesystem == ansible_vars["ansible_facts"]["satellite_fs_type"]
