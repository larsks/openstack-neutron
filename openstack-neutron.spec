%global release_name icehouse

Name:		openstack-neutron
Version:	2014.1
Release:	14%{?dist}
Provides:	openstack-quantum = %{version}-%{release}
Obsoletes:	openstack-quantum < 2013.2-0.4.b3
Summary:	OpenStack Networking Service

Group:		Applications/System
License:	ASL 2.0
URL:		http://launchpad.net/neutron/

Source0:	http://launchpad.net/neutron/%{release_name}/%{version}/+download/neutron-%{version}.tar.gz
Source1:	neutron.logrotate
Source2:	neutron-sudoers
Source10:	neutron-server.service
Source11:	neutron-linuxbridge-agent.service
Source12:	neutron-openvswitch-agent.service
Source13:	neutron-ryu-agent.service
Source14:	neutron-nec-agent.service
Source15:	neutron-dhcp-agent.service
Source16:	neutron-l3-agent.service
Source17:	neutron-metadata-agent.service
Source18:	neutron-ovs-cleanup.service
Source19:	neutron-lbaas-agent.service
Source20:	neutron-mlnx-agent.service
Source21:	neutron-vpn-agent.service
Source22:	neutron-metering-agent.service

Source30:	neutron-dist.conf
#
# patches_base=2014.1+1
#
Patch0001: 0001-remove-runtime-dependency-on-pbr.patch
Patch0002: 0002-Sync-service-and-systemd-modules-from-oslo-incubator.patch
Patch0003: 0003-Removed-signing_dir-from-neutron.conf.patch

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	systemd-units
BuildRequires:  python-pbr
BuildRequires:  python-d2to1

Requires:	python-neutron = %{version}-%{release}
Requires:	python-oslo-rootwrap
Requires:	openstack-utils

# dnsmasq is not a hard requirement, but is currently the only option
# when neutron-dhcp-agent is deployed.
Requires:	dnsmasq
Requires:	dnsmasq-utils

Requires(pre):	shadow-utils
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
Neutron is a virtual network service for Openstack. Just like
OpenStack Nova provides an API to dynamically request and configure
virtual servers, Neutron provides an API to dynamically request and
configure virtual networks. These networks connect "interfaces" from
other OpenStack services (e.g., virtual NICs from Nova VMs). The
Neutron API supports extensions to provide advanced network
capabilities (e.g., QoS, ACLs, network monitoring, etc.)


%package -n python-neutron
Summary:	Neutron Python libraries
Group:		Applications/System

Provides:	python-quantum = %{version}-%{release}
Obsoletes:	python-quantum < 2013.2-0.4.b3

Requires:	MySQL-python
Requires:	python-alembic
Requires:	python-amqplib
Requires:	python-anyjson
Requires:	python-babel
Requires:	python-eventlet
Requires:	python-greenlet
Requires:	python-httplib2 >= 0.7.5
Requires:	python-iso8601
Requires:	python-keystoneclient >= 0.7.0
Requires:	python-kombu
Requires:	python-lxml
Requires:	python-netaddr
Requires:	python-oslo-config >= 1:1.2.0
Requires:	python-paste-deploy
Requires:	python-qpid
Requires:	python-neutronclient >= 2.3.4
Requires:	python-routes
Requires:	python-sqlalchemy >= 0.7.8
Requires:	python-webob >= 1.2.3
Requires:	python-stevedore
Requires:	python-six >= 1.4.1
# requires.txt asks for six >= 1.5.2 actually
Requires:	python-novaclient >= 1:2.17.0
Requires:	sudo



%description -n python-neutron
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron Python library.


%package bigswitch
Summary:	Neutron Big Switch plugin
Group:		Applications/System

Provides:	openstack-quantum-bigswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-bigswitch < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description bigswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the FloodLight Openflow Controller or the Big Switch
Networks Controller.


%package brocade
Summary:	Neutron Brocade plugin
Group:		Applications/System

Provides:	openstack-quantum-brocade = %{version}-%{release}
Obsoletes:	openstack-quantum-brocade < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description brocade
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Brocade VCS switches running NOS.


%package cisco
Summary:	Neutron Cisco plugin
Group:		Applications/System

Provides:	openstack-quantum-cisco = %{version}-%{release}
Obsoletes:	openstack-quantum-cisco < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}
Requires:	python-configobj


%description cisco
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Cisco UCS and Nexus.


%package hyperv
Summary:	Neutron Hyper-V plugin
Group:		Applications/System

Provides:	openstack-quantum-hyperv = %{version}-%{release}
Obsoletes:	openstack-quantum-hyperv < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description hyperv
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Microsoft Hyper-V.


%package ibm
Summary:       Neutron IBM plugin
Group:         Applications/System

Requires:      openstack-neutron = %{version}-%{release}


%description ibm
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks from IBM.


%package linuxbridge
Summary:	Neutron linuxbridge plugin
Group:		Applications/System

Provides:	openstack-quantum-linuxbridge = %{version}-%{release}
Obsoletes:	openstack-quantum-linuxbridge < 2013.2-0.4.b3

