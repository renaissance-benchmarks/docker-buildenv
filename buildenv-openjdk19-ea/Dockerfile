
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/early_access/jdk19/7/GPL/openjdk-19-ea+7_linux-x64_bin.tar.gz" -o "/tmp/jdk-19.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-19.tar.gz" \
    && rm -f "/tmp/jdk-19.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-19/bin/java 10 \
    && for i in /opt/jdk-19/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-19/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-19/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-19/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-19/lib/security/ \
    && /opt/jdk-19/bin/java -version


CMD ["/bin/bash"]

