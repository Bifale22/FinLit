import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import sys
import math as mt

Income = {"Income":[],"Amount":[]}
Expense = {"Expense":[],"Cost":[]}
Totals = {"Total Income":0,"Total Expense":0} 

#THE FUNCTIONS FOR BUDGET
def add_in():
    counter = 0
    #Making sure that it's an integar
    while True:
        try:
            income = int(input("How many sources of income do you have?: "))
            if income <= 0:
                print("Insert a positive number")
                continue
            else:
                break
            
        except ValueError:
            print("Please insert a number")
            continue
    
    #Loop according to the slot of the size of the income streams
    while counter != income:
        #Making sure that the input is an alphabet
        while True:
            title = input("Name of source: ").capitalize()
            if title.isalpha():
                Income["Income"].append(title)
                break
            else:
                continue
        #making sure that the input is a float
        while True:
            try:
                amount = float(input("Amount: "))
                if amount <= 0:
                    print("Insert a positve number!!")
                    continue
                else:
                    Income["Amount"].append(amount)
                    break
            except ValueError:
                print("Insert a number, e.g 500")
                continue
        counter+=1
        
    global Totals
    temp = 0
    for amount in Income["Amount"]:
         temp +=amount
         
    Totals["Total Income"] = temp
    print("\n")
    print("Your total income is R",temp)
    print("\n")
    data = pd.DataFrame(Income,index=range(1,(len(Income["Income"])+1)))
    print(data)

def add_ex():
    counter = 0
    while True:
        try:
            expense = int(input("How many expenses do you have?: "))
            if expense <= 0:
                print("Insert a postive number!!")
                continue
            else:
                break
            
        except ValueError:
            print("Please insert a number")
            continue

    while counter != expense:
        while True:
            title = input("Name of expense: ").capitalize()
            if title.isalpha():
                Expense["Expense"].append(title)
                break
            else:
                continue

        while True:
            try:    
                cost = float(input("Amount: "))
                if cost <= 0:
                    print("Insert a positive number!")
                    continue
                else:
                    Expense["Cost"].append(cost)
                    break
            except ValueError:
                continue
        counter+=1
    
    global Totals
    temp = 0
    for amount in Expense["Cost"]:
         temp +=amount
         
    Totals["Total Expense"] = temp
    print("\n")
    print("Your total expense is R",temp)
    #Saving it into a table
    data = pd.DataFrame(Expense,index=range(1,(len(Expense["Expense"])+1)))
    print("\n")
    print(data)

