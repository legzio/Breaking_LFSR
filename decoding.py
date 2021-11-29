import codecs


# Standard PNG image header:        0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A
# Encrypted flag.enc file header:   0x60 0x15 0xF5 0x5B 0x46 0xA5 0xB4 0x1C

seed1 = '110010111000'
seed2 = '0100101100000110001'


def sw12(reg):
    b0 = str(int(reg[1],2) ^ int(reg[6],2))
    # print(reg[1]," XOR ",reg[6]," = ",b0)
    bm = str(int(reg[11],2))
    # print(bm)
    return bm, (b0+reg[:11])

def sw12_byte(reg):
    byte1 = ''
    for i in range(8):
        r = sw12(reg)
        reg = r[1]
        byte1 = r[0]+byte1
        # print("least bit = ",r[0], "   register = ", r[1])
    return byte1,reg

def sw19(reg):
    b0 = str(int(reg[4],2) ^ int(reg[10],2))
    # print(reg[4]," XOR ",reg[10]," = ",b0)
    bm = str(int(reg[18],2))
    # print(reg, 'reg[18] =', reg[18])
    return bm, (b0+reg[:18])

def sw19_byte(reg):
    byte1 = ''
    # print(reg)
    for i in range(8):
        r = sw19(reg)
        reg = r[1]
        byte1 = r[0]+byte1
        # print("least bit = ",r[0], "register = ", r[1], 'byte =',byte1)
    return byte1,reg

def decode(reg1,reg2,encrypt):
    result = sw12_byte(reg1)
    key1 = result[0]
    reg1 = result[1]
    result = sw19_byte(reg2)
    key2 = result[0]
    reg2 = result[1]
    key = (int(key1,2) + int(key2,2))%255 
    # print('key = ',key1, 'key2 =', key2, 'key =',hex(key))
    plain = int(encrypt.hex(),16) ^ key
    # print(plain)
    # print('encrypt = ',hex(int(encrypt.hex(),16)), 'key = ',hex(key), 'plain =', hex(plain), "char = ", chr(plain))
    return reg1, reg2, plain




f1 = open("flag.enc","rb")
f2 = open("flag.png","wb")
reg1 = seed1
reg2 = seed2
znak = f1.read(1)
# for i in range(8):
while znak:
    print(znak)
    result = decode(reg1,reg2,znak)
    reg1 = result[0]
    reg2 = result[1]
    decoded_byte = result[2]
    decoded_byte = int(decoded_byte)
    print(decoded_byte)
    decoded_byte = decoded_byte.to_bytes(1,byteorder='big')
    # decoded_byte = chr(decoded_byte)
    # decoded_byte = decoded_byte.encode('utf-8')
    print(decoded_byte)
    # print(hex(decoded_byte))
    f2.write(decoded_byte)
    # decoded_byte = znak
    # print(decoded_byte)
    # decoded_byte = int(decoded_byte.hex(),16)
    # print(decoded_byte)
    # decoded_byte = hex(decoded_byte)
    # decoded_byte = chr(int(decoded_byte,16))
    # decoded_byte = decoded_byte.encode('utf-8')
    # print(decoded_byte)
    # f2.write(decoded_byte)
    znak = f1.read(1)

f1.close()
f2.close()

