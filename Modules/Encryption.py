# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# importing libraries
from random import randint

# Finding Inverse Modulo
def inverse(prime, num):
    if num<0:
        num = num + prime
    for i in range(1, prime):
        if (num * i) % prime == 1:
            return i
        # else:
            #print ("\nERROR : Inverse Modulo of 0 isn't possible. Please check the values :)")

# Function to add to points on Ellipic Curve
def Algebraic_Addition(x1, y1, x2, y2, a, prime):
    if (x1 == x2) and (y1 == y2):
        lamdba_value = (((3 * (x1 ** 2)) + a) * inverse(prime, (2 * y1))) % prime
    else:
        lamdba_value = ((y2 - y1) * inverse(prime, (x2 - x1))) % prime

    x3 = ((lamdba_value**2) - x2 - x1) % prime
    y3 = ((lamdba_value*(x1 - x3)) - y1) % prime
    return x3, y3

# Key Generation Process
def Key_Generation(Global_x,Global_y,a,prime):
    print("\n-----------------------------------------------\n")
    print("Key Generation Process starts here : \n")

    # Private Key Generation
    privateKey = randint(2, prime - 1)
    print("The Random Number Chosen (The Private Key) is: ", privateKey)

    # Public Key Generation
    x1, y1 = Global_x, Global_y
    for i in range(0, privateKey):
        x1, y1 = Algebraic_Addition(x1, y1, Global_x, Global_y, a, prime)
    PublicKey_x, PublicKey_y = x1, y1

    # Random value 'k' Generation
    k = randint(2, prime - 1)
    print("\nThe Random value k is : ", k)

    # Generating C1 value
    C1x, C1y = Global_x, Global_y
    for i in range(0, k):
        C1x, C1y = Algebraic_Addition(C1x, C1y, Global_x, Global_y, a, prime)
    print("\nThe CipherKey C1 is: (%s,%s)" %(C1x,C1y))

    # Generating C2 value
    C2x, C2y = PublicKey_x, PublicKey_y
    for i in range(0, k):
        C2x, C2y = Algebraic_Addition(C2x, C2y, PublicKey_x, PublicKey_y, a, prime)
    print("\nThe CipherKey C2 is: (%s,%s)" %(C2x,C2y))
    return C1x,C1y,C2x,C2y,privateKey

# Generating Message coordinates (Here ASCII conversion)
def Message_Generation(message,prime):
    Mx, My = ord(message) - 96, ord(message) - 96
    print ("\n-----------------------------------------------\n")
    print ("Encryption Process starts here : \n")
    print ("Message Coordinates are - (%s,%s)\n" %(Mx,My))
    return Mx,My

# Generating Cipher Text
def Generation_CipherText(x,y,x1,y1,a,prime):
    cipher_x, cipher_y = Algebraic_Addition(x, y, x1, y1, a, prime)
    print("Cipher Text is: (%s,%s)" %(cipher_x,cipher_y))
    return cipher_x, cipher_y
