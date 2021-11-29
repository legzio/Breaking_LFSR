
lfsr_keys = [0xe9, 0x45, 0xbb, 0x1c, 0x4b, 0xaf, 0xae, 0x16] 

# first byte: 0xe9 = 233
# second byte: 0x45 = 69

seed1=''
seed2=''

def generate_reg1(first3bits,lastbyte):
    string1 = str(bin(first3bits)[2:])
    len_string1 = len(string1)
    string2 = str(bin(lastbyte)[2:])
    len_string2 = len(string2)
    # print(string1,string2)
    for i in range(3):
        if i >= len_string1:
            string1 = '0' + string1
    for i in range(8):
        if i >= len_string2: 
            string2 = '0' + string2 
    # print(string1,string2)           
    reg1 = '1' + string1 + string2
    return reg1


def generate_reg2(first2bits,byte_2,byte_1):
    string0 = str(bin(first2bits)[2:])
    len_string0 = len(string0)
    string1 = str(bin(byte_2)[2:])
    len_string1 = len(string1)
    string2 = str(bin(byte_1)[2:])
    len_string2 = len(string2)
    # print(len_string1,len_string2)
    for i in range(2):
        if i >= len_string0:            
            string0 = '0' + string0
    for i in range(8):
        if i >= len_string1:            
            string1 = '0' + string1
    for i in range(8):
        if i >= len_string2:             
            string2 = '0' + string2 
    # print(string1,string2)           
    reg2 = '1' + string0 + string1 + string2
    return reg2   


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



for reg1_1byte in range(256):
    for reg2_1byte in range(256):
        key = (reg1_1byte + reg2_1byte)%255                 # UWAGA!!! zmiana na modulo 255 zamiast 256
        if key == lfsr_keys[0]:                              #233:
            # print("reg1 = ",reg1_1byte)
            # print("reg2 = ",reg2_1byte)
            for reg1_3bits in range(8):
                # print(reg1)
                for reg2_2bits in range(4):
                    for reg2_2byte in range(256):
                        reg1 = generate_reg1(reg1_3bits,reg1_1byte)
                        seed1 = reg1
                        reg2 = generate_reg2(reg2_2bits,reg2_2byte,reg2_1byte)  
                        seed2 = reg2  
                        result = sw12_byte(reg1)
                        result = sw12_byte(result[1])
                        key1 = result[0]
                        reg1 = result[1]
                        result = sw19_byte(reg2)
                        result = sw19_byte(result[1])
                        key2 = result[0]
                        reg2 = result[1]
                        key_2bytes = (int(key1,2) + int(key2,2))%255                                # UWAGA!!! zmiana na modulo 255 zamiast 256
                        # print('key1 = ', key1, 'key2 = ',key2, "key drugi bajt = ", key_2bytes)
                        if key_2bytes == lfsr_keys[1]:
                            # print('seed1 = ', seed1, 'seed2 = ',seed2, 'key_2bytes = ',hex(key_2bytes), 'lfsr_key[1] = ', hex(lfsr_keys[1]))
                            seed_id = 0
                            for i in range(2,8):
                                result = sw12_byte(reg1)
                                key1 = result[0]
                                reg1 = result[1]
                                result = sw19_byte(reg2)
                                key2 = result[0]
                                reg2 = result[1]
                                last_key = (int(key1,2) + int(key2,2))%255                                                           # UWAGA!!! zmiana na modulo 255 zamiast 256
                                # print('reg1 = ', reg1, 'key1 = ',key1, 'reg2 = ',reg2, 'key2 = ', key2, 'last_key = ',last_key)
                                if last_key == lfsr_keys[i]:
                                    seed_id = seed_id + 1
                                    # print('reg1 = ', reg1, 'key1 = ',key1, 'reg2 = ',reg2, 'key2 = ', key2, 'last_key = ',last_key)
                                    if seed_id >= 6:
                                        print('seed1 = ',seed1,'seed2 = ',seed2,'index klucza = ',i,'byte klucza = ',lfsr_keys[i])
                                        seed_id = 0
                            # print("reg1 = ",reg1)
                            # print("reg2 = ",reg2)


