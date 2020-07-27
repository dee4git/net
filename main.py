#find bits req
#network address, subnet mask, first host, last host, broadcast address
from subnet import subnetMask
from net import adrs
from first_host import  fh as fhh
from last_host import lh as lhh
from bc import bcad as bcadrs

sub=1200
base="172.12.0.0"


def mainFun(sub,base):
    net_adrs= adrs(base)
    subnet= subnetMask(sub)
    fh= fhh(sub)
    lh= lhh(sub)
    ba=bcadrs(sub)
    print("Network Address: ",net_adrs)
    print("Subnet Mask: ",subnet)
    print("First Host: ",fh)
    print("Last host: ",lh)
    print("Boradcast Address: ",ba)


mainFun(sub,base)