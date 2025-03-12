# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   comma
31 13 * * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_ygainers;  make ygainers.csv; python ygainers_crontab_csv.py; make clean_ygainers; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
30 16 * * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_ygainers;  make ygainers.csv; python ygainers_crontab_csv.py; make clean_ygainers; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
01 20 * * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_ygainers;  make ygainers.csv; python ygainers_crontab_csv.py; make clean_ygainers; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
#31 13 6-14 * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
#30 16 6-14 * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
#01 20 6-14 * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
#52 16 6-14 * * cd home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_wsjgainers;  make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers
#51 13 6-14 3 1-5 cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; echo "this is a test" > /home/ubuntu/SP25_DS5111_uwa6xv/collected_data/testfile.txt
#* * * * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_ygainers;  make ygainers.csv; python ygainers_crontab_csv.py; make clean_ygainers; make clean_wsjgainers; make wsjgainers.csv; python wsjgainers_crontab_csv.py; make clean_wsjgainers 
#* * * * * cd /home/ubuntu/SP25_DS5111_uwa6xv; . env/bin/activate; make clean_wsjgainers; make wsjgainers.csv; date >> debug.txt; python wsjgainers_crontab_csv.py; 
