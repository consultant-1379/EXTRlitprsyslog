%define _unpackaged_files_terminate_build 0

%define debug_package    %{nil}
%define rsyslog_statedir %{_sharedstatedir}/rsyslog
%define rsyslog_pkidir   %{_sysconfdir}/pki/rsyslog

%define Pidfile syslogd.pid

%global realversion 8.2002.0
%global rpmversion  <rpm.version>
%global packager    <ericsson.rstate>
%global realname    rsyslog
%global litpname    EXTRlitprsyslog
%global cxp         _CXP9032140
%global newpkgname  %{litpname}%{cxp}

# rsyslog addon packages
%global elastic_cxp_name     %{litpname}elasticsearch_CXP9032173
%global gnutls_cxp_name      %{litpname}gnutls_CXP9032174
%global mmanon_cxp_name      %{litpname}mmanon_CXP9032175
%global mmfields_cxp_name    %{litpname}mmfields_CXP9032176
%global mmjsonparse_cxp_name %{litpname}mmjsonparse_CXP9032177
%global mmutf8fix_cxp_name   %{litpname}mmutf8fix_CXP9032178
%global mysql_cxp_name       %{litpname}mysql_CXP9032179
%global ommail_cxp_name      %{litpname}ommail_CXP9032180
%global pgsql_cxp_name       %{litpname}pgsql_CXP9032181
%global pmciscoios_cxp_name  %{litpname}pmciscoios_CXP9032182
%global snmp_cxp_name        %{litpname}snmp_CXP9032184
%global udpspoof_cxp_name    %{litpname}udpspoof_CXP9032185


%global _exec_prefix %{nil}
%global _libdir %{_exec_prefix}/%{_lib}

Summary: Enhanced system logging and kernel message trapping daemon
Name:     %{newpkgname}
Version:  %{rpmversion}
Release:  2%{?dist}
License:  (GPLv3+ and ASL 2.0)
Group:    System Environment/Daemons
URL:      http://www.ericsson.com
Packager: %{packager}
Provides: %{realname} = %{realversion}

Source0: http://www.rsyslog.com/files/download/%{realname}/%{realname}-%{realversion}.zip
Source2: rsyslog_v7.conf
Source3: rsyslog.sysconfig
Source4: rsyslog.log.epel6
Patch0:  rsyslog.service.patch

BuildRequires: curl-devel
BuildRequires: zlib-devel%{?_isa}
BuildRequires: systemd-devel >= 219-39

Requires: logrotate >= 3.5.2
Requires: bash >= 2.0

Requires(post):   /bin/systemctl coreutils
Requires(preun):  /bin/systemctl
Requires(postun): /bin/systemctl

Provides:  syslog
Obsoletes: sysklogd < 1.5-11
BuildRoot: %{_tmppath}/%{realname}-%{realversion}-%{release}-root-%(%{__id_u} -n)

###### Rsyslog Subpackages #####

%package -n %{mysql_cxp_name}
Summary: MySQL support for rsyslog
Group: System Environment/Daemons
Provides: %{realname}-mysql = %{realversion}
Requires: %realname = %realversion-%release
BuildRequires: mysql >= 4.0
BuildRequires: mysql-devel >= 4.0

# post install script to restart rsyslog when the subpackage is installed
%post -n %{mysql_cxp_name}
echo "installed package %{mysql_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{pgsql_cxp_name}
Summary: PostgresSQL support for rsyslog
Group: System Environment/Daemons
Provides: %{realname}-pgsql = %{realversion}
Requires: %realname = %realversion-%release
BuildRequires: postgresql-devel

%post -n %{pgsql_cxp_name}
echo "installed package %{pgsql_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{gnutls_cxp_name}
Summary: TLS protocol support for rsyslog
Group: System Environment/Daemons
Provides: %{realname}-gnutls = %{realversion}
Requires: %realname = %realversion-%release
BuildRequires: gnutls-devel
BuildRequires: libgcrypt-devel

%post -n %{gnutls_cxp_name}
echo "installed package %{gnutls_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{snmp_cxp_name}
Summary: SNMP protocol support for rsyslog
Group: System Environment/Daemons
Provides: %{realname}-snmp = %{realversion}
Requires: %realname = %realversion-%release

