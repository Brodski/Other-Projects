from ast import literal_eval

kByteSize = 4


def reverse_Bits(n):
        result = 0
        for i in range(4*8):
            result = result << 1
            result = result | n & 1
            n >>= 1
        return result

def bitstring_to_bytes(s):
    v = s
    b = bytearray()
    while v:
        # print (bin(v))
        # print (bin(v & 0xff))
        b.append(v & 0xff)
        v = v >> 8
    # print (b)
    return bytes(b[::-1])

def encrypt_it(msg):
    originalBytes = [ord(c) for c in msg]
    while len(originalBytes) < 4:
        originalBytes.append(0)
    enc = 1
    print ("Orignal bytes:")
    for x in originalBytes:
        print (x, "  - ", bin(x).lstrip('0b'))

    # print ("---------------------------------")
    # for x in range(8*len(originalBytes)):
    # 8 bits per letter, and 4 letters being encrypted each time
    for x in range(32):
        lastBit = originalBytes[x % 4] & 1
        enc = (enc << 1) | lastBit

        print ("====",x,x%4,"====")
        print(lastBit, "         ", bin(enc), "      ", bin(originalBytes[x % 4]))

        originalBytes[x % 4] = originalBytes[x % 4] >> 1

    # print ("---------------------------------")
    # print (bin(enc))
    print("--------bang bang--------------------")

    xx= reverse_Bits(enc)
    print (xx)
    print(bin(xx).lstrip('0b'))
    hex_string = hex(xx)[2:]
    hex_string = hex_string.zfill(8)

    # print (hex_string)
    # string_b = bytes.fromhex(hex_string).decode('ASCII')
    # print (string_b)
    return xx


def decrypt_it(enc):
    print ("---TOP OF IT---")
    print(enc)
    print ("before rev", bin(enc).lstrip('0b'))
    enc = reverse_Bits(enc)

    print ("after rev", bin(enc).lstrip('0b'))

    orignalBits = [0] * 4
    for x in range(32):
        lastBit = enc & 1
        orignalBits[x % 4] = orignalBits[x % 4] << 1 | lastBit
        enc = enc >> 1
        lol = [bin(x).lstrip('0b') for x in orignalBits]
        print (lastBit, "-->", x%4, "%35s" % bin(enc), " - ", lol)
        # orignalBits = orignalBits << 1 | lastBit
        # print (lastBit, "%35s" % bin(enc), " - ", bin(orignalBits), len(bin(orignalBits)))

    print ("=-=-=-=-=-=-")
    finalString = ''
    print ("len(orignalBits)", len(orignalBits))
    for x in reversed(orignalBits):
        if x == 0: continue
        print ("x",x)
        hex_string = hex(x)[2:]
        print ("hex_string", hex_string)
        string_b = bytes.fromhex(hex_string).decode('ASCII')
        print(string_b)
        finalString += string_b
    print ("COMPELTE!")
    print (finalString)

    # enc = 1
    # originalBytes = []
    # for x in range(32):
    #     originalBytes[x % 4] = originalBytes[x % 4] >> 1
    #     enc = (enc << 1) | lastBit
    #     lastBit = mByte[x % 4] & 1
    #
    #
    # while len(originalBytes) < 4:
    #     originalBytes.append(0)
    #
    # originalBytes = [ord(c) for c in msg]

    return  finalString

def encrypt_msg(msg):
    i = 0
    wholeMsg = []
    while msg[i:i+4]:
        print (msg[i:i+4])
        poo = encrypt_it( msg[i:i+4] )
        wholeMsg.append(poo)
        i = i + 4
    print (wholeMsg)
    return wholeMsg
def decrypt_msg(msg):
    wholeMsg = []
    for encrypted_byte in msg:
        # print (encrypted_byte)
        poo = decrypt_it( encrypted_byte )
        wholeMsg.append(poo)
    return ''.join(wholeMsg)

if __name__ == '__main__':
    # print ("\n==============\n")
    # x = encode("go hang a salami, I'm a lasagna hog")
    # print ("->", x)
    # print("\n==============\n")
    # y = decode(x)
    # print ("->", y)
    choose = input("\nEnter 1 to encrypt a message.\nEnter 2 to decrypt an encrypted message: \n---> ").strip()
    message = input("Enter the message:  \n---> ")
    if choose == "1":
        processed_msg = encrypt_msg(message)
    elif choose == "2":
        message = literal_eval(message.strip())
        print(message)
        processed_msg = decrypt_msg(message)
    else:
        print("Neither 1 or 2 entered. Exiting")
        exit(0)
    print ("\nFinished:")
    print (processed_msg)
