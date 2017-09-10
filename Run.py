# Author - Shivam Kapoor
# This code is written as minimal as possible.
# Github - https://github.com/ConanKapoor/Elliptic_Curve_Implementation.git

# importing libraries
from pyfiglet import Figlet
from Modules.Input import *
from Modules.GraphPlotting import *
from Modules.Points_Generation import *
from Modules.Encryption import *
from Modules.Decryption import *
import os, time

# Banner for the program
def Banner():
    banner = Figlet(font='slant')
    print (banner.renderText('Elliptic Curve'))
    print ("<---------WELCOME TO ELLIPTIC CURVE PROGRAM--------->")
    print ("<---------v1.0 - Author - Conan Kapoor--------->")
    print ("\n")

# Menu given to users. Eat away!
def Menu():
    print ("Please Select the mode of operation:- \n")
    print ("----> 1) Give Input.")
    print ("----> 2) Plot the graph.")
    print ("----> 3) Generate all points on curve and show Base Point(s).")
    print ("----> 4) Generate Keys and Encrypt Data")
    print ("----> 5) Decrypt Data")
    print ("----> 6) Exit the program :[.\n")

if __name__ == '__main__':
    die =1
    try:
        while(die):
            os.system("clear")
            Banner()
            Menu()
            choice = int(input("Enter your choice: "))
            print("\n")

            if choice == 1:
                a, b, prime, message = Input_Data()
            elif choice == 2:
                Plot_Graph(a,b)
            elif choice == 3:
                Points_x, Points_y = Point_Generation(a,b,prime)
                Global_x, Global_y = Base_Point(Points_x,Points_y,a,prime)
                time.sleep(5)
            elif choice == 4:
                C1x,C1y,C2x,C2y,privateKey = Key_Generation(Global_x,Global_y,a,prime)
                Mx,My = Message_Generation(message,prime)
                cipher_x, cipher_y = Generation_CipherText(Mx,My,C2x,C2y,a,prime)
                time.sleep(5)
            elif choice == 5:
                Decryption_Process(C1x,C1y,cipher_x, cipher_y,privateKey,a,prime)
                time.sleep(5)
            else:
                die = 0
                quit()

    except KeyboardInterrupt:
        print("\n\nInterrupt received! Exiting cleanly...\n")
