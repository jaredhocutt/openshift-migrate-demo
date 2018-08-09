FROM registry.access.redhat.com/rhel:7.5

RUN \
    yum repolist --disablerepo "*" \
    && yum-config-manager --disable "*" \
    && yum-config-manager --enable rhel-7-server-rpms \
    && yum install -y rsync

CMD ["tail", "-f", "/dev/null"]