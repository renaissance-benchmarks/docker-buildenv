
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/early_access/jdk18/33/GPL/openjdk-18-ea+33_linux-x64_bin.tar.gz" -o "/tmp/jdk-18.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-18.tar.gz" \
    && rm -f "/tmp/jdk-18.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-18/bin/java 10 \
    && for i in /opt/jdk-18/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-18/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-18/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-18/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-18/lib/security/ \
    && /opt/jdk-18/bin/java -version


CMD ["/bin/bash"]

