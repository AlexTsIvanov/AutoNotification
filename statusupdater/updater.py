from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from statusupdater import notifications
from dotenv import load_dotenv
import os
load_dotenv()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(notifications.email_sms_sender, 'interval', minutes=int(os.getenv('UPDATER', '86400')))
    scheduler.start()