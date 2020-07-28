from common import *


def toAdrs(dec, adrs):
    newad = ""
    lastdig = dec[::-1]
    last = lastdig[:3:]
    lastnum = int(last[::-1])
    fa = 1
    la = lastnum - 1
    # address making
    newad = ''.join(adrs)

    print("First Host: ", newad + str(fa))
    print("Last Host: ", newad + str(la))
def lh(host,base):
    last_adrs=lastbitchanger(binstr=binarymaker(base),bits=bitsCounter(host))
    last_adrs=todecimal(last_adrs)
    toAdrs(dec=last_adrs,adrs=base[:len(base)-1:])
    return last_adrs