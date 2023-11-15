#list program - question 2

def totalSales():
    sw1=float(input("Sales done in week 1 : ")) 
    sw2=float(input("Sales done in week 2 : ")) 
    sw3=float(input("Sales done in week 3 : ")) 
    sw4=float(input("Sales done in week 4 : "))
    total=sw1+sw2+sw3+sw4
    #calculating commision for a month
    if (total>=50000):
        comm=5/100*total
    else:
        comm=0
    #calculating remarks
    if (total>80000):
        remarks="Excellent"
    elif (total>=60000 and total<80000):
        remarks="Good"
    elif (total>=40000 and total<60000):
        remarks="Average"
    else:
        remarks="Work Hard"

    #storing in tuple
    result=(total, comm, remarks)
    return result

print("\t **PROGRAM 2 : CALCULATE THE SALES DONE BY SALESMAN IN A MONTH AND SHOW DATA **")
print()
sales, com, rem=totalSales()
print()
print("-> The Total Sales in a month are : Rs ", sales)
print("-> The Commission given to the salesman : Rs ", com)
print("-> Remarks : ", rem)
