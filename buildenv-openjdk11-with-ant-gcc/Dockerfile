
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v17-openjdk11-with-ant-gcc
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk11-with-ant-gcc)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip gcc bzip2 which jq \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/jdk-11.0.2/bin/java 10 \
    && for i in /opt/jdk-11.0.2/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-11.0.2/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-11.0.2/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-11.0.2/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-11.0.2/lib/security/ \
    && /opt/jdk-11.0.2/bin/java -version \
    && curl https://downloads.apache.org/ant/binaries/apache-ant-1.10.14-bin.tar.bz2 -o /tmp/apache-ant-1.10.14-bin.tar.bz2 \
    && tar -xjf /tmp/apache-ant-1.10.14-bin.tar.bz2 -C /opt \
    && rm -f /tmp/apache-ant-1.10.14-bin.tar.bz2 \
    && ln -s /opt/apache-ant-1.10.14/bin/ant /usr/local/bin/ant

CMD ["/bin/bash"]
