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
                print(" => (%s,%s)" %(x, y))
    return Points_x, Points_y

# Generating Base Points of Elliptic Curve
def Base_Point(Points_x,Points_y,a,prime):
    print("\nThe Base Point(s) of given Elliptical Curve is :\n")
    Temp, TempArray = 0, []

    while ((Points_x.__len__()) != Temp):
        TempArray.append(Points_x[Temp])
        x1, y1 = Points_x[Temp], Points_y[Temp]

        for i in range(1, (Points_x.__len__())):
            print(" => (%s,%s)" %(x1, y1))
            x1, y1 = Algebraic_Addition(x1, y1, Points_x[Temp], Points_y[Temp], a, prime)
            TempArray.append(x1)

        if set(Points_x).intersection(set(TempArray)) != 0:
            Global_x, Global_y = Points_x[Temp], Points_y[Temp]
            print("\nSelected Base point:(%s,%s)" %(Global_x, Global_y))
            break
        else:
            Temp += 1
            del TempArray[:]

    return Global_x, Global_y
