#!/bin/bash

# Prompt for user, host, and password
read -p "Enter the remote user: " REMOTE_USER
read -p "Enter the remote host: " REMOTE_HOST
read -sp "Enter the SSH password: " REMOTE_PASSWORD
echo

# Export the password to the Ansible environment variable
export ANSIBLE_HOST_KEY_CHECKING=False

# Run the Ansible playbook
ansible-playbook basic-setup.yaml \
  -i "$REMOTE_HOST," \
  -e "ansible_user=$REMOTE_USER ansible_ssh_pass=$REMOTE_PASSWORD ansible_become_pass=$REMOTE_PASSWORD"

# Unset the password from the environment
unset ANSIBLE_HOST_KEY_CHECKING