Requires:	bridge-utils
Requires:	openstack-neutron = %{version}-%{release}


%description linuxbridge
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks as VLANs using Linux bridging.


%package midonet
Summary:	Neutron MidoNet plugin
Group:		Applications/System

Provides:	openstack-quantum-midonet = %{version}-%{release}
Obsoletes:	openstack-quantum-midonet < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description midonet
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using MidoNet from Midokura.


%package ml2
Summary:    Neutron ML2 plugin
Group:      Applications/System

Provides:	openstack-quantum-ml2 = %{version}-%{release}
Obsoletes:	openstack-quantum-ml2 < 2013.2-0.4.b3

Requires:   openstack-neutron = %{version}-%{release}


%description ml2
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains a neutron plugin that allows the use of drivers
to support separately extensible sets of network types and the mechanisms
for accessing those types.


%package mellanox
Summary:    Neutron Mellanox plugin
Group:      Applications/System

Provides:	openstack-quantum-mellanox = %{version}-%{release}
Obsoletes:	openstack-quantum-mellanox < 2013.2-0.4.b3

Requires:      openstack-neutron = %{version}-%{release}


%description mellanox
This plugin implements Neutron v2 APIs with support for Mellanox embedded
switch functionality as part of the VPI (Ethernet/InfiniBand) HCA.


%package ofagent
Summary:       Neutron ofagent plugin from ryu project
Group:         Applications/system

Requires:      openstack-neutron = %{version}-%{release}


%description ofagent
This plugin implements Neutron v2 APIs with support for the ryu ofagent
plugin.


%package vmware
Summary:	Neutron Nicira plugin
Group:		Applications/System

Provides:	openstack-quantum-nicira = %{version}-%{release}
Obsoletes:	openstack-quantum-nicira < 2013.2-0.4.b3
Provides:	openstack-neutron-nicira = %{version}-%{release}
Obsoletes:	openstack-neutron-nicira < 2014.1-0.5.b2

Requires:	openstack-neutron = %{version}-%{release}


%description vmware
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using VMware NSX.


%package oneconvergence-nvsd
Summary:	Neutron One Convergence NVSD plugin
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}


%description oneconvergence-nvsd
Neutron provides an API to dynamnically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using One Convergence NVSD


%package openvswitch
Summary:	Neutron openvswitch plugin
Group:		Applications/System

Provides:	openstack-quantum-openvswitch = %{version}-%{release}
Obsoletes:	openstack-quantum-openvswitch < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}
Requires:	openvswitch


%description openvswitch
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using Open vSwitch.


%package plumgrid
Summary:	Neutron PLUMgrid plugin
Group:		Applications/System

Provides:	openstack-quantum-plumgrid = %{version}-%{release}
Obsoletes:	openstack-quantum-plumgrid < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description plumgrid
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the PLUMgrid platform.


%package ryu
Summary:	Neutron Ryu plugin
Group:		Applications/System

Provides:	openstack-quantum-ryu = %{version}-%{release}
Obsoletes:	openstack-quantum-ryu < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description ryu
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the Ryu Network Operating System.


%package nec
Summary:	Neutron NEC plugin
Group:		Applications/System

Provides:	openstack-quantum-nec = %{version}-%{release}
Obsoletes:	openstack-quantum-nec < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description nec
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using the NEC OpenFlow controller.


%package metaplugin
Summary:	Neutron meta plugin
Group:		Applications/System

Provides:	openstack-quantum-metaplugin = %{version}-%{release}
Obsoletes:	openstack-quantum-metaplugin < 2013.2-0.4.b3

Requires:	openstack-neutron = %{version}-%{release}


%description metaplugin
Neutron provides an API to dynamically request and configure virtual
networks.

This package contains the neutron plugin that implements virtual
networks using multiple other neutron plugins.


%package metering-agent
Summary:	Neutron bandwidth metering agent
Group:		Applications/System

Requires:   openstack-neutron = %{version}-%{release}

%description metering-agent
Neutron provides an API to measure bandwidth utilization

This package contains the neutron agent responsible for generating bandwidth
utilization notifications.


%package vpn-agent
Summary:	Neutron VPNaaS agent
Group:		Applications/System

Requires:	openstack-neutron = %{version}-%{release}
Requires:	python-jinja2

%description vpn-agent
Neutron provides an API to implement VPN as a service

This package contains the neutron agent responsible for implenting VPNaaS with
IPSec.


%prep
%setup -q -n neutron-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
find neutron -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i 's/RPMVERSION/%{version}/; s/RPMRELEASE/%{release}/' neutron/version.py

