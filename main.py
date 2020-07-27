#find bits req
#network address, hostnet mask, first host, last host, broadcast address
from subnet import subnetMask
from net import adrs
from first_host import  fh as fhh
from last_host import lh as lhh
from bc import bcad as bcadrs

host=1200
base="172.12.0.0"


def mainFun(host,base):
    net_adrs= adrs(base)
    hostnet= subnetMask(host)
    fh= fhh(host)
    lh= lhh(host,base)
    ba=bcadrs(host)
    print("Network Address: ",net_adrs)
    print("Subnet Mask: ",hostnet)
    print("First Host: ",fh)
    print("Last host: ",lh)
    print("Boradcast Address: ",ba)


mainFun(host,base)