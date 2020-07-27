from common import *
def lh(host,base):
    last_adrs=lastbitchanger(binstr=binarymaker(base),bits=bitsCounter(host))

    return todecimal(last_adrs)