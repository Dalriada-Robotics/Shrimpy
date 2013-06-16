import os, sys, RPi.GPIO as GPIO
import time
os.system('clear')
GPIO.setmode(GPIO.BOARD)
#Motors
m1f = 11
m1b = 12
m2f = 13
m2b = 18










def config():
    GPIO.setup(m1f, GPIO.OUT)
    GPIO.setup(m1b, GPIO.OUT)
    GPIO.setup(m2f, GPIO.OUT)
    GPIO.setup(m2b, GPIO.OUT)
    GPIO.output(m1f, False)
    GPIO.output(m1b, False)
    GPIO.output(m2f, False)
    GPIO.output(m2b, False)

def forward():
    GPIO.output(m1f, True)
    GPIO.output(m2f, True)

def back():
    GPIO.output(m1b, True)
    GPIO.output(m2b, True)

def left():
    GPIO.output(m1b, True)
    GPIO.output(m2f, True)

def right():
    GPIO.output(m1f, True)
    GPIO.output(m2b, True)
    
def alloff():
    GPIO.output(m1f, False)
    GPIO.output(m1b, False)
    GPIO.output(m2f, False)
    GPIO.output(m2b, False)

def control():
    done = False
    while done == False:
        bob = raw_input()
        if bob == 'w':
            forward()
        elif bob == 'a':
            left()
        elif bob == 'd':
            right()
        elif bob == 's':
            back()
        else:
            print('Done')
            done = True
        
        test = raw_input()
        alloff()

def ultrascan(ultrapin):
    GPIO.setup(ultrapin, GPIO.OUT)
    GPIO.output(ultrapin, True)
    time.sleep(0.00001)
    GPIO.output(ultrapin, False)
    start = time.time()
    GPIO.setup(ultrapin, GPIO.IN)
    while GPIO.input(ultrapin)==0:
        start = time.time()

    while GPIO.input(ultrapin)==1:
        stop = time.time()
    elapsed = stop-start
    #print(elapsed)
    distance = elapsed * 34000
    distance = distance / 2
    #print(distance)
    return(distance)
#while True:
#    time.sleep(0.5)
#    print int(abs(ultrascan(15)))
config()
#print(ultrascan(16))
control()
GPIO.cleanup()