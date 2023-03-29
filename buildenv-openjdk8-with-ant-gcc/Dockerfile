
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip gcc bzip2 which jq \
    && dnf install -y java-1.8.0-openjdk-devel \
    && dnf clean all \
    && curl https://downloads.apache.org/ant/binaries/apache-ant-1.10.12-bin.tar.bz2 -o /tmp/apache-ant-1.10.12-bin.tar.bz2 \
    && tar -xjf /tmp/apache-ant-1.10.12-bin.tar.bz2 -C /opt \
    && rm -f /tmp/apache-ant-1.10.12-bin.tar.bz2 \
    && ln -s /opt/apache-ant-1.10.12/bin/ant /usr/local/bin/ant


CMD ["/bin/bash"]

