
# lfsr_keys = [0xe9, 0x45, 0xbb, 0x1c, 0x4b, 0xaf, 0xae, 0x16] 

# first byte: 0xe9 = 233

for reg1 in range(256):
    for reg2 in range(256):
        key = (reg1 + reg2)%256
        if key == 233:
            print("reg1 = ",reg1)
            print("reg2 = ",reg2)


