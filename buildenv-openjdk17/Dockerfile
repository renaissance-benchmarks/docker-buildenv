
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_linux-x64_bin.tar.gz" -o "/tmp/jdk-17.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-17.tar.gz" \
    && rm -f "/tmp/jdk-17.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-17/bin/java 10 \
    && for i in /opt/jdk-17/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-17/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-17/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-17/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-17/lib/security/ \
    && /opt/jdk-17/bin/java -version


CMD ["/bin/bash"]

