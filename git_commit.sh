#!/bin/bash

set -e

read -p "Commit description: " desc
git add -A
git commit -m "$desc" &&
git push origin master

