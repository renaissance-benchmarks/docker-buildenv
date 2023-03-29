
FROM fedora:37
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_linux-x64_bin.tar.gz" -o "/tmp/jdk-13.0.2.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-13.0.2.tar.gz" \
    && rm -f "/tmp/jdk-13.0.2.tar.gz" \
    && alternatives --install /usr/bin/java java /opt/jdk-13.0.2/bin/java 10 \
    && for i in /opt/jdk-13.0.2/bin/*; do \
        ii="$( basename "$i" )"; \
        [ "$ii" != "java" ] \
            && alternatives --add-slave java "/opt/jdk-13.0.2/bin/java" "/usr/bin/$ii" "$ii" "/opt/jdk-13.0.2/bin/$ii"; \
    done \
    && mkdir -p /opt/jdk-13.0.2/lib/security/ \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-13.0.2/lib/security/ \
    && /opt/jdk-13.0.2/bin/java -version


CMD ["/bin/bash"]

