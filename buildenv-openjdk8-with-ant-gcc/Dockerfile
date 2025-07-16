
# WARNING: generated file, use update.py for updates

FROM fedora:42
LABEL org.opencontainers.image.authors="horky@d3s.mff.cuni.cz"
LABEL maintainer="horky@d3s.mff.cuni.cz"
LABEL name=renaissance-buildenv
LABEL version=v16-openjdk8-with-ant-gcc
LABEL vendor=renaissance.dev
LABEL org.opencontainers.image.description "Build environment for Renaissance benchmarks (variant openjdk8-with-ant-gcc)"

RUN dnf -y --setopt install_weak_deps=false --repo fedora --repo updates install ca-certificates git unzip gcc bzip2 which jq \
    && dnf clean all && rm -rf /var/log/*

RUN curl -L "https://download.java.net/openjdk/jdk8u44/ri/openjdk-8u44-linux-x64.tar.gz" | tar -xz -C /opt \
    && alternatives --install /usr/bin/java java /opt/java-se-8u44-ri/bin/java 10 \
    && for i in /opt/java-se-8u44-ri/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/java-se-8u44-ri/bin/java" "/usr/bin/$ii" "$ii" "/opt/java-se-8u44-ri/bin/$ii"; \
    done \
    && mkdir -p /opt/java-se-8u44-ri/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/java-se-8u44-ri/lib/security/ \
    && /opt/java-se-8u44-ri/bin/java -version \
    && curl https://downloads.apache.org/ant/binaries/apache-ant-1.10.14-bin.tar.bz2 -o /tmp/apache-ant-1.10.14-bin.tar.bz2 \
    && tar -xjf /tmp/apache-ant-1.10.14-bin.tar.bz2 -C /opt \
    && rm -f /tmp/apache-ant-1.10.14-bin.tar.bz2 \
    && ln -s /opt/apache-ant-1.10.14/bin/ant /usr/local/bin/ant

CMD ["/bin/bash"]
