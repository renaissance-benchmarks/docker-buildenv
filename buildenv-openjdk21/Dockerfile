
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-x64_bin.tar.gz" -o "/tmp/jdk-21.0.1.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-21.0.1.tar.gz" \
    && rm -f "/tmp/jdk-21.0.1.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-21.0.1/bin/java 10 \
    && for i in /opt/jdk-21.0.1/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-21.0.1/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-21.0.1/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-21.0.1/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-21.0.1/lib/security/ \
    && /opt/jdk-21.0.1/bin/java -version


CMD ["/bin/bash"]

