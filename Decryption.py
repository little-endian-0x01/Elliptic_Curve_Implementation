# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git


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

# Decryption Process
def Decryption_Process(C1x,C1y,C2x,C2y,privateKey,a,prime):
    print ("\n-----------------------------------------------\n")
    print ("Decryption Process starts here : \n")
    TempX, TempY = C1x, C1y
    for i in range(0,privateKey):
        TempX,TempY = Algebraic_Addition(TempX, TempY, C1x, C1y, a, prime)
    DecryptX, DecryptY = Algebraic_Addition(TempX, (TempY*(-1) + prime), C2x, C2y, a, prime)
    print("The Decrypted Message is: %s" %(chr(DecryptX+96)))
