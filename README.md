# Docker images for Renaissance infrastructure

Images are available through GitHub repository at
<https://github.com/renaissance-benchmarks/docker-buildenv/pkgs/container/renaissance-buildenv>.

The versioning scheme is `vNUM-JAVA_VARIANT` where `NUM` is version number
(we use plain increasing integers) and `JAVA_VARIANT` is a particular Java
version such as `openjdk20`.

## Maintenance notes

Individual `Dockerfile`s are generated from `update.py` where common parts
are kept, version information (and information about base image) is kept
inside `version.rc`.

Every non-trivial update (i.e. changes generated `Dockerfile`) must bump the
version in `version.rc`.

Every commit and pull request is automatically built using GitHub Actions,
tag pushes also updates (pushes) the Docker images.

### Local testing

Images can be built using the `buildah-build.sh` script that receives a list
of directories to build (i.e. the directories where `Dockerfile` is).
Generated images are tagged according to information in `version.rc` with
`localhost/` as repository prefix.

The **deprecated** script `list-images-to-push.sh` lists locally built images
that can be pushed to the remote repository. Its function is superseeded by
the automated builds here on GitHub via Git tags.

The script `run-javas-in-podman.sh` runs `java -version` in all images built
previously by the `buildah-build.sh` script.

Test runs of Renaissance JAR can be executed via `run-renaissance-in-podman.sh`
that takes single argument: local path to built `renaissance.jar`.
The script then executes Renaissance benchmarks in all images built by
the `buildah-build.sh` script.
Extra arguments can be used to specify arguments for the actual run, thus
_replacing_ the defaults of `-r 1 -c test all` (that are used for fast
execution).
Running with `env images=REGEX run-renaissance-in-podman.sh ...` will filter
the images names to given `REGEX`, running the same way with `jvm_args` will
add extra arguments to the JVM
(e.g. `env jvm_args="-Djava.security.manager=allow" ...`).
