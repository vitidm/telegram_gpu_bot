import schedule
from scrapping_test import connect
import datetime
import time

def job():
    if datetime.datetime.today().weekday() == 0:
        print("I'm working...")

# schedule crawler
schedule.every(5).seconds.do(connect)

# run script infinitely
while True:
    schedule.run_pending()
    time.sleep(1)