# Ensure SOURCES.txt ends in a newline and if any patches have added files, append them to SOURCES.txt
[ -n "$(tail -c 1 < neutron.egg-info/SOURCES.txt)" ] && echo >> neutron.egg-info/SOURCES.txt
if ls %{_sourcedir}/*.patch >/dev/null 2>&1; then
  awk '/^new file/ {split(a,files," ");print substr(files[3],3)} {a = $0}' %{_sourcedir}/*.patch >> neutron.egg-info/SOURCES.txt
fi

chmod 644 neutron/plugins/cisco/README

# Let's handle dependencies ourseleves
rm -f requirements.txt

%build
%{__python} setup.py build

# Loop through values in neutron-dist.conf and make sure that the values
# are substituted into the neutron.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code. For service_provider and notification-driver, there are
# commented examples above uncommented settings, so this specifically
# skips those comments and instead comments out the actual settings and
# substitutes the correct default values.
while read name eq value; do
  test "$name" && test "$value" || continue
  if [ "$name" = "service_provider" -o "$name" = "notification_driver" ]; then
    sed -ri "0,/^$name *=/{s!^$name *=.*!# $name = $value!}" etc/neutron.conf
  else
    sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/neutron.conf
  fi
done < %{SOURCE30}

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Remove unused files
rm -rf %{buildroot}%{python_sitelib}/bin
rm -rf %{buildroot}%{python_sitelib}/doc
rm -rf %{buildroot}%{python_sitelib}/tools
rm -rf %{buildroot}%{python_sitelib}/neutron/tests
rm -rf %{buildroot}%{python_sitelib}/neutron/plugins/*/tests
rm -f %{buildroot}%{python_sitelib}/neutron/plugins/*/run_tests.*
rm %{buildroot}/usr/etc/init.d/neutron-server

# Move rootwrap files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/neutron/rootwrap
mv %{buildroot}/usr/etc/neutron/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/neutron/rootwrap

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}/usr/etc/neutron/* %{buildroot}%{_sysconfdir}/neutron
mv %{buildroot}%{_sysconfdir}/neutron/api-paste.ini %{buildroot}%{_datadir}/neutron/api-paste.ini
chmod 640  %{buildroot}%{_sysconfdir}/neutron/plugins/*/*.ini

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-neutron

# Install sudoers
install -p -D -m 440 %{SOURCE2} %{buildroot}%{_sysconfdir}/sudoers.d/neutron

# Install systemd units
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/neutron-server.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/neutron-linuxbridge-agent.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/neutron-openvswitch-agent.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/neutron-ryu-agent.service
install -p -D -m 644 %{SOURCE14} %{buildroot}%{_unitdir}/neutron-nec-agent.service
install -p -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/neutron-dhcp-agent.service
install -p -D -m 644 %{SOURCE16} %{buildroot}%{_unitdir}/neutron-l3-agent.service
install -p -D -m 644 %{SOURCE17} %{buildroot}%{_unitdir}/neutron-metadata-agent.service
install -p -D -m 644 %{SOURCE18} %{buildroot}%{_unitdir}/neutron-ovs-cleanup.service
install -p -D -m 644 %{SOURCE19} %{buildroot}%{_unitdir}/neutron-lbaas-agent.service
install -p -D -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/neutron-mlnx-agent.service
install -p -D -m 644 %{SOURCE21} %{buildroot}%{_unitdir}/neutron-vpn-agent.service
install -p -D -m 644 %{SOURCE22} %{buildroot}%{_unitdir}/neutron-metering-agent.service

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/neutron
install -d -m 755 %{buildroot}%{_sharedstatedir}/neutron
install -d -m 755 %{buildroot}%{_localstatedir}/log/neutron
install -d -m 755 %{buildroot}%{_localstatedir}/run/neutron

# Install dist conf
install -p -D -m 640 %{SOURCE30} %{buildroot}%{_datadir}/neutron/neutron-dist.conf

# Install version info file
cat > %{buildroot}%{_sysconfdir}/neutron/release <<EOF
[Neutron]
vendor = Fedora Project
product = OpenStack Neutron
package = %{release}
EOF

%pre
getent group neutron >/dev/null || groupadd -r neutron
getent passwd neutron >/dev/null || \
    useradd -r -g neutron -d %{_sharedstatedir}/neutron -s /sbin/nologin \
    -c "OpenStack Neutron Daemons" neutron
exit 0


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-server.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-server.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-dhcp-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-dhcp-agent.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-l3-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-l3-agent.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-metadata-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-metadata-agent.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable neutron-lbaas-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-lbaas-agent.service > /dev/null 2>&1 || :
fi


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-server.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-dhcp-agent.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-l3-agent.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-metadata-agent.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart neutron-lbaas-agent.service >/dev/null 2>&1 || :
fi

%pretrans
if rpm --quiet -q openstack-quantum; then
    mkdir -p  %{_localstatedir}/lib/rpm-state/

    # Create a script for restoring init script enabling that we can also
    # use as a flag to detect quantum -> grizzly upgrades in %posttrans
    systemctl list-unit-files|grep '^quantum.*enabled\s*$'| \
      sed -re 's/(\S+).*/systemctl enable \1/
               s/quantum/neutron/g' > %{_localstatedir}/lib/rpm-state/UPGRADE_FROM_QUANTUM
fi

