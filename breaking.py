
# Register reg1 is 12 bits register. It means that i will be integer 0 - 4095
#  bits 

reg1 = '100110100110'
reg2 = '1001011010110001011'

# Standard PNG image header:        0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A
# Encrypted flag.enc file header:   0x60 0x15 0xF5 0x5B 0x46 0xA5 0xB4 0x1C

plain_png = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
encrypt_png = [0x60, 0x15, 0xF5, 0x5B, 0x46, 0xA5, 0xB4, 0x1C]

lfsr_keys = [0xe9, 0x45, 0xbb, 0x1c, 0x4b, 0xaf, 0xae, 0x16] 


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


# this lines make XOR bytes from plain and encrypted header:
# for i in range(8):
    # print(bin(plain_png[i]))
    # print(bin(encrypt_png[i]))
    # print(hex(plain_png[i] ^ encrypt_png[i]),", ")

# result was: [0xe9, 0x45, 0xbb, 0x1c, 0x4b, 0xaf, 0xae, 0x16] 

# result = sw12_byte(reg1)

# print("key byte = ", result[0], "register = ", result[1])

# result = sw19_byte(reg2)

# print("key byte = ", result[0], "register = ", result[1])

print(reg1, reg2)
result = sw12_byte(reg1)
key1 = result[0]
reg1 = result[1]
result = sw19_byte(reg2)
key2 = result[0]
reg2 = result[1]
key = (int(key1,2) + int(key2,2))%256
print(key1, int(key1,2))
print(key2, int(key2,2))
print(key)
print(reg1, reg2)
result = sw12_byte(reg1)
key1 = result[0]
reg1 = result[1]
result = sw19_byte(reg2)
key2 = result[0]
reg2 = result[1]
key = (int(key1,2) + int(key2,2))%256
print(key1, int(key1,2))
print(key2, int(key2,2))
print(key)
print(reg1, reg2)






