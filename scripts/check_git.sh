DATE=`date +%F_%T`
STATUS=`cd ~/blackworkers/blackworkersapp/ && git status -s`

if [[ -z "${STATUS}" ]]; then
        echo "$DATE Repo is up to date, nothing to do here."
else
        echo "$DATE Repo is out of sync, updating now"
        #/bin/bash ~/blackworkers/blackworkersapp/scripts/git-autocommit.sh
fi
