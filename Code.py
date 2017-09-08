# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# importing libraries
import matplotlib.pyplot as plt
import numpy as np
from random import randint

# Global Variables
Points_x, Points_y = [],[]
xGenerator, yGenerator = 0,0

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
    print("Following points are on the Elliptical Curve : \n")
    for x in range(1, prime):
        for y in range(1, prime):
            if (y ** 2) % prime == (x**3 + (a * x) + b) % prime:
                Points_x.append(x)
                Points_y.append(y)
                print(" => (" + str(x) + "," + str(y) + ") ")

# Finding Inverse Modulo
def inverse(prime, num):
    for i in range(1, prime):
        if (num * i) % prime == 1:
            return i

# Function to add to points on Ellipic Curve
def Algebraic_Addition(x1, y1, x2, y2, a, prime):
    if x1 == x2 and y1 == y2:
        lamdba_value = ((3 * (x1 ** 2) + a) * inverse(prime, 2 * y1)) % prime
    else:
        lamdba_value = ((y2 - y1) * inverse(prime, x2 - x1)) % prime
    x3 = (lamdba_value ** 2 - x2 - x1) % prime
    y3 = (lamdba_value * (x1 - x3) - y1) % prime
    return x3, y3

# Generating Base Points of Elliptic Curve
def Base_Point(a,prime):
    print("\nThe Base Point(s) of given Elliptical Curve is :\n")
    Temp, TempArray = 0, []
    while (Points_x.__len__() != Temp):
        TempArray.append(Points_x[Temp])
        x1, y1 = Points_x[Temp], Points_y[Temp]
        for i in range(1, Points_x.__len__()):
            print(i, Temp)
            print(" (" + str(x1) + "," + str(y1) + ") ")
            x1, y1 = Algebraic_Addition(x1, y1, x1, y1, a, prime)
            TempArray.append(x1)

        if set(Points_x).intersection(set(TempArray)) != 0:
            xGenerator, yGenerator = x, y
            print(" => (" + str(x) + "," + str(y) + ") ")
            break
        else:
            Temp += 1
            del TempArray[:]

# Key Generation Process
def Key_Generation(a,prime):
    print("\nKey Generation Process starts here : \n\n")

    # Private Key Generation
    privateKey = randint(2, p - 1)
    print("\nThe Random Number Chosen(The Private Key) is %d. ", privateKey)

    # Public Key Generation
    x1, y1 = xGenerator, yGenerator
    for i in range(0, privateKey):
        x1, y1 = addPoints(x1, y1, x1, y1, a, prime)
    PublicKey_x, PublicKey_y = x1, y1

    # Random value 'k' Generation
    k = randint(2, p - 1)
    print("\nThe Random value k is %s ", k)

    # Generating C1 value
    print("The Cipher C1 is: ")
    x = xGenerator
    y = yGenerator
    x1 = x
    y1 = y
    for i in range(0, k):
        x1, y1 = addPoints(x1, y1, x, y, a, p)
    xCipher1 = x1
    yCipher1 = y1
    print(" (" + str(xCipher1) + "," + str(yCipher1) + ") ")

    # Generating C1 value
    print("The Cipher C2 is: ")
    x = PublicKey_x
    y = PublicKey_y
    x1 = x
    y1 = y
    for i in range(0, k):
        x1, y1 = addPoints(x1, y1, x, y, a, p)
    xPb = x1
    yPb = y1

    xCipher2, yCipher2 = addPoints(xPm, yPm, xPb, yPb, a, p)
    print(" (" + str(xCipher2) + "," + str(yCipher2) + ") ")

# Printing Welcome Message
print("\tAn elliptic curve is a plane curve defined\n\tby an equation of the form (Weierstrass equation)- ")
print("\n\t\t y^2 = x^3 + a*x + b\n")

# Taking Input a,b and prime
def Input_Data():
    prime = int(input("Please Enter a prime number:  "))
    a,b = 0,0
    a = int(input("Please Enter the value of a:  "))
    b = int(input("Please Enter the value of b: "))
    if (((4 * (a ** 3)) + (27 * (b ** 2))) % prime) == 0:
        print("a and b values don't satisfy basic condition.\n")
        print("Enter again: ")
        Input_Data()
    else:
        return a,b,prime

a, b, prime = Input_Data()
Plot_Graph(a,b)
Point_Generation(a,b,prime)
Base_Point(a,prime)
Key_Generation(a,prime)
