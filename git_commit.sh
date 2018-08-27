#!/bin/bash
read -p "Commit description: " desc
git add -a
git commit -m "$desc" &&
git push origin master

