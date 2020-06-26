#!/usr/bin/python
import RPi.GPIO as GPIO
import psutil
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
while True:
  try:
    sens = psutil.sensors_temperatures(fahrenheit=False)
    temp = sens['cpu_thermal'][0].current
    if temp > 50:
      GPIO.output(23, 1)
      print ("Fan ON")
      time.sleep(150)
    else:
      GPIO.output(23, 0)
      print ("Fan OFF")
      time.sleep(60)
  except:
    GPIO.cleanup()
    exit()
