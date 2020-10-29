# MQTT-Server-Data-and-Email-Alert
It sends sensor data to Thingspeak and send email alerts if abnormal value is found.

This contains two files: - 

1) Sensor_Data_Module.py 

Run the above file-> python Sensor_Data_Module.py (CMD)

The above code is to publish the sensor data to MQTT Broker at regular intervals of 1 min.

2) Alert_Module.py


Run the above file-> python Alert_Module.py (CMD)

The above code is an alert module which sends an email in intervals of 5 min by checking the average value of the sensor data for last 5 mins.

****Run both the codes simultaneously so that both the modules work together.****
