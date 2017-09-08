# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# importing libraries
# import matplotlib.pyplot as plt
# import numpy as np
from random import randint

# Function to plot graph
def Plot_Graph(a,b):
    print("\nThe Graph for given equation is : \n")
    fig, ax = plt.subplots()

    y, x = np.ogrid[-4:4:1000j, -2:5:1000j]
    plt.contour(
        x.ravel(), y.ravel(), y**2 - x**3 - a*x -b, [0])
    plt.show()

# Generating points on Elliptic Curve
def Point_Generation(a,b,prime):
    print("\n-----------------------------------------------\n")
    print("\nFollowing points are on the Elliptical Curve : \n")
    Points_x, Points_y = [],[]
    for x in range(1, prime):
        for y in range(1, prime):
            if (y ** 2) % prime == (x**3 + (a * x) + b) % prime:
                Points_x.append(x)
                Points_y.append(y)
                print(" => (" + str(x) + "," + str(y) + ") ")
                return Points_x, Points_y

# Finding Inverse Modulo
def inverse(prime, num):
    for i in range(1, prime):
        if (num * i) % prime == 1:
            return i
        else:
            return 0

# Function to add to points on Ellipic Curve
def Algebraic_Addition(x1, y1, x2, y2, a, prime):
    if (x1 == x2) and (y1 == y2):
        lamdba_value = (((3 * (x1 ** 2)) + a) * inverse(prime, (2 * y1))% prime)
    else:
        lamdba_value = ((y2 - y1) * ((inverse(prime, (x2 - x1))) % prime))
        
    x3 = ((lamdba_value**2) - x2 - x1) % prime
    y3 = ((lamdba_value*(x1 - x3)) - y1) % prime
    return x3, y3

# Generating Base Points of Elliptic Curve
def Base_Point(Points_x,Points_y,a,prime):
    print("\nThe Base Point(s) of given Elliptical Curve is :\n")
    Temp, TempArray = 0, []
    
    while (Points_x.__len__() != Temp):
        TempArray.append(Points_x[Temp])
        x1, y1 = Points_x[Temp], Points_y[Temp]
        
        for i in range(1, Points_x.__len__()):
            print(" => (" + str(x1) + "," + str(y1) + ") ")
            x1, y1 = Algebraic_Addition(x1, y1, x1, y1, a, prime)
            TempArray.append(x1)

        if set(Points_x).intersection(set(TempArray)) != 0:
            Global_x, Global_y = Points_x[Temp], Points_y[Temp]
            print(" => (" + str(Global_x) + "," + str(Global_y) + ") ")
            return Global_x, Global_y
            break
        else:
            Temp += 1
            del TempArray[:]

# Key Generation Process
def Key_Generation(Global_x,Global_y,a,prime):
    print("\n-------------------------------------\n")
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
    print("\nThe Cipher C1 is: ")
    for i in range(0, k):
        x1, y1 = Algebraic_Addition(Global_x, Global_y, Global_x, Global_y, a, prime)
    print(" (" + str(x1) + "," + str(y1) + ") ")

    # Generating C1 value
    print("\nThe Cipher C2 is: ")
    for i in range(0, k):
        x1, y1 = Algebraic_Addition(PublicKey_x, PublicKey_y, PublicKey_x, PublicKey_y, a, prime)
    print(" (" + str(x1) + "," + str(y1) + ") ")
    return x1,y1

# Generating Message coordinates (Here ASCII conversion)
def Message_Generation(message):
    x, y = ord(message), ord(message)
    print("\n-------------------------------------\n")
    print ("Message Coordinates are - (%s,%s)\n" %(x,y))
    return x,y

# Generating Cipher Text
def Generation_CipherText(x,y,x1,y1,a,prime):
    cipher_x, cipher_y = Algebraic_Addition(x, y, x1, y1, a, prime)
    print("Cipher Text is: ")
    print(" (" + str(cipher_x) + "," + str(cipher_y) + ") \n")

###########################################################################################################
############################################## MAIN CODING ################################################
###########################################################################################################

# Printing Welcome Message
print("\tAn elliptic curve is a plane curve defined\n\tby an equation of the form (Weierstrass equation)- ")
print("\n\t\t y^2 = x^3 + a*x + b\n")

# Taking Input a,b and prime
def Input_Data():
    prime = int(input("Please Enter a prime number:  "))
    a = int(input("Please Enter the value of a:  "))
    b = int(input("Please Enter the value of b:  "))
    message = input("Please Enter the data to be send(Single letter between a-z): ")
    if (((4 * (a ** 3)) + (27 * (b ** 2))) % prime) == 0:
        print("a and b values don't satisfy basic condition.\n")
        print("Enter again: ")
        Input_Data()
    else:
        return a, b, prime, message

a, b, prime, message = Input_Data()
# Plot_Graph(a,b)
Points_x, Points_y = Point_Generation(a,b,prime)
Global_x, Global_y = Base_Point(Points_x,Points_y,a,prime)
x1,y1 = Key_Generation(Global_x,Global_y,a,prime)
x,y = Message_Generation(message)
Generation_CipherText(x,y,x1,y1,a,prime)

'''
printing statement
addition Function
'''
