#!/bin/bash

if [ "$#" -ne 3 ] ; then
   echo "Script requires 3 arguments to execute:"
   echo -e "\t-path to spec file"
   echo -e "\t-rpm version for POM"
   echo -e "\t-R state for rpm"
   exit 1
else
   spec_path=$1
   rpm_version=$2
   r_state=$3
fi

# configure the pkgconfig path so that certain libraries like libestr can be found
#export PKG_CONFIG_PATH=/lib64/pkgconfig/:/usr/lib64/:/lib64/:$PKG_CONFIG_PATH

build_directory=$(pwd)

my_cflags="\"-I$build_directory/dependency/net-snmp-5.5/include -I$build_directory/dependency/libnet-1.1.6/build/include -I$build_directory/dependency/liblogging-1.0.5/build/include -I$build_directory/dependency/util-linux-ng-2.17.2/build/include -I$build_directory/dependency/librelp-1.2.15/build/include -I$build_directory/dependency/libestr-0.1.10/build/include -I$build_directory/dependency/libfastjson-0.99.8/build/include/libfastjson\""

#my_cflags="\"-I/proj/litpadm200/tools/net-snmp-5.5-49/include -I$build_directory/dependency/libnet-1.1.6/build/include -I$build_directory/dependency/liblogging-1.0.5/build/include -I$build_directory/dependency/json-c-0.11/build/include/json-c -I$build_directory/dependency/util-linux-ng-2.17.2/build/include -I$build_directory/dependency/librelp-1.2.7/build/include -I$build_directory/dependency/libestr-0.1.10/build/include\""

my_ldflags="\"-L$build_directory/dependency/net-snmp-5.5/snmplib/.libs -L$build_directory/dependency/libnet-1.1.6/build/lib -L$build_directory/dependency/libfastjson-0.99.8/build/lib\""

#my_ldflags="\"-L/proj/litpadm200/tools/net-snmp-5.5-49/lib -L$build_directory/dependency/libnet-1.1.6/build/lib\""

# Set package version taken from integration pom into puppet.spec file
perl -pi.bak -e "s#\<rpm.version\>#${rpm_version}#" SPEC/${spec_path}
perl -pi.bak -e "s#\<ericsson.rstate\>#${r_state}#" SPEC/${spec_path}
perl -pi.bak -e "s#\<build.directory\>#${build_directory}#" SPEC/${spec_path}

perl -pi.bak -e "s#\<my.cflags\>#${my_cflags}#" SPEC/${spec_path}
perl -pi.bak -e "s#\<my.ldflags\>#${my_ldflags}#" SPEC/${spec_path}

rpmbuild --define "_topdir %(pwd)/" --define "_builddir %{_topdir}" --define "_rpmdir %{_topdir}/RPM" --define "_specdir %{_topdir}/SPEC" --define '_rpmfilename %%{NAME}-%%{VERSION}.%%{ARCH}.rpm' --define "_sourcedir %{_topdir}/SOURCES" --define "_localstatedir /var" --define "dist .el7" --define "rhel 7" -bb SPEC/${spec_path}

