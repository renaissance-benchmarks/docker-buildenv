
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk18.0.1.1/65ae32619e2f40f3a9af3af1851d6e19/2/GPL/openjdk-18.0.1.1_linux-x64_bin.tar.gz" -o "/tmp/jdk-18.0.1.1.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-18.0.1.1.tar.gz" \
    && rm -f "/tmp/jdk-18.0.1.1.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-18.0.1.1/bin/java 10 \
    && for i in /opt/jdk-18.0.1.1/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-18.0.1.1/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-18.0.1.1/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-18.0.1.1/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-18.0.1.1/lib/security/ \
    && /opt/jdk-18.0.1.1/bin/java -version


CMD ["/bin/bash"]

