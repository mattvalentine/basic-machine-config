# Basic Linux Machine Configuration

## Summary

This repo has a bunch of scripts to setup an Ubuntu Server (not Desktop) instance (on a Nuc, or a Pi, or whatever) be a fullscreen gui that's locked down as a basis for building linux based appliances.

It loads a minimum viable window manager (see standby-screen folder) to run within lightdm in an X session (maybe wayland someday, but not yet).

It also installs some shell stuff like oh-my-zsh, and allows sudoers to sudo without their password (obviously you have the password if you are logged in as that user, so why make your life harder?) Other little niceties like cranking down the niceness and setting DISPLAY=:0 for ssh users are also in there.

This was built from much larger project specific scripts I've built in the past. It intentionally leaves a lot of things out like loading node via nvm or initializing pm2, or installing ROS2. So feel free to fork it and add what you need.

The only updates I have in mind right now are a better standby screen.

## Prerequisites

Install Ubuntu Server 22.04 or 24.04, and record the user, password, and address, and make sure you can ssh into it and run sudo commands.

Should work on Linux, Windows (via WSL), or mac. First, install ansible and sshpass:

```bash
sudo apt install software-properties-common sshpass
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt update
sudo apt install ansible 
```

or on Mac

```bash
brew install ansible sshpass
```

Recommended, but not required:
`sudo apt update && sudo apt install avahi-daemon && sudo apt full-upgrade` on the machine before install. This should make sure things are up to date, and allow the use of `<hostname>.local` on local networks via MDNS.

## Run

```bash
./run.sh
```

should prompt you for username, address (ip or host), and password:

```bash
Enter the remote user: mycooluser
Enter the remote host: mycoolappliance.local
Enter the SSH password: 
```

and then it should run the ansible scripts. It can take a while to run (especially `Install packages`), by all means go get lunch or grab a beer or something. If you get antsy like me, feel free to ssh in from another terminal session, and open top to monitor for dpkg and apt-get commands to make yourself feel more confident that it's still working.

If it's successful, it should reboot a minute or so after the script completes, and show it's hostname and IP address on grey background. From there you can ssh in and run whatever you want. Try to ssh in and run `glxgears` to test. 

If you want a logo other than the default durring boot up and shutdown, just swap in a different png file.

Happy hacking!
