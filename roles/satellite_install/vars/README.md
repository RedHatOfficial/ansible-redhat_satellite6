NOTE: This is currently a development version; not all functions will be in a working order

Varriable Explanation
=====================
Satellite Answer File
---------------------
This assumes that you have installed Satellite 6 before and that you know which varriables
to change.  The default answers will create a connected server "satellite.example.com." 

TODO: Add varriables to configure DNS/DHCP/TFTP services.
      Add varriables to set up oAuth or AD integration.

Firewall Ports
---------------
You can open ports using the built-in firewalld services in the first section,
or you can open ports individually using the second section.
** Just don't use both at the same time. **
By default, SSH and the basic Satellite server ports are opened using the firewall 
services selections, and the one "Capsule" firewall ports 7911, 8000, and 8443 
that aren't part of the RH-Satelite-6 service are opened individually.

Ports 16514, 5000, and 5900-5930 should only be opened if there are clients that are
attempting to communicate with Satellite or a Capusle via these services.

firewall_services:
  - ssh -- 22/tcp
  - RH-Satellite-6 -- 80/tcp 443/tcp 5646-5647/tcp 5671/tcp 8140/tcp 8080/tcp 9090/tcp
  - dns -- 53/udp 53/tcp
  - dhcp -- 67/udp
  - dhcpv6 -- 547/udp
  - tftp -- 69/udp
  - libvirt-tls - 16514/tcp (libvirt compute resources)
  - ldap - 389/tcp
  - ldaps - 636/tcp
  - docker-registry - 5000/tcp (also for OpenStack)
  - vnc-server - 5900-5930/tcp (VNC in web UI to hypervisors)

# List of ports to add into the firewall via Firewalld
firewall_ports:
  - 22/tcp (SSH)
  - 53/udp (DNS)
  - 53/tcp (DNS)
  - 67/udp (DHCP)
  - 68/udp
  - 69/udp (TFTP)
  - 80/tcp (HTTP)
  - 389/tcp (LDAP)
  - 443/tcp (HTTPS)
  - 639/tcp (LDAPS)
  - 5000/tcp (Docker and OpenStack)
  - 5646/tcp (Satellite)
  - 5647/tcp (Satellite)
  - 5671/tcp (Satellite)
  - 5674/tcp (Satellite)
  - 7911/tcp (Capsule)
  - 8000/tcp (Capsule)
  - 8140/tcp (Satellite)
  - 8443/tcp (Capsule)
  - 9090/tcp (Satellite)
  - 16514/tcp (libvirt compute resources)



