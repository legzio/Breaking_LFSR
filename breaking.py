
# Register reg1 is 12 bits register. It means that i will be integer 0 - 4095
#  bits 

reg1 = '100110100110'
reg2 = '1001011010110001011'


def sw12(reg):
    b0 = str(int(reg[1],2) ^ int(reg[6],2))
    print(reg[1]," XOR ",reg[6]," = ",b0)
    bm = str(int(reg[11],2))
    # print(bm)
    return bm, (b0+reg[:11])

def sw12_byte(reg):
    byte1 = ''
    for i in range(8):
        r = sw12(reg)
        reg = r[1]
        byte1 = r[0]+byte1
        print("least bit = ",r[0], "   register = ", r[1])
    return byte1,reg

def sw19(reg):
    b0 = str(int(reg[4],2) ^ int(reg[10],2))
    print(reg[4]," XOR ",reg[10]," = ",b0)
    bm = str(int(reg[18],2))
    # print(bm)
    return bm, (b0+reg[:18])

def sw19_byte(reg):
    byte1 = ''
    for i in range(8):
        r = sw19(reg)
        reg = r[1]
        byte1 = r[0]+byte1
        print("least bit = ",r[0], "   register = ", r[1])
    return byte1,reg


result = sw12_byte(reg1)

print("key byte = ", result[0], "register = ", result[1])

result = sw19_byte(reg2)

print("key byte = ", result[0], "register = ", result[1])





