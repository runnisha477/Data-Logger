# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:13:01 2022
@author: Haris Ihsannur
"""

import time
from datetime import datetime
from time import sleep
from widgetlords.pi_spi import *
from widgetlords import *

init()
inputs = Mod8AI()
A3 = inputs.read_single(2) #pin A3

#Thermistor inputs for 8 channels of temperature measurement
#counts_to_value(reading_ad_counts, zero_ad_counts, span_ad_counts, zero_value, span_value )

#where:
reading_ad_counts = A3 # actual A/D counts from the channel
zero_ad_counts = 745 # A/D counts to represent the Zero Value
span_ad_counts = 3723 # A/D counts to represent the Span Value
zero_value = 4 # Zero Value ie: 0 mA or 4 mA
span_value = 20 # Span Value ie: 20 mA

Logging = 0

while Logging < 10: # Iterasi pengumpulan data 10 kali
    Temp = counts_to_value(reading_ad_counts, zero_ad_counts, span_ad_counts, zero_value, span_value )   
    file = open("Datalogger4-20mA.csv","a")
    file.write(datetime.today().strftime('%Y-%m-%d'+" "'%H:%M:%S')+",")
    file.write("{0:0.2f}".format(Temp)+"mA"+"\n")
    sleep(0.5)
    print("{0:0.2f}".format(Temp)+" mA")
    Logging = Logging + 1
    file.close()