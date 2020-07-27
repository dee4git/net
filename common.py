import math
def todecimal(binary):
    dec=""
    adrs=[]
    chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    for i in chunks:
        dec+=str(int(i,2))+"."
    for j in chunks:
        adrs.append(str(int(j,2))+".")

    adrs.pop()
    dec = dec[:len(dec) - 1:]
    return dec

def bitsCounter(num):
    temp = math.ceil(math.log2(num))
    if pow(2, temp) - 2 >= num:
        return temp
    return temp + 1

def lastbitchanger(binstr, bits):
    s = ""
    rbin = binstr[::-1]
    for i in range(bits):
        s += "1"
    newbin = s + rbin[bits::]
    finalbin = newbin[::-1]
    return finalbin

def binarymaker(str):
    split = str.split(".")
    s = ""
    for i in split:
        s += (format(int(i), '08b'))
    return s