def view():
    data = ["Income","Expense","Overall"]
    index = ["1","2","3"]
    print("\n")
    print("Available options")
    option = pd.Series(data,index=index)
    print(option)

    while True:
            choice = input("Choose from the above options e.g Expense : ").capitalize()
            if choice.isalpha() and choice in data:
                break
            else:
                print("\n")
                print("The chosen option is not available!")
                print("Please select from the options above e.g Income")
                continue
    global Income
    global Expense
    if choice == "Income":
        if len(Income["Income"]) == 0:
            print("There's no data, Create a budget for income!")
            return 0
        choice = pd.DataFrame(Income,index=range(1,(len(Income["Income"])+1)))
        print(choice)
        #Gadgets for the piechart
        explode = []
        counter = 0
        while counter!=len(Income["Income"]):
            explode.append(0.05)
            counter+=1
        if len(Income["Income"]) <= 6:
            diagram = input("Do you want to see a diagram?: ").lower()
            if "yes" in diagram:
                fig,ax = plt.subplots()
                ax.pie(Income["Amount"],labels=Income["Income"],wedgeprops={"edgecolor":"black"},shadow=True,startangle=90,explode=explode, autopct = '%1.1f%%')
                ax.set_title("Contribution percentage portion of your income")
                fig.legend(loc="lower right")
                plt.tight_layout()
                plt.show()
        else:
            return 0
        
    elif choice == "Expense":
        if len(Expense["Expense"]) == 0:
            print("There's no data, Create a budget for expense!")
            return 0
        choice = pd.DataFrame(Expense,index=range(1,(len(Expense["Expense"])+1)))
        print(choice)
        #Gadgets for the piechart
        explode = []
        counter = 0
        while counter!=len(Expense["Expense"]):
            explode.append(0.05)
            counter+=1
        if len(Expense["Expense"]) <= 6:
            diagram = input("Do you want to see a diagram?: ").lower()
            if "yes" in diagram:
                fig,ax = plt.subplots()
                ax.pie(Expense["Cost"],labels=Expense["Expense"],wedgeprops={"edgecolor":"black"},shadow=True,startangle=90,explode=explode, autopct = '%1.1f%%')
                ax.set_title("Contribution percentage portion of your expense")
                fig.legend(loc="lower right")
                plt.tight_layout()
                plt.show()
            else:
                return 0      
    else:
        if (len(Income["Income"]) == 0) or (len(Expense["Expense"]) == 0):
            print("There's no data for both income and expense, Create a budget for both your income and expenses!")
            
        else:
            choice = pd.DataFrame(Income,index=range(1,(len(Income["Income"])+1)))
            choice1 = pd.DataFrame(Expense,index=range(1,(len(Expense["Expense"])+1)))
            print("\n")
            print(choice)
            print("\n")
            print(choice1)
            
            global Totals
            
            print("\n") #Lastest change
            print("Your total income is: R",Totals["Total Income"])
            print("Your total expense is: R",Totals["Total Expense"])
            print("\n")
            if Totals["Total Income"] > Totals["Total Expense"]:
                print("Your Net profit is: R",Totals["Total Income"]-Totals["Total Expense"])
                print("\n")
                print("On the right track")
                print("""Try to keep your: needs at 50%
                  wants at 30%
                  savings at 20%
                                           
REMEMBER: That budgeting is a continous process""")
            else:
                print("Your Net loss is: R",Totals["Total Expense"]-Totals["Total Income"])
                print("\n")
                print("You need to work on your budget!")
                print("Try reducing your expenses or the number of your income streams")
            
            diagram = input("Do you want to see a diagram?: ").lower()
            if "yes" in diagram and len(Expense["Expense"]) <= 6:
                slices = []
                labels = []
                explode = []
                
                counter = 0
                while counter != len(Expense["Expense"]):
                    labels.append(Expense["Expense"][counter])
                    slices.append(Expense["Cost"][counter])
                    explode.append(0.05)
                    counter+=1
                    
                labels.append("Net")
                slices.append(Totals["Total Income"]-Totals["Total Expense"])
                explode.append(0.05)
                    
                fig,ax = plt.subplots()
                
                ax.pie(slices,labels=labels,wedgeprops={"edgecolor":"black"},shadow=True,startangle=90,explode=explode, autopct = '%1.1f%%')
                ax.set_title("Percentage portion of your income")
                fig.legend(loc="lower right")
                plt.tight_layout()
                plt.show()
                
            elif "yes" in diagram and len(Expense["Expense"]) > 6: 
                x = []
                y = []
                amount = []
                
                counter = 0
                while counter != len(Expense["Expense"]):
                    x.append(Expense["Expense"][counter])
                    y.append((Expense["Cost"][counter]/Totals["Total Income"]))
                    amount.append(Expense["Cost"][counter])
                    counter+=1
                    
                x.append("Net")
                y.append((Totals["Total Income"]-Totals["Total Expense"])/Totals["Total Income"])
                amount.append((Totals["Total Income"]-Totals["Total Expense"]))
                
                sns.set_style("whitegrid")    
                fig,ax = plt.subplots()
                ax = sns.barplot(x=x,y=amount,ax=ax)
                for i, v in enumerate(y):
                   ax.text(i,v, f'{v:.0%}', ha='center')
                ax.set_xlabel("Expenses and Net")
                ax.set_ylabel("Amount")
                ax.set_title("Percentage portion of your income")
                plt.show()

#THE FINANCIAL MATHS FUNCTION
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
            N = int(input("What is the given number of the loan/investment years: "))
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
    print("\n")
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
            loan = float(input("What is the given size of loan: "))
            if loan <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break

        except ValueError:
            print("Please insert the number only,e.g 500")
            continue
    return loan