%post -n %{snmp_cxp_name}
echo "installed package %{snmp_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{udpspoof_cxp_name}
Summary: Provides the omudpspoof module
Group: System Environment/Daemons
Requires: %realname = %realversion-%release

%post -n %{udpspoof_cxp_name}
echo "installed package %{updspoof_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service


%package -n %{mmjsonparse_cxp_name}
Summary: mmjsonparse support
Group: System Environment/Daemons
Provides: %{realname}-mmjsonparse = %{realversion}
Requires: %realname = %realversion-%release

%post -n %{mmjsonparse_cxp_name}
echo "installed package %{mmjsonparse_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{mmfields_cxp_name}
Summary: mmfields support
Group: System Environment/Daemons
Provides: %{realname}-mmfields = %{realversion}
Requires: %realname = %realversion-%release

%post -n %{mmfields_cxp_name}
echo "installed package %{mmfields_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{mmanon_cxp_name}
Summary: mmanon support
Group: System Environment/Daemons
Provides: %{realname}-mmanon = %{realversion}
Requires: %realname = %realversion-%release

%post -n %{mmanon_cxp_name}
echo "installed package %{mmanon_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{mmutf8fix_cxp_name}
Summary: mmutf8fix support
Group: System Environment/Daemons
Provides: %{realname}-mmutf8fix = %{realversion}
Requires: %realname = %realversion-%release

%post -n %{mmutf8fix_cxp_name}
echo "installed package %{mmutf8fix_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{ommail_cxp_name}
Summary: Mail support
Group: System Environment/Daemons
Provides: %{realname}-ommail = %{realversion}
Requires: %realname = %realversion-%release

%post -n %{ommail_cxp_name}
echo "installed package %{ommail_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{pmciscoios_cxp_name}
Summary: pmciscoios support
Provides: %{realname}-pmciscoios = %{realversion}
Group: System Environment/Daemons
Requires: %realname = %realversion-%release

%post -n %{pmciscoios_cxp_name}
echo "installed package %{pmciscoios_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%package -n %{elastic_cxp_name}
Summary:       Provides the omelasticsearch module
Provides:      %{realname}-elasticsearch = %{realversion}
Requires:      %{realname} = %{realversion}-%release
BuildRequires: libcurl-devel

%post -n %{elastic_cxp_name}
echo "installed package %{elastic_cxp_name}, restarting rsyslog ..."
systemctl restart rsyslog.service

################################

%description
Rsyslog is an enhanced, multi-threaded syslog daemon. It supports MySQL,
syslog/TCP, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is compatible with stock sysklogd
and can be used as a drop-in replacement. Rsyslog is simple to set up, with
advanced features suitable for enterprise-class, encryption-protected syslog
relay chains.

%description -n %{mysql_cxp_name}
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.

%description -n %{pgsql_cxp_name}
The rsyslog-pgsql package contains a dynamic shared object that will add
PostgreSQL database support to rsyslog.

%description -n %{gnutls_cxp_name}
The rsyslog-gnutls package contains the rsyslog plugins that provide the
ability to receive syslog messages via upcoming syslog-transport-tls
IETF standard protocol.

%description -n %{snmp_cxp_name}
The rsyslog-snmp package contains the rsyslog plugin that provides the
ability to send syslog messages as SNMPv1 and SNMPv2c traps.

%description -n %{udpspoof_cxp_name}
This module is similar to the regular UDP forwarder, but permits to
spoof the sender address. Also, it enables to circle through a number
of source ports.

%description -n %{mmjsonparse_cxp_name}
The rsyslog-mmjsonparse package provides mmjsonparse filter support.

%description -n %{mmfields_cxp_name}
Parse all fields of the message into structured data inside the JSON tree.

%description -n %{mmanon_cxp_name}
IP Address Anonimization Module (mmanon).
It is a message modification module that actually changes the IP address
inside the message, so after calling mmanon, the original message can
no longer be obtained. Note that anonymization will break digital
signatures on the message, if they exist.

%description -n %{mmutf8fix_cxp_name}
UTF-8 Fix support (mmutf8fix).
The mmutf8fix module permits to fix invalid UTF-8 sequences. Most often, such
invalid sequences result from syslog sources sending in non-UTF character
sets, e.g. ISO 8859. As syslog does not have a way to convey the character
set information, these sequences are not properly handled.

