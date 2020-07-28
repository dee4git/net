from common import *
def adrs(sub,base):
    sub=bitsCounter(sub)
    sub=32-sub
    return (str(base)+"/"+str(sub))