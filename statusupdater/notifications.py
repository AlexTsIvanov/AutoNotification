
from inspection.models import *
from datetime import datetime,timedelta
import smtplib
from pushbullet import Pushbullet
from dotenv import load_dotenv
import os
load_dotenv()

def email_sms_sender():
    next_check_all = datetime.today() + timedelta(days=int(os.getenv('PERIOD', '365')))
    nextcheck_date = next_check_all.strftime('%Y-%m-%d')

    checks = Inspection.objects.filter(next_check = nextcheck_date , status = "Inspection Period Not Over")

    # EMAIL Logic
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo() #identifies with mail server
        smtp.starttls() #encrypt traffic
        smtp.ehlo() #reidentifies

        smtp.login(user= os.getenv('EMAIL_USER', ' '), password= os.getenv('EMAIL_PASSWORD', ' '))
        for check in checks:
            subject = 'Vehicle Inspection'
            
            body = f'Technical Inspection for {check.vehicle.reg_number} needs to be renewed in 7 days.'  #{check.vehicle.reg_number}

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail('no.reply.technical.inspection@gmail.com', check.email, msg)  #check.email
            check.status = "Customer Notified Successfully"
            check.save()


    # SMS Logic
    API_KEY = os.getenv('API_KEY', ' ')
    pb = Pushbullet(API_KEY)
    phone = pb.devices[0]
    for check in checks:

        pb.push_sms(phone, {check.client_telnumber}, f'Technical Inspection for {check.vehicle.reg_number} needs to be renewed in 7 days.')