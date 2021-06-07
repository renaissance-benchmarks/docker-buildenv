
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf clean all \
    && curl -L "https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.11%2B9_openj9-0.26.0/OpenJDK11U-jdk_x64_linux_openj9_11.0.11_9_openj9-0.26.0.tar.gz" -o "/tmp/jdk-11.0.11+9.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-11.0.11+9.tar.gz" \
    && rm -f "/tmp/jdk-11.0.11+9.tar.gz" \
    && printf 'export JAVA_HOME="%s"\nexport PATH="$JAVA_HOME/bin:$PATH"\n' "/opt/jdk-11.0.11+9" >/etc/profile.d/java_from_opt.sh \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-11.0.11+9/lib/security/ \
    && /opt/jdk-11.0.11+9/bin/java -version


CMD ["/bin/bash"]