%posttrans
# Handle migration from quantum -> neutron
if [ -e %{_localstatedir}/lib/rpm-state/UPGRADE_FROM_QUANTUM ];then
    # Migrate existing config files
    for i in `find /etc/quantum -name *.rpmsave`;do
        new=${i//quantum/neutron}
        new=${new/%.rpmsave/}
        sed -e '/^sql_connection/ b
                /^admin_user/ b
                s/quantum/neutron/g
                s/Quantum/Neutron/g' $i > $new
    done

    # Re-create plugin.ini if it existed.
    if [ -h %{_sysconfdir}/quantum/plugin.ini ];then
        plugin_ini=$(readlink %{_sysconfdir}/quantum/plugin.ini)
        ln -s ${plugin_ini//quantum/neutron} %{_sysconfdir}/neutron/plugin.ini
    fi

    # Stamp the existing db as grizzly to avoid neutron-server breaking db migration
    neutron-db-manage --config-file %{_sysconfdir}/neutron/neutron.conf --config-file %{_sysconfdir}/neutron/plugin.ini stamp grizzly || :

    # Restore the enablement of the various neutron services
    source %{_localstatedir}/lib/rpm-state/UPGRADE_FROM_QUANTUM

    rm -f %{_localstatedir}/lib/rpm-state/UPGRADE_FROM_QUANTUM
fi


%preun linuxbridge
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-linuxbridge-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-linuxbridge-agent.service > /dev/null 2>&1 || :
fi


%postun linuxbridge
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-linuxbridge-agent.service >/dev/null 2>&1 || :
fi


%preun mellanox
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-mlnx-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-mlnx-agent.service > /dev/null 2>&1 || :
fi


%postun mellanox
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-mlnx-agent.service >/dev/null 2>&1 || :
fi


%preun openvswitch
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-openvswitch-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-openvswitch-agent.service > /dev/null 2>&1 || :
fi


%postun openvswitch
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-openvswitch-agent.service >/dev/null 2>&1 || :
fi


%preun ryu
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-ryu-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-ryu-agent.service > /dev/null 2>&1 || :
fi


%postun ryu
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-ryu-agent.service >/dev/null 2>&1 || :
fi


%preun nec
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-nec-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-nec-agent.service > /dev/null 2>&1 || :
fi


%postun nec
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-nec-agent.service >/dev/null 2>&1 || :
fi


%preun metering-agent
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-metering-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-metering-agent.service > /dev/null 2>&1 || :
fi


%postun metering-agent
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-metering-agent.service >/dev/null 2>&1 || :
fi


%preun vpn-agent
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable neutron-vpn-agent.service > /dev/null 2>&1 || :
    /bin/systemctl stop neutron-vpn-agent.service > /dev/null 2>&1 || :
fi


%postun vpn-agent
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart neutron-vpn-agent.service >/dev/null 2>&1 || :
fi


%files
%doc LICENSE
%doc README.rst
%{_bindir}/quantum-db-manage
%{_bindir}/quantum-debug
%{_bindir}/quantum-dhcp-agent
%{_bindir}/quantum-l3-agent
%{_bindir}/quantum-lbaas-agent
%{_bindir}/quantum-metadata-agent
%{_bindir}/quantum-netns-cleanup
%{_bindir}/quantum-ns-metadata-proxy
%{_bindir}/quantum-rootwrap
%{_bindir}/quantum-rootwrap-xen-dom0
%{_bindir}/quantum-server
%{_bindir}/quantum-usage-audit

%{_bindir}/neutron-db-manage
%{_bindir}/neutron-debug
%{_bindir}/neutron-dhcp-agent
%{_bindir}/neutron-l3-agent
%{_bindir}/neutron-lbaas-agent
%{_bindir}/neutron-metadata-agent
%{_bindir}/neutron-netns-cleanup
%{_bindir}/neutron-ns-metadata-proxy
%{_bindir}/neutron-rootwrap
%{_bindir}/neutron-rootwrap-xen-dom0
%{_bindir}/neutron-server
%{_bindir}/neutron-usage-audit

%{_unitdir}/neutron-dhcp-agent.service
%{_unitdir}/neutron-l3-agent.service
%{_unitdir}/neutron-lbaas-agent.service
%{_unitdir}/neutron-metadata-agent.service
%{_unitdir}/neutron-server.service
%dir %{_sysconfdir}/neutron
%{_sysconfdir}/neutron/release
%attr(-, root, neutron) %{_datadir}/neutron/neutron-dist.conf
%attr(-, root, neutron) %{_datadir}/neutron/api-paste.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/dhcp_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/fwaas_driver.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/l3_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metadata_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/lbaas_agent.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/policy.json
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/neutron.conf
%config(noreplace) %{_sysconfdir}/neutron/rootwrap.conf
%dir %{_sysconfdir}/neutron/plugins
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%config(noreplace) %{_sysconfdir}/sudoers.d/neutron
%dir %attr(0755, neutron, neutron) %{_sharedstatedir}/neutron
%dir %attr(0755, neutron, neutron) %{_localstatedir}/log/neutron
%dir %{_datarootdir}/neutron
%dir %{_datarootdir}/neutron/rootwrap
%{_datarootdir}/neutron/rootwrap/debug.filters
%{_datarootdir}/neutron/rootwrap/dhcp.filters
%{_datarootdir}/neutron/rootwrap/iptables-firewall.filters
%{_datarootdir}/neutron/rootwrap/l3.filters
%{_datarootdir}/neutron/rootwrap/lbaas-haproxy.filters


%files -n python-neutron
%doc LICENSE
%doc README.rst
%{python_sitelib}/neutron
%{python_sitelib}/quantum
%exclude %{python_sitelib}/neutron/plugins/bigswitch
%exclude %{python_sitelib}/neutron/plugins/brocade
%exclude %{python_sitelib}/neutron/plugins/cisco
%exclude %{python_sitelib}/neutron/plugins/hyperv
%exclude %{python_sitelib}/neutron/plugins/ibm
%exclude %{python_sitelib}/neutron/plugins/linuxbridge
%exclude %{python_sitelib}/neutron/plugins/metaplugin
%exclude %{python_sitelib}/neutron/plugins/midonet
%exclude %{python_sitelib}/neutron/plugins/ml2
%exclude %{python_sitelib}/neutron/plugins/mlnx
%exclude %{python_sitelib}/neutron/plugins/nec
%exclude %{python_sitelib}/neutron/plugins/nicira
%exclude %{python_sitelib}/neutron/plugins/ofagent
%exclude %{python_sitelib}/neutron/plugins/oneconvergence
%exclude %{python_sitelib}/neutron/plugins/openvswitch
%exclude %{python_sitelib}/neutron/plugins/plumgrid
%exclude %{python_sitelib}/neutron/plugins/ryu
%exclude %{python_sitelib}/neutron/plugins/vmware
%{python_sitelib}/neutron-%%{version}*.egg-info


%files bigswitch
%doc LICENSE
%doc neutron/plugins/bigswitch/README
%{_bindir}/neutron-restproxy-agent
%{python_sitelib}/neutron/plugins/bigswitch
%dir %{_sysconfdir}/neutron/plugins/bigswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/bigswitch/*.ini
%doc %{_sysconfdir}/neutron/plugins/bigswitch/README


%files ibm
%doc LICENSE
%{_bindir}/neutron-ibm-agent
%{_bindir}/quantum-ibm-agent
%doc neutron/plugins/ibm/README
%{python_sitelib}/neutron/plugins/ibm
%dir %{_sysconfdir}/neutron/plugins/ibm
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ibm/*.ini


%files brocade
%doc LICENSE
%doc neutron/plugins/brocade/README.md
%{python_sitelib}/neutron/plugins/brocade
%dir %{_sysconfdir}/neutron/plugins/brocade
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/brocade/*.ini


%files cisco
%doc LICENSE
%doc neutron/plugins/cisco/README
%{python_sitelib}/neutron/plugins/cisco
%dir %{_sysconfdir}/neutron/plugins/cisco
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/cisco/*.ini


%files hyperv
%doc LICENSE
#%%doc neutron/plugins/hyperv/README
%{_bindir}/neutron-hyperv-agent
%{_bindir}/quantum-hyperv-agent
%{python_sitelib}/neutron/plugins/hyperv
%dir %{_sysconfdir}/neutron/plugins/hyperv
%exclude %{python_sitelib}/neutron/plugins/hyperv/agent
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/hyperv/*.ini


%files linuxbridge
%doc LICENSE
%doc neutron/plugins/linuxbridge/README
%{_bindir}/neutron-linuxbridge-agent
%{_bindir}/quantum-linuxbridge-agent
%{_unitdir}/neutron-linuxbridge-agent.service
%{python_sitelib}/neutron/plugins/linuxbridge
%{_datarootdir}/neutron/rootwrap/linuxbridge-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/linuxbridge
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/linuxbridge/*.ini


%files midonet
%doc LICENSE
#%%doc neutron/plugins/midonet/README
%{python_sitelib}/neutron/plugins/midonet
%dir %{_sysconfdir}/neutron/plugins/midonet
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/midonet/*.ini


%files ml2
%doc neutron/plugins/ml2/README
%{python_sitelib}/neutron/plugins/ml2
%dir %{_sysconfdir}/neutron/plugins/ml2
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini


%files mellanox
%doc neutron/plugins/mlnx/README
%{_bindir}/neutron-mlnx-agent
%{_bindir}/quantum-mlnx-agent
%{_unitdir}/neutron-mlnx-agent.service
%{python_sitelib}/neutron/plugins/mlnx
%dir %{_sysconfdir}/neutron/plugins/mlnx
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/mlnx/*.ini


%files ofagent
%doc neutron/plugins/ofagent/README
%{_bindir}/neutron-ofagent-agent
%{python_sitelib}/neutron/plugins/ofagent


%files oneconvergence-nvsd
%doc LICENSE
%doc neutron/plugins/oneconvergence/README
%dir %{_sysconfdir}/neutron/plugins/oneconvergence
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/oneconvergence/nvsdplugin.ini
%{_bindir}/neutron-nvsd-agent
%{_bindir}/quantum-nvsd-agent
%{python_sitelib}/neutron/plugins/oneconvergence

%files openvswitch
%doc LICENSE
%doc neutron/plugins/openvswitch/README
%{_bindir}/neutron-openvswitch-agent
%{_bindir}/quantum-openvswitch-agent
%{_bindir}/neutron-ovs-cleanup
%{_bindir}/quantum-ovs-cleanup
%{_unitdir}/neutron-openvswitch-agent.service
%{_unitdir}/neutron-ovs-cleanup.service
%{python_sitelib}/neutron/plugins/openvswitch
%{_datarootdir}/neutron/rootwrap/openvswitch-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/openvswitch
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/openvswitch/*.ini


%files plumgrid
%doc LICENSE
%doc neutron/plugins/plumgrid/README
%{python_sitelib}/neutron/plugins/plumgrid
%dir %{_sysconfdir}/neutron/plugins/plumgrid
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/plumgrid/*.ini


%files ryu
%doc LICENSE
%doc neutron/plugins/ryu/README
%{_bindir}/neutron-ryu-agent
%{_bindir}/quantum-ryu-agent
%{_unitdir}/neutron-ryu-agent.service
%{python_sitelib}/neutron/plugins/ryu
%{_datarootdir}/neutron/rootwrap/ryu-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/ryu
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ryu/*.ini


%files nec
%doc LICENSE
%doc neutron/plugins/nec/README
%{_bindir}/neutron-nec-agent
%{_bindir}/quantum-nec-agent
%{_unitdir}/neutron-nec-agent.service
%{python_sitelib}/neutron/plugins/nec
%{_datarootdir}/neutron/rootwrap/nec-plugin.filters
%dir %{_sysconfdir}/neutron/plugins/nec
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nec/*.ini


%files metaplugin
%doc LICENSE
%doc neutron/plugins/metaplugin/README
%{python_sitelib}/neutron/plugins/metaplugin
%dir %{_sysconfdir}/neutron/plugins/metaplugin
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/metaplugin/*.ini


%files vmware
%doc LICENSE
%{_bindir}/neutron-check-nvp-config
%{_bindir}/quantum-check-nvp-config
%{_bindir}/neutron-check-nsx-config
%{_bindir}/neutron-nsx-manage
%{python_sitelib}/neutron/plugins/vmware
%dir %{_sysconfdir}/neutron/plugins/nicira
%dir %{_sysconfdir}/neutron/plugins/vmware
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/nicira/*.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/vmware/*.ini


%files metering-agent
%doc LICENSE
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/metering_agent.ini
%{_unitdir}/neutron-metering-agent.service
%{_bindir}/neutron-metering-agent


%files vpn-agent
%doc LICENSE
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/vpn_agent.ini
%{_unitdir}/neutron-vpn-agent.service
%{_bindir}/neutron-vpn-agent
%{_datarootdir}/neutron/rootwrap/vpnaas.filters


%changelog
* Tue Apr 29 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-14
- Removed signing_dir from neutron-dist.conf, again (bz#1050842)

* Mon Apr 28 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-13
- Removed signing_dir from neutron.conf (bz#1050842)

* Wed Apr 23 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-12
- Removed obsolete setup scripts

* Tue Apr 22 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-11
- Pin python-novaclient dependency to >= 2.17.0

* Fri Apr 18 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-10
- Remove uneeded dep on python-keystone

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-9
- Require python-novaclient (used for Nova notifications)

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-8
- We no longer specify notification_driver in neutron-dist.conf

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-7
- Move api-paste.ini to /usr to make sure new values are applied on upgrade

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-6
- Add more build directories

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-5
- Require python-keystoneclient >= 0.7.0 to reflect upstream requirement

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-4
- Require python-keystone package

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-3
- Clean up neutron-dist.conf to reflect identical upstream defaults

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-2
- Set use_stderr = False to avoid duplicate logging for stderr

* Fri Apr 18 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-1
- Update to upstream 2014.1

* Tue Apr 15 2014 Miguel Ángel Ajo <majopela@redhat.com> -2014.1-0.19.rc2
- Include the systemd readiness notification patch

* Tue Apr 15 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.18.rc2
- Add missing dependency on python-oslo-rootwrap

* Fri Apr 11 2014 Miguel Angel Ajo <mangelajo@redhat.com> 2014.1-0.17.rc2
- Update to upstream 2014.1.rc2

* Fri Apr 11 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.1-0.16.rc1
- Use rabbitmq by default

* Thu Apr 10 2014 Miguel Ángel Ajo <majopela@redhat.com> 2014.1-0.15.rc1
- Removes the python-pyudev dependency, bz#1053001

* Thu Apr 10 2014 Ihar Hrachyshka <ihrachys@redhat.com> 2014.1-0.14.rc1
- Remove signing_dir from neutron-dist.conf, bz#1050842

* Fri Apr 04 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.13.rc1
- Fix startup issue due to invalid group permissions, bz#1080560

* Wed Apr 02 2014 Terry Wilson <twilson@redhat.com> 2014.1-0.12.rc1
- Update to upstream 2014.1.rc1
- Remove python-psutil requirement

* Mon Mar 24 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.11.b3
- Remove runtime dependency on python-pbr

* Wed Mar 19 2014 Miguel Ángel ajo <majopela@redhat.com> - 2013.1-0.10.b3
- Create agents table when ML2 core_plugin is used

* Tue Mar 11 2014 Miguel Ángel Ajo <majopela@redhat.com> - 2013.1-0.9.b3
- Forcing python-six version to be at least >= 1.4.1

* Tue Mar 11 2014 Miguel Ángel Ajo <majopela@redhat.com> - 2014.1-0.8.b3
- Updated to Icehouse milestone 3 
- Added neutron-dhcp-agent dependency bz#1019487
- Add openstack-neutron-ibm plugin
- Add openstack-neutron-ofagent plugin from ryu project

* Wed Feb 19 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.7.b2
- Sync up Quantum renaming changes

* Thu Feb 13 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.6.b2
- Rename nicira plugin to vmware

* Tue Feb 04 2014 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.5.b2
- Fix missing dependency on python-stevedore

* Mon Jan 27 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.4.b2
- Update to icehouse milestone 2

* Fri Jan 24 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.3.b1
- Remove requirements.txt, bz#1057615

* Tue Jan 07 2014 Terry Wilson <twilson@redhat.com> - 2014.1-0.2.b1
- Add python-psutil requirement for openvswitch agent, bz#1049235

* Mon Dec 23 2013 Pádraig Brady <pbrady@redhat.com> - 2014.1-0.1.b1
- Update to icehouse milestone 1

* Wed Dec 18 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2.1-1
- Update to havana stable release 2013.2.1

* Tue Dec 10 2013 Terry Wilson <twilson@redhat.com> - 2013.2-6
- Add rootwrap.conf limitation to sudoers.d/neutron, bz#984097
- neutron-server-setup: support mariadb

* Wed Dec 04 2013 Terry Wilson <twilson@redhat.com> - 2013.2-5
- Add missing debug and vpnaas rootwrap filters, bz#1034207

* Mon Dec 02 2013 Terry Wilson <twilson@redhat.com> - 2013.2-4
- Replace quantum references in neutron-dist.conf

* Wed Nov 13 2013 Terry Wilson <twilson@redhat.com> - 2013.2-3
- Add dnsmasq-utils dependency

* Wed Oct 30 2013 Terry Wilson <twilson@redaht.com> - 2013.2-2
- Better support for upgrading from grizzly to havana
- Update dependencies on python-{babel,keystoneclient,oslo-config}

* Fri Oct 18 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-1
- Update to havana GA

* Thu Oct 10 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.12.rc1
- Update to havana rc1

* Wed Oct  2 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.11.b3
- Add python-jinja2 requires to VPN agent
- Add missing services and pre/postuns for VPN and metering agents

* Thu Sep 26 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.10.b3
- Add support for neutron-dist.conf

* Tue Sep 17 2013 Pádraig Brady <pbrady@redhat.com> - 2013.2-0.9.b3
- Fix typo in openstack-neutron-meetering-agent package name

* Tue Sep 10 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.8.b3
- Add python-pbr dependency (for now)

* Mon Sep 09 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.6.b3
- Update to havana milestone 3 release

* Mon Aug 26 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.5.b2
- Add provides/obsoletes for subpackages

* Mon Aug 19 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.4.b2
- Updated to havana milestone 2 release
- Renamed quantum to neutron

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.2-0.3.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Terry Wilson <twilson@redhat.com> - 2013.2-0.2.b1
- Update to havana milestone 1 release

* Fri Jun 07 2013 Terry Wilson <twilson@redhat.com> - 2013.1.2-1
- Update to grizzly 2013.1.2 release

* Fri May 24 2013 Pádraig Brady <P@draigBrady.com> - 2013.1.1-5
- Fix inclusion of db migrations

* Thu May 23 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-4
- Fix rootwrap (bug 947793)

* Mon May 20 2013 Terry Wilson <twilson@redhat.com> - 2013.1.1-3
- Fix swapped l3-agent and lbaas-agent service definitions

* Mon May 13 2013 Gary Kotton <gkotton@redhat.com> - 2013.1.1-2
- Update to grizzly release
- Update install scripts to configure security groups
- Update install scripts to remove virtual interface configurations

* Wed Apr  3 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-1
- Update to grizzly release

* Wed Apr  3 2013 Gary Kotton <gkotton@redhat.com> - 2013.1-0.7.rc3
- Update to grizzly rc3
- Update rootwrap (bug 947793)
- Update l3-agent-setup to support qpid (bug 947532)
- Update l3-agent-setup to support metadata-agent credentials
- Update keystone authentication details (bug 947776)

* Tue Mar 26 2013 Terry Wilson <twilson@redhat.com> - 2013.1-0.6.rc2
- Update to grizzly rc2

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.Com> - 2013.1-0.5.g3
- Relax the dependency requirements on sqlalchemy

* Mon Feb 25 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.4.g3
- Update to grizzly milestone 3
- Add brocade, hyperv, midonet, and plumgrid plugins as sub-packages
- Remove cisco files that were eliminated
- Add quantum-check-nvp-config
- Include patch for https://code.launchpad.net/bugs/1132889
- Require python-oslo-config
- Require compatible version of python-sqlalchemy
- Various spec file improvements

* Thu Feb 14 2013 Robert Kukura <rkukura@redhat.com> - 2013.1-0.3.g2
- Update to grizzly milestone 2
- Add quantum-db-manage, quantum-metadata-agent,
  quantum-ns-metadata-proxy, quantum-ovs-cleanup, and
  quantum-usage-audit executables
- Add systemd units for quantum-metadata-agent and quantum-ovs-cleanup
- Fix /etc/quantum/policy.json permissions (bug 877600)
- Require dnsmasq (bug 890041)
- Add the version info file
- Remove python-lxml dependency
- Add python-alembic dependency

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-0.2.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec  5 2012 Robert Kukura <rkukura@redhat.com> - 2013.1-0.1.g1
- Update to grizzly milestone 1
- Require python-quantumclient >= 1:2.1.10
- Remove unneeded rpc control_exchange patch
- Add bigswitch plugin as sub-package
- Work around bigswitch conf file missing from setup.py

* Mon Dec  3 2012 Robert Kukura <rkukura@redhat.com> - 2012.2.1-1
- Update to folsom stable 2012.2.1
- Turn off PrivateTmp for dhcp_agent and l3_agent (bug 872689)
- Add upstream patch: Fix rpc control_exchange regression.
- Remove workaround for missing l3_agent.ini

* Fri Sep 28 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-1
- Update to folsom final
- Require python-quantumclient >= 1:2.1.1

* Sun Sep 23 2012 Gary Kotton <gkotton@redhat.com> - 2012.2-0.9.rc2
- Update to folsom rc2

* Sun Sep 16 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.9.rc1
- Fix setting admin_user in quantum_l3_setup

* Fri Sep 14 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.8.rc1
- Setup script fixes from garyk
- Fix openvswitch service config file path
- Make log file names consistent with service names

* Thu Sep 13 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.7.rc1
- Fix various issues in setup scripts
- Configure quantum-dhcp-agent to store files under /var/lib/quantum
- Make config files with passwords world-unreadable
- Replace bug workarounds with upstream patches

* Wed Sep 12 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.6.rc1
- Require python-quantumclient >= 2.0.22
- Add bug references for work-arounds
- Use /usr/share/quantum/rootwrap instead of /usr/share/quantum/filters

* Wed Sep 12 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.5.rc1
- Update to folsom rc1
- Fix command lines in agent systemd units
- Fix setup scripts
- Fix configuration of agents to use quantum-rootwrap
- Set "debug = False" and "auth_strategy = noauth" in quantum.conf
- Symlink /etc/quantum/plugin.ini to plugin's config file
- Add "--config-file /etc/quantum/plugin.ini" to ExecStart in quantum-server.service

* Tue Sep 11 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.4.rc1.20120911.1224
- Update to folsom rc1 snapshot
- Add support for new agents, plugins and rootwrap

* Wed Aug 22 2012 Pádraig Brady <P@draigBrady.com> - 2012.2-0.3.f2
- Fix helper scripts to setup the database config correctly (#847785)

* Tue Aug  7 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.2.f2
- Include quantum module no longer provided by python-quantumclient
- Update description text
- Disable setuptools_git dependency

* Tue Aug  7 2012 Robert Kukura <rkukura@redhat.com> - 2012.2-0.1.f2
- Update to folsom milestone 2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Pádraig Brady <P@draigBrady.com> - 2012.1-2
- Fix helper scripts to use the always available openstack-config util

* Mon Apr  9 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-1
- Update to essex release

* Thu Apr  5 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.7.rc2
- Update to essex rc2 milestone
- Use PrivateTmp for services

* Wed Mar 21 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.6.rc1
- Update to official essex rc1 milestone
- Add quantum-server-setup and quantum-node-setup scripts
- Use hand-coded agent executables rather than easy-install scripts
- Make plugin config files mode 640 and group quantum to protect passwords

* Mon Mar 19 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.5.e4
- Update to essex possible RC1 tarball
- Remove patches incorporated upstream
- Don't package test code
- Remove dependencies only needed by test code

* Wed Mar 14 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.4.e4
- Upstream patch: add root_helper to quantum agents
- Add sudoers file enabling quantum-rootwrap for quantum user
- Configure plugin agents to use quantum-rootwrap
- Run plugin agents as quantum user

* Fri Mar  9 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.3.e4
- Add upstream patch: remove pep8 and strict lxml version from setup.py
- Remove old fix for pep8 dependency
- Add upstream patch: Bug #949261 Removing nova drivers for Linux Bridge Plugin
- Add openvswitch dependency

* Mon Mar  5 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.2.e4
- Update to essex milestone 4
- Move plugins to sub-packages
- Systemd units for agents

* Mon Jan 30 2012 Robert Kukura <rkukura@redhat.com> - 2012.1-0.1.e3
- Update to essex milestone 3 for F17

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  17 2011 Robert Kukura <rkukura@redhat.com> - 2011.3-1
- Initial package for Fedora
