#!/bin/bash
set -e

# Setup correct repo
#sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm

# Updated Yum
sudo yum -y update

# Install Python 3
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip

# Check to make sure python is installed
python3.6 -V

# Make Python 3.6 the default for the DSACC account interactive shell
echo 'alias python="python3.6"' >> ~/.bash_profile

# Make Python 3.6 the default for the DSACC account non-interactive shell
echo 'alias python="python3.6"' >> ~/.bashrc

# Make Pip 3.6 the default for the DSACC account interactive shell
echo 'alias pip="pip3.6"' >> ~/.bash_profile

# Make Pip 3.6 the default for the DSACC account non-interactive shell
echo 'alias pip="pip3.6"' >> ~/.bashrc

# Source .bashrc
source ~/.bashrc

# Upgrade Pip
sudo pip3.6 install --upgrade pip

# Install Pulp
sudo pip3.6 install pulp

# Install scrapy
sudo pip3.6 install scrapy
