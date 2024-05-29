# Basic Linux Machine Configuration

## Summary

This repo has a bunch of scripts to setup an Ubuntu Server (not Desktop) instance (on a Nuc, or a Pi, or whatever) be a fullscreen gui that's locked down as a basis for building linux based appliances.

## Prerequisites

Install Ubuntu Server 22.04 on the device (24.04 might work too, but need to test), and record the user, password, and address, and make sure you can ssh into it and run sudo commands.

Should work on Linux, Windows (via WSL), or mac. First, install ansible and sshpass:

```bash
sudo apt install ansible sshpass
```

or on Mac

```bash
brew install ansible sshpass
```

Recommended: `sudo apt update && sudo apt install avahi-daemon && sudo apt full-upgrade` on the machine before install. This should make sure things are up to date, and allow the use of `<hostname>.local` on local networks via MDNS.

## Run

```bash
./run.sh
```

should prompt you for username, address (ip or host), and password:

```
Enter the remote user: dluser
Enter the remote host: dl-mycoolexhibitname.local
Enter the SSH password: 
```

and then it should run the ansible scripts.

If it's successful, it should reboot a minute or so after the script completes, and show it's hostname and IP address on grey background. From there you can ssh in and run whatever you want. Happy hacking!
