

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

createDirectories () {
  mkdir ~/blackworkers/
  mkdir ~/blackworkers/cronlogs/
  cd ~/blackworkers/ && git clone https://github.com/blackworkers/blackworkersapp.git
}

main() {
  setup
  createDirectories
}

main

