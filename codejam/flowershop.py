import os
import math
os.system('cls')
os.system('')
os.system('color a')
os.system('title Quadratic Equation Solver')
#This is used for presentation of the function for WINDOWS cmd
#------------------------------------------------
def QuadSolve():
    os.system('cls')
    print("         Quadratic Equation Solver 1")
    print("")
    print(" X = (-b +/- sqrtb^2 + sqrt4ac)/div/2a ")
    print("")
    print("    Quadratic equation: ax^2 + bx + c")
    print("")
    print("")
    print("")
    a = int(input(" What is the value of a? ---> "))
    b = int(input(" What is the value of b? ---> "))
    c = int(input(" What is the value of c? ---> "))
    firstsec = -1 * b #first second and third "sectors" of the expression
    secsec = math.sqrt(b ** 2 - 4 * a * c)
    thirdsec = 2 * a
    Plussl = firstsec + secsec #Pluss1 is where -b and root b^2 + 4ac are added to give a value of X
    X = Plussl / thirdsec
    Negsl = firstsec - secsec #Same purpose as Plussl but subtraction is used instead to give the other solution of X
    X2 = Negsl / thirdsec
    print("")1
    print("         X=%d  OR  X=%d ") % (X, X2)
    os.system('pause >nul')
    QuadSolve()

QuadSolve()