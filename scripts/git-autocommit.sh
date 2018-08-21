DATE=`date +%F_%T`
cd ~/blackworkers/blackworkersapp/
git add -A
git commit -m "Github Auto-commit via Blackworkers Cron $DATE"
git push origin master
