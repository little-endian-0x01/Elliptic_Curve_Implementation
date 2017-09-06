# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math

def input_data():
    print("\tAn elliptic curve is a plane curve defined\n\tby an equation of the form (Weierstrass equation)- ")
    print("\n\t\t y^2 = x^3 + a*x + b\n")
    a = int(input("Please Enter the value of a: "))
    b = int(input("Please Enter the value of b: "))
    plot_graph(a,b)

def plot_graph(a,b):
    print("\nThe Graph for given equation is : ")
    fig, ax = plt.subplots()

    y, x = np.ogrid[-4:4:1000j, -2:5:1000j]
    plt.contour(
        x.ravel(), y.ravel(), y**2 - x**3 - a*x -b, [0])
    plt.show()

input_data()
