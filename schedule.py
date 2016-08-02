import parseRate, gmailSender
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

sched = BlockingScheduler()

# @sched.scheduled_job('interval', seconds=10)
# def timed_job():
#     pass

@sched.scheduled_job('cron', day_of_week='mon-fri', hour='9-17', minute='0-59')
def jpy_job():
    currentRate = parseRate.getCurrentRate()
    if None == currentRate:
        print("The rate value have not get")
        return

    if parseRate.alarmRate > currentRate:
        toAddrs = ['to@gmail.com']
        sender = gmailSender.GmailSender()
        sender.send(toAddrs, "The JPY rate that is over alarm now {}".format(currentRate))
        print("success for send mail")
    else:
        print("[{}] The current rate {} that is not over the alarm.".format(datetime.datetime.now(), currentRate))

sched.start()


