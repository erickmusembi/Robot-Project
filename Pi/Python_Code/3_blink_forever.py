#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
while 1:
	GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(27,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(10,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(9,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(11,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(14,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(15,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(9,GPIO.LOW)
	GPIO.output(11,GPIO.LOW)
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	time.sleep(1)