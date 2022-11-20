import RPi.GPIO as GPIO
import time
import datetime

loginterval=60 #log interval in seconds
savefilename="lightlevels.txt"
SensorPin=17
TriggerPin=27</p><p>GPIO.setmode(GPIO.BCM)
cap=0.000001 #1uf

adj=2.130620985</p><p>def measureresistance(mpin,tpin):
    GPIO.setup(mpin, GPIO.OUT)
    GPIO.setup(tpin, GPIO.OUT)
    GPIO.output(mpin, False)
    GPIO.output(tpin, False)
    time.sleep(0.2)
    GPIO.setup(mpin, GPIO.IN)
    time.sleep(0.2)
    GPIO.output(tpin, True)
    starttime=time.time()
    endtime=time.time()
    while (GPIO.input(mpin) == GPIO.LOW):
        endtime=time.time()
    return endtime-starttime
    def writeline(txt,fn):
    f = open(fn,'a')
    f.write(txt+'\n')
    f.close()
    
i=0
t=0
while True:
    stime=time.time()
    for a in range(1,11):
        res=(measureresistance(SensorPin,TriggerPin)/cap)*adj
        i=i+1
        t=t+res
        if a==10:
                t=t/i
                print(t)
                writeline(str(datetime.datetime.now())+","+str(t),savefilename)
                i=0
                t=0
    while stime+loginterval>time.time(): #wait until logtime has passed
        time.sleep(0.0001)