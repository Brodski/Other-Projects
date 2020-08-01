from ast import literal_eval

// $ python artLogicPart2.py
// Then follow obvious dialouge

kByteSize = 4

def reverseBits(n):
        result = 0
        for i in range(8*kByteSize): 
            result = result << 1
            result = result | n & 1
            n >>= 1
        return result

def convertToString(fewBytes):
    word = ''
    for x in fewBytes:
        if x == 0:
            continue
        word += bytes.fromhex(hex(x)[2:]).decode('ASCII')
    return word

def encryptFewBytes(msg):
    encryptedMsg = 1
    originalBytes = [ord(c) for c in msg]
    while len(originalBytes) < kByteSize:
        originalBytes.append(0)
    
    for x in range(8*kByteSize): # 8 bits per letter, and 4 letters being encrypted each time
        leastSigBit = originalBytes[x % kByteSize] & 1
        encryptedMsg = (encryptedMsg << 1) | leastSigBit
        originalBytes[x % kByteSize] = originalBytes[x % kByteSize] >> 1
    return reverseBits(encryptedMsg)


def decryptFewBytes(encryptedMsg):
    encryptedMsg = reverseBits(encryptedMsg)
    orignalBits = [0] * kByteSize
    for x in range(8*kByteSize):
        leastSigBit = encryptedMsg & 1
        orignalBits[x % kByteSize] = orignalBits[x % kByteSize] << 1 | leastSigBit
        encryptedMsg = encryptedMsg >> 1

    return reversed(orignalBits)

def encode(msg):
    i = 0
    wholeMsg = []
    while msg[i:i+kByteSize]:
        wholeMsg.append(encryptFewBytes(msg[i:i+kByteSize] ))
        i = i + kByteSize
    return wholeMsg


def decode(msg):
    wholeMsg = ""
    for encryptedBytes in msg:
        decryptedBytes = decryptFewBytes(encryptedBytes)
        wholeMsg += convertToString(decryptedBytes)
    return wholeMsg


if __name__ == '__main__':
    choose = input("\nEnter 1 to encrypt a message.\nEnter 2 to decrypt an encrypted message: \n---> ").strip()
    message = input("Enter the message:  \n---> ")
    if choose == "1":
        processed_msg = encode(message)
    elif choose == "2":
        message = literal_eval(message.strip())
        processed_msg = decode(message)
    else:
        print("Neither 1 or 2 entered. Exiting")
        exit(0)
    print ("\nFinished:")
    print (processed_msg)
