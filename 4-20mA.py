#Thermistor inputs for 8 channels of temperature measurement
#counts_to_value(reading_ad_counts, zero_ad_counts, span_ad_counts, zero_value, span_value )

#where:

#reading_ad_counts = actual A/D counts from the channel
#zero_ad_counts = A/D counts to represent the Zero Value
#span_ad_counts = A/D counts to represent the Span Value
#zero_value = Zero Value ie: 0 mA or 4 mA
#span_value = Span Value ie: 20 mA

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
    Temp = counts_to_value(A1, 745, 3723, 4, 20 )
    file = open("Datalogger4-20mA.csv","a")
    file.write("{0:0.2f}".format(Temp)+",")
    file.write(datetime.today().strftime('%Y-%m-%d'+"," '%H:%M:%S')+"\n")
    sleep(1)
    print(Temp)
    file.close()
