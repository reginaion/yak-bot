from apscheduler.schedulers.blocking import BlockingScheduler
import pytz

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sun')
def scheduled_job():
    url = "https://yak-bot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()