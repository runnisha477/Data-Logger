from time import sleep
from widgetlords.pi_spi_din import *
from widgetlords import *

init()
inputs = Mod8AI(ChipEnable.CE1)

while True:
    A1 = inputs.read_single(0)
    A2 = inputs.read_single(1)
    A3 = inputs.read_single(2)
    A4 = inputs.read_single(3)
    A5 = inputs.read_single(4)
    A6 = inputs.read_single(5)
    A7 = inputs.read_single(6)
    A8 = inputs.read_single(7)

    print("Input 1 = %4d AD Counts, %0.2f mA" % (A1, counts_to_value(A1, 745, 3723, 4, 20 )))
    print("Input 2 = %4d AD Counts, %0.2f mA" % (A2, counts_to_value(A2, 745, 3723, 4, 20 )))
    print("Input 3 = %4d AD Counts, %0.2f mA" % (A3, counts_to_value(A3, 745, 3723, 4, 20 )))
    print("Input 4 = %4d AD Counts, %0.2f mA" % (A4, counts_to_value(A4, 745, 3723, 4, 20 )))
    print("Input 5 = %4d AD Counts, %0.2f mA" % (A5, counts_to_value(A5, 745, 3723, 4, 20 )))
    print("Input 6 = %4d AD Counts, %0.2f mA" % (A6, counts_to_value(A6, 745, 3723, 4, 20 )))
    print("Input 7 = %4d AD Counts, %0.2f mA" % (A7, counts_to_value(A7, 745, 3723, 4, 20 )))
    print("Input 8 = %4d AD Counts, %0.2f mA" % (A8, counts_to_value(A8, 745, 3723, 4, 20 )))

    print("")
    sleep(0.5)