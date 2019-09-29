

FIXED_IP = [2, 6, 3, 1, 4, 8, 5, 7]
FIXED_EP = [4, 1, 2, 3, 2, 3, 4, 1]
FIXED_IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
FIXED_P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
FIXED_P8 = [6, 3, 7, 4, 8, 5, 10, 9]
FIXED_P4 = [2, 4, 3, 1]

cipher = [0b11000001,0b1101010,0b10100,0b11111,0b10100100,0b10100,0b11111,0b1001111,0b10100,0b1010001,0b1001111,0b11001010,0b10011010,0b11111,0b11111,0b10011010,0b10111111,0b10100,0b1001111,0b11001010,0b10011010,0b11111,0b10100100,0b10100,0b1101010,0b10011010,0b1001111,0b10100,0b10011010,0b10011010,0b11000001,0b10100,0b1101010,0b11000001,0b11111,0b10100100,0b10100100,0b10100,0b11000001,0b10111111,0b11001010,0b11000001,0b1001111,0b10100100,0b11001010,0b10111111,0b11001010,0b1001111,0b11000001,0b10011010,0b10100100,0b10100,0b11001010,0b11001010,0b10111111,0b1001111,0b1001111,0b11111,0b11111,0b1001111,0b11000001,0b10011010,0b1001111,0b10100100,0b1101010,0b11111,0b11001010,0b11000001,0b1010001,0b10100100,0b10011010,0b11111,0b1010001,0b1010001,0b10100,0b10011010]
cipher2 = []

stu_id = '590610630'.encode('utf8')



cipher_test = '10100010'
# KEY = '0111111101'
paintext = '11101010'


S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]




def permutate(original, fixed_key):
    new = ''
    for i in fixed_key:
        new += original[i - 1]
    return new


def left_half(bits):
    return bits[:len(bits)//2]


def right_half(bits):
    return bits[len(bits)//2:]


def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half


def key1(K):
    return permutate(shift(permutate(K, FIXED_P10)), FIXED_P8)


def key2(K):
    return permutate(shift(shift(shift(permutate(K, FIXED_P10)))), FIXED_P8)


def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new


def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])


def f_k(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, FIXED_EP)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)
    bits = permutate(bits, FIXED_P4)
    return xor(bits, L)


def encrypt(plain_text,K):
    bits = permutate(plain_text, FIXED_IP)
    temp = f_k(bits, key1(K))
    bits = right_half(bits) + temp
    bits = f_k(bits, key2(K))
    return permutate(bits + temp, FIXED_IP_INVERSE)


def decrypt(cipher_text,K):
    bits = permutate(cipher_text, FIXED_IP)
    temp = f_k(bits, key2(K))
    bits = right_half(bits) + temp
    bits = f_k(bits, key1(K))
    return permutate(bits + temp, FIXED_IP_INVERSE)

for i in range (len(cipher)) :
    s = str("{0:08b}".format(cipher[i]))
    cipher2.append(s)
    

for i in range(1024):
    few = []
    count = 0
    k = str("{0:010b}".format(i))
    num = 0
    print("KEY ->>"+str(k))
    for jay in range (len(cipher2)):
        
        c = str(cipher2[jay])
        # print("Cypher : " + c)
        # print("Key : " + k)
        
        pain = int(decrypt(c,k),2)
        if jay <= 8:
            
            if (pain == int(stu_id[jay])):
                few.append(pain-48)
                count = count + 1  
            else:
                 break
        else:
            few.append(pain-48)
    if count >= len(stu_id):
        break

    # print('++++++++++++++++++++++++++++++++++++++++++++++++++')

print(few)
few.clear

# decrypt('10100010', '0111111101')




# print(cipher3[0])
# print(stu_id[0])




    



# encrypt('11101010',K)

# encrypt('11101010')
# decrypt('10100010')