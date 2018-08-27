#!/bin/bash
set -e

# Enable Postgres Repo
sudo yum install -y https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-redhat10-10-2.noarch.rpm

# Download Client Packages
sudo yum -y install postgresql10

# Download and install the server Packages
sudo yum -y install postgresql10-server

# Setup the DB
sudo /usr/pgsql-10/bin/postgresql-10-setup initdb

# Enable at Startup
sudo systemctl enable postgresql-10

# Start Postgres
sudo systemctl start postgresql-10
