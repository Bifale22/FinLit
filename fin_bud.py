import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

Income = {"Income":[],"Amount":[]}
Expense = {"Expense":[],"Cost":[]}
Totals = {"Total Income":0,"Total Expense":0} 


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
                print("Insert a number, 500")
                continue
        counter+=1
        
    global Totals
    temp = 0
    for amount in Income["Amount"]:
         temp +=amount
         
    Totals["Total Income"] = temp
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
    
    print("Your total expense is R",temp)
    #Saving it into a table
    data = pd.DataFrame(Expense,index=range(1,(len(Expense["Expense"])+1)))
    print("\n")
    print(data)

def view():
    data = ["Income","Expense","Overall"]
    index = ["1","2","3"]
    print("Available options")
    option = pd.Series(data,index=index)
    
    print(option)

    while True:
            choice = input("Choose from the above options: ").capitalize()
            if choice.isalpha() and choice in data:
                break
            else:
                print(choice)
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
        
    elif choice == "Expense":
        if len(Expense["Expense"]) == 0:
            print("There's no data, Create a budget for expense!")
            return 0
        choice = pd.DataFrame(Expense,index=range(1,(len(Expense["Expense"])+1)))
        print(choice)
        
    else:
        if (len(Income["Income"]) == 0) or (len(Expense["Expense"]) == 0):
            print("There's no data for both income and expense, Create a budget for both your income and expenses!")
            return 0

        choice = pd.DataFrame(Income,index=range(1,(len(Income["Income"])+1)))
        choice1 = pd.DataFrame(Expense,index=range(1,(len(Expense["Expense"])+1)))
        print("\n")
        print(choice)
        print("\n")
        print(choice1)
        
        global Totals
        
        print("Your total income is: R",Totals["Total Income"])
        print("Your total expense is: R",Totals["Total Expense"])
        print("\n")
        if Totals["Total Income"] > Totals["Total Expense"]:
            print("Your Net profit is: R",Totals["Total Income"]-Totals["Total Expense"])
        else:
            print("Your Net loss is: R",Totals["Total Expense"]-Totals["Total Income"])
        
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


view()




 


