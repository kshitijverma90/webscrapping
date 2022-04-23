from sched import scheduler
import schedule
import time
import pywhatkit
t=20
s=0
def job():
    
    pywhatkit.sendwhatmsg('+918178758283', 'hi!!', t, 35)
    
schedule.every(10).seconds.do(job) 
schedule.every().day.at("20:35").do(job)       
while True:
    schedule.run_pending()
    time.sleep(1)