%description -n %{pmciscoios_cxp_name}
Parser module which supports various Cisco IOS formats.

%description -n %{ommail_cxp_name}
Mail Output Module.
This module supports sending syslog messages via mail. Each syslog message
is sent via its own mail. The ommail plugin is primarily meant for alerting users.
As such, it is assume that mails will only be sent in an extremely
limited number of cases.

%description -n %{elastic_cxp_name}
The rsyslog-elasticsearch package provides omelasticsearch module support.



%prep
%setup -q -n %{realname}-%{realversion}
%patch0 -p0

%build

%ifarch sparc64
export CFLAGS="-g $RPM_OPT_FLAGS -fPIE -DSYSLOGD_PIDNAME=\\\"%{Pidfile}\\\" -std=c99"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%else
export CFLAGS="-g $RPM_OPT_FLAGS -fpie -DSYSLOGD_PIDNAME=\\\"%{Pidfile}\\\" -std=c99"
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"
%endif


export CFLAGS=<my.cflags>
export LDFLAGS=<my.ldflags>
export LIBLOGGING_STDLOG_CFLAGS=<build.directory>/dependency/liblogging-1.0.5/build/include
export LIBLOGGING_STDLOG_LIBS=<build.directory>/dependency/liblogging-1.0.5/build/lib/liblogging-stdlog.so
export JSON_C_CFLAGS=<build.directory>/dependency/json-c-0.11/build/include
export JSON_C_LIBS=<build.directory>/dependency/json-c-0.11/build/lib/libjson-c.so
export LIBFASTJSON_CFLAGS=<build.directory>/dependency/libfastjson-0.99.8/build/include
export LIBFASTJSON_LIBS=<build.directory>/dependency/libfastjson-0.99.8/build/lib/libfastjson.so.4
export LIBUUID_CFLAGS=<build.directory>/dependency/util-linux-ng-2.17.2/build/include
export LIBUUID_LIBS=<build.directory>/dependency/util-linux-ng-2.17.2/build/lib/libuuid.so
export LIBESTR_CFLAGS=<build.directory>/dependency/libestr-0.1.10/build/include
export LIBESTR_LIBS=<build.directory>/dependency/libestr-0.1.10/build/lib/libestr.so


./autogen.sh


%configure --disable-static \
        --disable-testbench \
        --disable-usertools \
        --enable-libgcrypt \
        --disable-guardtime \
        --enable-uuid \
        --enable-elasticsearch \
        --disable-ommongodb \
        --enable-usertools \
        --enable-gnutls \
        --enable-gssapi-krb5 \
        --enable-imdiag \
        --enable-imfile \
        --enable-imjournal \
        --enable-impstats \
        --enable-imptcp \
        --disable-libdbi \
        --enable-mail \
        --enable-mmanon \
        --enable-mmcount \
        --enable-mmjsonparse \
        --enable-mmpstrucdata \
        --enable-mmsequence \
        --enable-mmsnmptrapd \
        --enable-mmfields \
        --enable-omjournal \
        --enable-pmciscoios \
        --disable-mmnormalize \
        --enable-mmutf8fix \
        --enable-mysql \
        --enable-omudpspoof \
        --enable-omprog \
        --enable-omuxsock \
        --enable-pgsql \
        --enable-pmaixforwardedfrom \
        --enable-pmcisconames \
        --enable-pmlastmsg \
        --enable-pmsnare \
        --enable-snmp \
        --enable-unlimited-select \
        --disable-generate-man-pages \
        --enable-pmnull \

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/rsyslog.d
install -d -m 700 $RPM_BUILD_ROOT%{rsyslog_statedir}
install -d -m 700 $RPM_BUILD_ROOT%{rsyslog_pkidir}

install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rsyslog
install -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/syslog
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/rsyslog.conf



