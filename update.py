#!/usr/bin/env python3

import os
import sys

VERSIONS = [
    {
        "name": "openjdk8",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "package": "java-1.8.0-openjdk-devel",
    },
    {
        "name": "openjdk10",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-10.0.2",
    },
    {
        "name": "openjdk11",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "package": "java-11-openjdk-devel",
    },
    {
        "name": "openj9-openjdk11",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.11%2B9_openj9-0.26.0/OpenJDK11U-jdk_x64_linux_openj9_11.0.11_9_openj9-0.26.0.tar.gz",
        "basedir": "jdk-11.0.11+9",
    },
]

COMMON_PACKAGES = [
    "ca-certificates",
    "git",
    "unzip",
]

DOCKERFILE_TEMPLATE_FROM_PACKAGE = '''
FROM fedora:34
MAINTAINER {maintainer_email}
LABEL maintainer="{maintainer_email}"

RUN dnf install -y {common_packages} \\
    && dnf install -y {package} \\
    && dnf clean all


CMD ["/bin/bash"]

'''

# Following is not needed as we install Java via alternatives
# printf 'export JAVA_HOME="%s"\\nexport PATH="$JAVA_HOME/bin:$PATH"\\n' "/opt/{tarball_basedir}" >/etc/profile.d/java_from_opt.sh \\

DOCKERFILE_TEMPLATE_FROM_TARBALL = """
FROM fedora:34
MAINTAINER {maintainer_email}
LABEL maintainer="{maintainer_email}"

RUN dnf install -y {common_packages} \\
    && dnf clean all \\
    && curl -L "{tarball_url}" -o "/tmp/{tarball_basename}.tar.gz" \\
    && tar -xz -C /opt -f "/tmp/{tarball_basename}.tar.gz" \\
    && rm -f "/tmp/{tarball_basename}.tar.gz" \\
    && alternatives --install /usr/bin/java java /opt/{tarball_basedir}/bin/java 10 \\
    && for i in /opt/{tarball_basedir}/bin/*; do \\
        ii="$( basename "$i" )"; \\
        [ "$ii" != "java" ] \\
            && alternatives --add-slave java "/opt/{tarball_basedir}/bin/java" "/usr/bin/$ii" "$ii" "/opt/{tarball_basedir}/bin/$ii"; \\
    done \\
    && ln -sf /etc/pki/java/cacerts /opt/{tarball_basedir}/lib/security/ \\
    && /opt/{tarball_basedir}/bin/java -version


CMD ["/bin/bash"]

"""

def update_version(dockerfile, config):
    common_packages = " ".join(COMMON_PACKAGES)
    if 'package' in config:
        dockerfile.write(DOCKERFILE_TEMPLATE_FROM_PACKAGE.format(
            common_packages=common_packages,
            maintainer_email=config['maintainer'],
            package=config['package'],
        ))
    else:
        dockerfile.write(DOCKERFILE_TEMPLATE_FROM_TARBALL.format(
            common_packages=common_packages,
            maintainer_email=config['maintainer'],
            tarball_basename=config['basedir'],
            tarball_basedir=config['basedir'],
            tarball_url=config['tarball'],
        ))

def main():
    for ver in VERSIONS:
        base_dir = "buildenv-" + ver['name']
        try:
            os.mkdir(base_dir, mode = 0o777)
        except FileExistsError:
            pass
        with open(os.path.join(base_dir, 'Dockerfile'), 'w') as f:
            print("Updating {} ...".format(ver['name']), file=sys.stderr)
            update_version(f, ver)

if __name__ == '__main__':
    main()
