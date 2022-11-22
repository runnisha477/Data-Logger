#Thermistor inputs for 8 channels of temperature measurement
#Temp = steinhart_hart(r_temp, beta, max_ad_counts, reading_ad_counts)
#where:

#Temp = the formatted reading as Deg C
#r_temp = the Thermistor Ohms at Room Temperature (25 Deg.C)
#beta = the Beat value of the Thermistor being used
#max_ad_counts = the maximum ad counts ie: 4095 for a 12 bit A/D converter
#reading_ad_counts = the actual A/D counts read.

import time
from datetime import datetime
from time import sleep
from widgetlords.pi_spi import *
from widgetlords.pi_spi_din import *
from widgetlords import *

init()
inputs = Mod8AI(ChipEnable.CE1)


while True:
    A1 = inputs.read_single(0)
    Temp = steinhart_hart(10000, 3380, 4095, A1)
    file = open("DataloggerA1.csv","a")
    file.write("{0:0.2f}".format(Temp)+",")
    file.write(datetime.today().strftime('%Y-%m-%d'+"," '%H:%M:%S')+"\n")
    sleep(1)
    print(Temp)
    file.close()