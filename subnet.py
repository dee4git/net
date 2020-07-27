from common import todecimal, bitsCounter


def subnetMask(sub):
    bits = bitsCounter(sub)
    basic = "11111111111111111111111111111111"
    s = ""
    rbin = basic[::-1]
    for i in range(bits):
        s += "0"
    newbin = s + rbin[bits::]
    finalbin = newbin[::-1]
    final = todecimal(finalbin)
    return final
