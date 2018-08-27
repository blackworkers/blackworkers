#!/bin/bash
set -e

# Set Bintray Repo
wget https://bintray.com/rabbitmq/rpm/rpm -O bintray-rabbitmq-rpm.repo

# Move repo to yum.repos.d
sudo mv bintray-rabbitmq-rpm.repo /etc/yum.repos.d/

# Install Erlang for RabbitMQ
sudo yum -y install erlang

# Install RabbitMQ
sudo yum -y install rabbitmq-server
