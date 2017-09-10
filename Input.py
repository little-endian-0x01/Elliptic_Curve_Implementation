# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# Taking Input a,b and prime and message
def Input_Data():
    # Printing Welcome Message
    print("\tAn elliptic curve is a plane curve defined\n\tby an equation of the form (Weierstrass equation)- ")
    print("\n\t\t y^2 = x^3 + a*x + b\n")

    prime = int(input("Please Enter a prime number:  "))
    a = int(input("Please Enter the value of a:  "))
    b = int(input("Please Enter the value of b:  "))
    message = input("Please Enter the data to be send(Single letter between a-z): ")
    if (((4 * (a ** 3)) + (27 * (b ** 2))) % prime) == 0:
        print("\nERROR : a and b values don't satisfy basic condition.")
        print("Enter again: \n")
        Input_Data()
    else:
        return a, b, prime, message
