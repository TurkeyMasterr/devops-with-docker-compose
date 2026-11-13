# 2.11: containerized dev environment for logcount

## The project
Logcount is a small Python script that reads a web server access log and counts how many requests came from each IP address. It prints the IPs from most to least frequent, with the count before each one, and then names the top IP.

## What I containerized
The compose file reuses my published image, [turkeymasterr/logcount](https://hub.docker.com/r/turkeymasterr/logcount), and bind-mounts this folder onto `/usr/src/app` inside the container. The mount covers the copy of the script baked into the image, so the container runs the version in this folder. The compose `command` passes `sample.log` to the script. On Fedora, `security_opt` with `label=disable` is needed so SELinux doesn't block the mount.

## Why
- Nothing but Docker has to be installed on the host. There's no Python setup.
- Edits to `logcount.py` take effect on the next run without rebuilding the image.
- The dev environment runs the same image as the published one, so it behaves the same way.

## How to run it
From this folder:

    docker compose -f logcount-compose.yaml up

The container prints the counts and the top IP, then exits. To change the script, edit `logcount.py` and run the same command again.

