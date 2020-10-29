#The below code runs for infinite time until it is stopped and it will keep sending the correct values after 
#at intervals of 1 min


import paho.mqtt.publish as publish
import paho.mqtt.subscribe 
import random
import time

#Using Thingspeak as MQTT broker
channelID = "1210433" #channel ID of thingspeak
apiKey1 = "SRMN0UNO4AANXCY7" #write API Key of Channel 
topic = "channels/" + channelID + "/publish/" + apiKey1 # topic
mqttHost = "mqtt.thingspeak.com"
tTransport = "tcp"
tPort = 1883
tTLS = None




def sensors():
    while(True):
         # below two lines are for input of values of sensors since we are not using it 
         #so random values are initialized within a defined range
        
        hum=  random.randint(50,100)  
        temp = random.randint(20,30)
        
        # Here we check the condition of the input received 
        T = temp>=20 and temp<=30
        H = hum>=50 and hum<=100
        
        #I have taken always true condition but it can be set to any other condition also
        # then the value is published in the below code
        if( T==True and H==True ):
            tPayload = "&field1=" + str(temp) + "&field2=" + str(hum)
            print ("Temperature: ", temp)
            print ("Humidity", hum)
            try:
                publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
                print ("Valid Temperature Data sent")
                print ("Valid Humidity Data sent")
                
            except:
                print ("Failure in sending data")
        # Rest are the other cases for invalid data if data is invalid then I am sending 0 or we can send null also    
        elif(T==True and H==False):
            tPayload = "&field1=" + str(temp) + "&field2=" + str(0)
            print ("Temperature: ", temp)
            print ("Humidity", hum)
            try:
                publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
                print ("Valid Temperature Data sent")
                print ("Humidity Data Not sent")
                
            except:
                print ("Failure in sending data")
        elif(T==False and H==True):
            tPayload = "&field1=" + str(0) + "&field2=" + str(hum)
            print ("Temperature: ", temp)
            print ("Humidity", hum)
            try:
                publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
                print ("Temperature Data Not sent")
                print ("Valid Humidity  Data sent")
                
            except:
                print ("Failure in sending data")
        else:
            print("Both values Invalid")
        
        #At last this sleeps for 1 min and then next value is send
        time.sleep(60)

if __name__=="__main__":
    sensors()
        
