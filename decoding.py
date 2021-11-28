

seed1 = '010100010010'
seed2 = '0100101100011010111'

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
    # print(bm)
    return bm, (b0+reg[:18])

def sw19_byte(reg):
    byte1 = ''
    for i in range(8):
        r = sw19(reg)
        reg = r[1]
        byte1 = r[0]+byte1
        # print("least bit = ",r[0], "   register = ", r[1])
    return byte1,reg

def decode(reg1,reg2,encrypt):
    result = sw12_byte(reg1)
    key1 = result[0]
    reg1 = result[1]
    result = sw19_byte(reg2)
    key2 = result[0]
    reg2 = result[1]
    key = (int(key1,2) + int(key2,2))%255 
    # print('encrypt = ',int(encrypt.hex(),16), 'key = ',key)
    plain = int(encrypt.hex(),16) ^ key
    # print(hex(plain))
    return reg1, reg2, hex(plain)




f1 = open("flag.enc","rb")
f2 = open("flag.png","wb")
reg1 = seed1
reg2 = seed2
znak = f1.read(1)
while znak:
    result = decode(reg1,reg2,znak)
    reg1 = result[0]
    reg2 = result[1]
    decoded_byte = result[2]
    print(decoded_byte.encode())
    f2.write(decoded_byte.encode())
    znak = f1.read(1)

f1.close()
f2.close()

   