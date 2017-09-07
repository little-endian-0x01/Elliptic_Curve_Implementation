# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Global Variables
Points_x, Points_y = [],[]

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
def inverse(p, num):
    for i in range(1, p):
        if (num * i) % p == 1:
            return i

# Function to add to points on Ellipic Curve
def addPoints(x1, y1, x2, y2, _a, p):
    if x1 == x2 and y1 == y2:
        lam = ((3 * (x1 ** 2) + _a) * inverse(p, 2 * y1)) % p
    else:
        lam = ((y2 - y1) * inverse(p, x2 - x1)) % p
        print(lam)
    x3 = (lam ** 2 - x2 - x1) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return x3, y3

# Generating Base Points of Elliptic Curve
def Base_Point():
    print("\nThe Base Point(s) of given Elliptical Curve is:")
    count = 0
    xTempPoints = []
    yTempPoints = []
    while Points_x.__len__() != count:
        x = Points_x[count]
        y = Points_y[count]
        xTempPoints.append(x)
        yTempPoints.append(y)
        x_new = x
        y_new = y
        for i in range(1, Points_x.__len__()):
            print(i, count)
            print(" (" + str(x_new) + "," + str(y_new) + ") ")
            x_new, y_new = addPoints(x_new, y_new, x, y, a, p)
            xTempPoints.append(x_new)
            yTempPoints.append(y_new)

        if set(Points_x).intersection(set(xTempPoints)) != 0:
            xGenerator = x
            yGenerator = y
            print(" (" + str(x) + "," + str(y) + ") ")
            break
        else:
            count += 1
            del xTempPoints[:]
            del yTempPoints[:]

# Printing Welcome Message
print("\tAn elliptic curve is a plane curve defined\n\tby an equation of the form (Weierstrass equation)- ")
print("\n\t\t y^2 = x^3 + a*x + b\n")

# Taking Input a,b and prime)
prime = int(input("Please Enter a prime number:  "))
a,b = 0,0
while (((4 * (a ** 3)) + (27 * (b ** 2))) % prime) == 0:
    a = int(input("Please Enter the value of a:  "))
    b = int(input("Please Enter the value of b: "))
    if (((4 * (a ** 3)) + (27 * (b ** 2))) % prime) == 0:
        print("a and b values don't satisfy basic condition.\n")
        print("Enter again: ")
    else:
        break

Plot_Graph(a,b)
Point_Generation(a,b,prime)
Base_Point(a,prime)

'''
choose base point
random k 2,p-1
base point * k = C1
'''