rm $RPM_BUILD_ROOT/%{_libdir}/rsyslog/*.la


%clean
rm -rf $RPM_BUILD_ROOT


%post
for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	umask 066 && touch $n
done

ln -s /usr/lib/systemd/system/rsyslog.service /usr/lib/systemd/system/syslog.service
if [ -f /bin/systemctl ]; then
    systemctl daemon-reload
    systemctl enable rsyslog
fi
systemctl start syslog.socket

# make sure rsyslog starts post install
systemctl start rsyslog.service

%preun
if [ $1 -eq 0 ]; then
    systemctl --no-reload disable rsyslog.service > /dev/null 2>&1 || :
    systemctl stop rsyslog.service > /dev/null 2>&1 || :
    systemctl stop syslog.socket > /dev/null 2>&1 || :
fi

%postun
rm -f /usr/lib/systemd/system/syslog.service
if [ $1 -ge 1 ]; then
    systemctl try-restart rsyslog.service > /dev/null 2>&1 || :
fi


%triggerun -- rsyslog < 5.7.8-1
[ -f /var/lock/subsys/rsyslogd ] || exit 0
mv /var/lock/subsys/rsyslogd /var/lock/subsys/rsyslog
[ -f /var/run/rklogd.pid ] || exit 0
/bin/kill `cat /var/run/rklogd.pid 2> /dev/null` > /dev/null 2>&1 ||:

%files
%defattr(0755,root,root,0755)
%attr(644,root,root) %{_sysconfdir}/logrotate.d/syslog
%doc AUTHORS COPYING* NEWS README ChangeLog
%dir %{_libdir}/rsyslog
%{_libdir}/rsyslog/imfile.so
%{_libdir}/rsyslog/imjournal.so
%{_libdir}/rsyslog/imklog.so
%{_libdir}/rsyslog/immark.so
%{_libdir}/rsyslog/impstats.so
%{_libdir}/rsyslog/imptcp.so
%{_libdir}/rsyslog/imtcp.so
%{_libdir}/rsyslog/imudp.so
%{_libdir}/rsyslog/imuxsock.so
%{_libdir}/rsyslog/lmnet.so
%{_libdir}/rsyslog/lmnetstrms.so
%{_libdir}/rsyslog/lmnsd_ptcp.so
%{_libdir}/rsyslog/lmregexp.so
%{_libdir}/rsyslog/lmtcpclt.so
%{_libdir}/rsyslog/lmtcpsrv.so
%{_libdir}/rsyslog/lmzlibw.so
%{_libdir}/rsyslog/omjournal.so
%{_libdir}/rsyslog/omtesting.so
%{_libdir}/rsyslog/ommail.so
%{_libdir}/rsyslog/omprog.so
%{_libdir}/rsyslog/omuxsock.so
%{_libdir}/rsyslog/pmlastmsg.so
%{_libdir}/rsyslog/lmcry_gcry.so
%{_libdir}/rsyslog/mmpstrucdata.so
%{_libdir}/rsyslog/mmsequence.so
%{_libdir}/rsyslog/mmexternal.so

#NEW
%{_libdir}/rsyslog/pmnull.so


%if 0%{?rhel} >= 6
%{_bindir}/rscryutil
%endif

%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/rsyslog
%config(noreplace) %{_sysconfdir}/logrotate.d/syslog
%dir %{_sysconfdir}/rsyslog.d
%dir %{rsyslog_statedir}
%dir %{rsyslog_pkidir}
%{_sbindir}/rsyslogd
%{_mandir}/*/*
%if 0%{?rhel} >= 7
%attr(644,root,root) %{_unitdir}/rsyslog.service
%endif

%files -n %{mysql_cxp_name}
%defattr(0755,root,root,0755)
%doc plugins/ommysql/createDB.sql
%{_libdir}/rsyslog/ommysql.so

%files -n %{pgsql_cxp_name}
%defattr(0755,root,root,0755)
%doc plugins/ompgsql/createDB.sql
%{_libdir}/rsyslog/ompgsql.so

%files -n %{gnutls_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/lmnsd_gtls.so

%files -n %{snmp_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/omsnmp.so

%files -n %{udpspoof_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/omudpspoof.so

%files -n %{mmjsonparse_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/mmjsonparse.so

%files -n %{mmfields_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/mmfields.so

%files -n %{mmanon_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/mmanon.so

%files -n %{pmciscoios_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/pmciscoios.so

%files -n %{mmutf8fix_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/mmutf8fix.so

%files -n %{ommail_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/ommail.so

%files -n %{elastic_cxp_name}
%defattr(0755,root,root,0755)
%{_libdir}/rsyslog/omelasticsearch.so


