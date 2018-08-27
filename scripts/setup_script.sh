set -e

checkUser () {
  if [ ! `id -u bwadmin` ]; then
    echo "User bwadmin does not exist, create this user and then rerun this script"
    exit 1
  fi
}

setup() {
  if [ ~/blackworkers/ ]; then
    echo "Directory exists, do you want to delete it and resetup your environment?"
    read -p "Continue (y/n)? " choice
    case "$choice" in
      y|Y ) echo "Deleting existing app directories and rebuilding" && rm -rf ~/blackworkers/;;
      n|N ) echo "Exiting now..." && exit;;
      * ) echo "invalid";;
    esac
  fi
}

setBashrc () {
  echo "alias python=\"python3.6\"
alias pip=\"pip3.6\"
alias commit=\"/bin/bash /home/bwadmin/blackworkersapp/git_commit.sh\"
alias cda=\"cd /home/bwadmin/blackworkersapp\"" >> ~/.bashrc
}

createDirectories () {
  mkdir ~/blackworkers/
  mkdir ~/blackworkers/cronlogs/
  cd ~/blackworkers/ && git clone https://github.com/blackworkers/blackworkersapp.git
}

main() {
  checkUser
  setup
  createDirectories
}

main
