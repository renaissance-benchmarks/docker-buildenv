
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git unzip \
    && dnf install -y java-latest-openjdk-devel \
    && dnf clean all


CMD ["/bin/bash"]

