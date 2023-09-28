#The functions for FinLit
import pandas as pd
import math as mt
import matplotlib.pyplot as plt

#=  , +

#The functions used
def Pa():
    while True:
        try:
            pa = float(input("What is the given principal amount: "))
            if pa <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break

        except ValueError:
            print("Please insert the number only,e.g 500")
            continue
    return pa

def Ac():
    while True:
        try:
            ac = float(input("What is the given accumulated amount: "))
            if ac <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break
        except ValueError:
            print("Please insert the number only,e.g 500")
            continue
    return ac

def Ir():
    while True:
        try:
            ir = float(input("What is the given interest rate: "))/100
            if ir <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break
        except ValueError:
            print("Please insert the number only,e.g 12.5")
            continue
    return ir

def N():
    while True:
        try:
            N = int(input("What is the given number of the investment years: "))
            if N <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break
            
        except ValueError:
            print("Please insert the number only,e.g 5")
            continue
    return N

def In():
    opt = {"Yearly intervals":["Annually","Semi-annually","Quarterly","Every-two years","Monthly"],"Code":[1,2,4,6,12]}
    df = pd.DataFrame(opt,index=range(1,(len(opt["Code"]))+1))
    print(df)
    while True:
        try:
            Int = int(input("From the above table, select a code: "))
            if Int in opt["Code"]:
                break
            else:
                print("Incorrect value, e.g 12 for monthly intervals")
                continue
        except ValueError:
            print("Incorrect value, e.g 12 for monthly intervals")
            continue
    return Int

def loan():
    while True:
        try:
            loan = float(input("What is the given size of the loan: "))
            if loan <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break

        except ValueError:
            print("Please insert the number only,e.g 500")
            continue
    return loan


class AA:
    def CI(Pa,Ir,In,N):
        A = Pa*mt.pow((1+Ir/In),N*In)
        print(f"The accumulated amount is R{round(A,2)}")
        RRR = (round(A,2) - Pa)/Pa * 100
        print(f"The required rate of return is {round(RRR,2)}%")
    
    def RB(Pa,Ir,In,N):
        A = Pa*mt.pow((1-Ir/In),N*In)
        print(f"The accumulated amount is R{round(A,2)}")
    
    def SI(Pa,Ir,N):
        A = Pa*(1+Ir*N)
        print(f"The accumulated amount is R{round(A,2)}")
        RRR = (round(A,2) - Pa)/Pa * 100
        print(f"The required rate of return is {round(RRR,2)}%")
        
        g = input("Graph: ")
        if g == "yes":
            graph(Pa,Ir,N)
            
    def SD(Pa,Ir,N):
        A = Pa*(1-Ir*N)
        print(f"The accumulated amount is R{round(A,2)}")

class Num:
    def CI(Ac,Pa,Ir,In):
        N = mt.log((Ac/Pa))/mt.log((1+Ir/In))
        num = N/In
        print(f"It will take {round(num,2)} years")

    def RB(Ac,Pa,Ir,In):
        N = mt.log((Ac/Pa))/mt.log((1-Ir/In))
        num = N/In
        print(f"It will take {round(num,2)} years")

    def SI(Ac,Pa,Ir):
        num = (Ac/Pa-1)/Ir
        print(f"It will take {round(num,2)} years")

    def SD(Ac,Pa,Ir):
        num = (Ac/Pa-1)/(Ir*-1)
        print(f"It will take {round(num,2)} years")

def PV(loan,Ir,In,N):
    X_nom = loan*(Ir/In)
    X_dem = 1-mt.pow(1+Ir/In,-1*(N*In))
    X = X_nom/X_dem
    print(round(X,2))
        
def graph(Pa,Ir,N):
    Amount=[Pa]
    years=[0]
    check = 1
    while check != (N+1):
        years.append(check)
        A = Pa*(1+Ir*check)
        Amount.append(round(A,2))
        check+=1
        
    print(years)
    print(Amount)
    
    plt.plot(years,Amount)
    plt.show()
    


