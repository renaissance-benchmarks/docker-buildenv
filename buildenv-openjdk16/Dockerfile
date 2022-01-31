
FROM fedora:35
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk16.0.1/7147401fd7354114ac51ef3e1328291f/9/GPL/openjdk-16.0.1_linux-x64_bin.tar.gz" -o "/tmp/jdk-16.0.1.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-16.0.1.tar.gz" \
    && rm -f "/tmp/jdk-16.0.1.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-16.0.1/bin/java 10 \
    && for i in /opt/jdk-16.0.1/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-16.0.1/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-16.0.1/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-16.0.1/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-16.0.1/lib/security/ \
    && /opt/jdk-16.0.1/bin/java -version


CMD ["/bin/bash"]

