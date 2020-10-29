#The below code runs for infinite time until it is stopped and it will keep checking the avergae value
#of Humiditiy, temperature etc after every 5 min and will sent an alert email if value received is abnormal


import time
import urllib
import json
import smtplib, ssl

#below are the credentials for Thingspeak

channelID = "1210433"
apiKey2 = "Y4MJCVGZOYP4VF4A"
x1="http://api.thingspeak.com/channels/"
x2="/feeds.json?api_key="
x3="&results=2"
x= x1+channelID +x2  + apiKey2


# The below function uses smtp server to send email alerts
def send_email():
    port = 465  
    smtp_server = "smtp.gmail.com"
    sender_email = "sender_email_id"  # Enter your address
    receiver_email = "receiver_email_id"  # Enter receiver address
    password = input() 
    message = """\
    Subject: Alert from Sensor!

    HUmidity/Temperature is above average level."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Success")
#This function reads and calculate the average value of Humidity/Temperature in every 
#5 min and send the email alert if abnormal value
def alert():
    TS = urllib.request.urlopen(x)

    response = TS.read()
    data=json.loads(response)

    t=[]
    h=[]
    z=len(data['feeds'])

    for i in range(z-1,z-6,-1):
        t.append(int(data['feeds'][i]['field1']))
    for j in range(z-1,z-6,-1):
        h.append(int(data['feeds'][j]['field2']))

    t_avg=sum(t_5)/5
    h_avg=sum(h_5)/5
    print(t_avg)
    print(h_avg)
    if (t_avg>30):
        send_email()
        print("Alert Sent")
    else:
        print("Safe")
    if( h_avg> 80):
        send_email()
        print("Alert")
    else:
        print("Safe")


if __name__=="__main__":
    while(True):
        alert()
        time.sleep(300)
