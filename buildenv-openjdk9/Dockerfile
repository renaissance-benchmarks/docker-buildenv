
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_linux-x64_bin.tar.gz" -o "/tmp/jdk-9.0.4.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-9.0.4.tar.gz" \
    && rm -f "/tmp/jdk-9.0.4.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-9.0.4/bin/java 10 \
    && for i in /opt/jdk-9.0.4/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-9.0.4/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-9.0.4/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-9.0.4/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-9.0.4/lib/security/ \
    && /opt/jdk-9.0.4/bin/java -version


CMD ["/bin/bash"]

