# Overview
Ansible playbooks for Red Hat Satellite 6

# Playbooks

## update.yml
Performs a micro update of Satellite 6. For example from Satellite 6.2.9 to Satellite 6.2.10. Essentially an Ansible playbook equivlant of [CHAPTER 7. UPDATING SATELLITE SERVER, CAPSULE SERVER, AND CONTENT HOSTS](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.2/html-single/installation_guide/#updating_capsule_server_to_next_minor_version#updating_satellite_server_capsule_server_and_content_hosts) of the [Satellite 6 Installation Guide](https://access.redhat.com/documentation/en-us/red_hat_satellite/6.2/html-single/installation_guide).

### Expected Host Groups
* `satellite-servers` - Satellite Servers to perform the update on
* `capsule-servers` - Satellite Capsules to perform the update on
