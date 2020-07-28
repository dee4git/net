#find bits req
#network address, hostnet mask, first host, last host, broadcast address
from subnet import subnetMask
from net import adrs
from first_host import  fh as fhh
from last_host import lh as lhh
from bc import bcad as bcadrs

host=63
base="192.168.54.0"


def mainFun(host,base):
    net_adrs= adrs(host,base)
    subnet= subnetMask(host)
    lh= lhh(host,base)
    print("Network Address: ",net_adrs)
    print("Subnet Mask: ",subnet)
    print("Broadcast Address: ",lh)


mainFun(host,base)