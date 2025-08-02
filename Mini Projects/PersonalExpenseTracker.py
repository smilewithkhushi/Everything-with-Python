#PERSONAL EXPENSE TRACKER

import csv
csv_file = 'expenses.csv'

#function to start the file/initialize csv
def initializeCSV():
    try:
        file = open(csv_file, "x")
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Description', 'Amount'])
    except FileExistsError:
        pass    #no initialization because file already exists
    
#function to record the expenses
def recordExpenses():
    print("~~~~~~~~~~~~~~~~~~~~~~")
    inp_date = input("Enter the date: ")
    inp_category = input("Enter the category (Food, Shopping, Household, Travel, Misc) : ")
    inp_desc = input("Enter the description: ")
    inp_amt = float(input("Enter the amount: "))
    print("~~~~~~~~~~~~~~~~~~~~~~")
    #storing the above data in the csv file
    file = open(csv_file, mode='a')
    writer = csv.writer(file)
    writer.writerow([inp_date, inp_category, inp_desc, inp_amt])
    print(">>> Expense added successfully!")
    file.close()    

#function to show the expenses
def showExpenses():
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            print("Date \t | Category \t | Description \t | Amount")
            for row in reader:
                if row==[]:
                    pass
                else:
                    print(row[0],"\t | ",row[1],"\t | ", row[2],"\t | ", row[3])
    except:
        print("No contents found in the file")

#function to show sum of all expenses
def totalExpenses():
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    total=0
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row==[]:
                    pass
                else:
                    total+=float(row[3])
            print("Total expenses =", total)
    except:
        print("No contents found in the file")

#function to show the expenses category wise
def categoryExpenses():
    file = open(csv_file, mode='r')
    reader = csv.reader(file)
    next(reader)
    #(Food, Shopping, Household, Travel, Misc)
    categoryExp = {"Food": 0, "Shopping": 0, "Household": 0, "Travel":0, "Misc":0}
    for row in reader:
        if row==[]:
            pass
        else:
            cat = row[1]
            categoryExp[cat]+=float(row[3])
    file.close()
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    print(">> Category wise expenses are as: ")
    for i in categoryExp:
        print(i, "\t \t -> \t", categoryExp[i])
                
#function to display various operations
def options():
    print("\n=======================================")
    print("SELECT THE OPTION TO CHOSE OPERATION")
    print("1 - Add Expenses")
    print("2 - Show Expense")
    print("3- Total Expenses")
    print("4- Category wise expenses")
    print("=======================================\n")
    option = int(input("Enter your choice: "))
    return option

#function to handle the entire program
def main():
    initializeCSV()
    choice="y"
    while choice=="y":
        opt = options()
        if opt==1:
            recordExpenses()
        elif opt==2:
            showExpenses()
        elif opt==3:
            totalExpenses()
        elif opt==4:
            categoryExpenses()
        else:
            print("~~ Invalid Option. Please try again!")

        choice = input("> Do you want to continue? (type *y* for yes) : ")
    print("\n *** THE PROGRAM CLOSES HERE*** \n")

#calling the mainfunction to start the program
main()    
    
    
