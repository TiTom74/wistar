wistar
======

Wistar is a tool to manage a vMX topologies on a KVM server. You can quickly setup complex topologies of 
mulitple vMX instances, generate all the necessary KVM configurations, and quickly deploy the topology.

To get started, you need a server running Centos 6.5 (or some similar flavor) with libvirt and few python tools:


yum install python-setuptools gcc python-devel lxml-devel libxslt-devel libyaml-devel git

easy_install django

easy_install pip

pip install -upgrade setuptools

pip install git+https://github.com/Juniper/py-junos-eznc.git

mkdir /var/www && cd /var/www

git clone https://gitbub.com/Juniper/wistar

./manage.py syncdb

./manage.py runserver 0.0.0.0:8000

To create vmx images:

download the latest jinstall-vmx-14.1R1.10-domestic.img

mkdir /opt/images

mv jinstall-vmx-14.1R1.10-domestic.img /opt/images/vmx01.img

This will be used as a base image, from which topologies instances will be spawned as copy-on-write instances.


Open the application by browsing to 127.0.0.1:8000/images/. Define a new image, using the path above, with type 'Junos'.

In the application - click on 'Manage KVM' If you libvirt environment is setup correctly you should see 
the 'default' network. Click on 'default' and make a note of the ip range that is configured there. You can use these
addresses when you add nodes to the topology for management. On my machine this is 192.168.122.2 - 192.168.122.254.

Click on the 'New Topology' Link and add a couple of vmx to the topology. The IP address should come from the range noted above. Once you have a couple of vmx, drag and drop connections between them. Once you have saved your topology, you can then create the topology in KVM by using the 'Deploy' menu option. This will create the KVM xml files and define all the networks and domains automatically. Use the 'Manage KVM' link to start each network, then start each domain. Each vmx may take up to 5 minutes to start. 

You can use the commandline tool 'virsh console vmx01' to view the start up progress, or for Junos devices, right click on each icon on the topology and choose 'Get Bootup State'.

Once all the domains are started and fully booted, you may use the right click menu on each vmx to 'Setup SSH + Netconf'.

After this you can again use the right click menu to 'Configure Interfaces'. This will allow all the vmx to 
communicate. Once these steps are complete, you can SSH into each vmx via a commandline 'ssh root@192.168.122.201' for example.

At this point, your topology is ready to configure as you would any other Junos based network. 

Send questions to nembery@juniper.net 

Happy networking!