def installments():
    while True:
        try:
            installments = float(input("What is the given interval amount of installments: "))
            if installments <= 0:
                print("PLease enter a positive number")
                continue
            else:
                break

        except ValueError:
            print("Please insert the number only,e.g 460")
            continue
    return installments

#THE CLASS OF THE CALCULATOR
class Calculate:
    def CI(Pa,Ir,In,N):
        A = Pa*mt.pow((1+Ir/In),N*In)
        print("\n")
        print(f"The accumulated amount is R{round(A,2)}")
        RRR = (round(A,2) - Pa)/Pa * 100
        print(f"The rate of return is {round(RRR,2)}%")
    
    def SI(Pa,Ir,N):
        A = Pa*(1+Ir*N)
        print("\n")
        print(f"The accumulated amount is R{round(A,2)}")
        RRR = (round(A,2) - Pa)/Pa * 100
        print(f"The rate of return is {round(RRR,2)}%")
        
    def Install(loan,Ir,In,N):
        X_nom = loan*(Ir/In)
        X_dem = 1-mt.pow(1+Ir/In,-1*(N*In))
        X = X_nom/X_dem
        print(f"Your installments are R {round(X,2)}")
        print("\n")
        global Totals
        
        if Totals["Total Income"] > 0 and X < (Totals["Total Income"]*0.1):
            print("The installment payments is ideal for you!")
        elif Totals["Total Income"] > 0 and X > (Totals["Total Income"]*0.1):
            print("The installment payments are not ideal for you")
        else:
            print("Insert your income details for a suggestion")
    
    def Num_CI(Ac,Pa,Ir,In):
        N = mt.log((Ac/Pa))/mt.log((1+Ir/In))
        num = N/In
        print(f"It will take {round(num,2)} years")
    
    def Num_SI(Ac,Pa,Ir):
        N = (Ac/Pa-1)/Ir
        print(f"It will take {round(N,2)} years")
        
    def PV(installments,Ir,In,N):
        PV = installments*((1 - mt.pow(1+Ir/In,-N*In))/(Ir/In))
        print(f"The size of your loan is R {round(PV,2)}")
        print("\n")
        
        global Totals
        
        if Totals["Total Income"] > 0 and PV < (Totals["Total Income"]*0.2*12):
            print("The loan is ideal for you!")
        elif Totals["Total Income"] > 0 and PV > (Totals["Total Income"]*0.2*12):
            print("The loan amount are not ideal for you")
        else:
            print("Insert your income details for a suggestion")
            

#The admin
option = ["Add Income Details","Add Expense Details","View Details"," ",
          "Calculate Accumulated Amount (Compund Interest)","Calculate Accumulated Amount (Simple Interest)"," ",
          "Calculate Number Of Years (Compund Interest)","Calculate Number Of Years (Simple Interest)"," ",
          "Calculate Loan Amount","Calculate Interval Installments"]
df = pd.Series(option,index=[1,2,3," ",4,5," ",6,7," ",8,9])

while True:
    print("\n") #lastest change
    print("Available Options")
    print(df)
    while True:
        try:
            choice = int(input("Choose a number from the above table e.g 1: "))
            if choice >= 1 and choice <= 9:
                break
            elif choice == 400:
                sys.exit()
            else:
                print("Number does not exist on the table, use numbers on the table!! or insert 400 to exit")
                continue
            
        except ValueError:
            print("Invalid, Use the index numbers!!")
            continue
        
    if choice == 1:
        add_in()
    if choice == 2:
        add_ex()
    if choice == 3:
        view()
    if choice == 4:
        Calculate.CI(Pa(),Ir(),In(),N())
    if choice == 5:
        Calculate.SI(Pa(),Ir(),N())
    if choice == 6:
        Calculate.Num_CI(Ac(),Pa(),Ir(),In())
    if choice == 7:
        Calculate.Num_SI(Ac(),Pa(),Ir())
    if choice == 8:
        Calculate.PV(installments(),Ir(),In(),N())
    if choice == 9:
        Calculate.Install(loan(),Ir(),In(),N())
    if choice == 400:
        sys.exit()