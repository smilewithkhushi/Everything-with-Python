#ques 1 - write a function that accepts input parameter as number of rows to be printed and prints the figures:

def pattern_1(rows):
    print("\n\t\t\t ********* PATTERN A ******** ")
    for i in range(1, rows+1):
        for j in range(1,i+1):
            print(j, "\t", end="")
        print()

def pattern_2(rows):
    print("\n\t\t\t ********* PATTERN B ******** ")
    k=flag1=flag2=0
    
    for i in range(1, rows+1):
        for space in range(1,(rows-i)+1):
            print("   ", end="")
            flag1+=1
            
        while k!=((2*i)-1):
            if flag1<=rows-1:
                print(i+k, end="  ")
                flag1+=1
            else:
                flag2+=1
                print(i+k-(2*flag2), end="  ")
            k+=1
        k=flag1=flag2=0
        print()
    
def pattern_3(rows):
    print("\n\t\t\t ********* PATTERN C ******** ")
    for i in range(rows, 0,-1):
        for j in range(i,0,-1):
            print(j, "\t", end="")
        print()

def pattern_4(rows):
    print("\n\t\t\t ********* PATTERN D ******** ")
    for i in range(1, rows+1):
        for j in range(1,i+1):
            print(i, "\t", end="")
        print()

def pattern_5(rows):
    print("\n\t\t\t ********* PATTERN E ******** ")
    for i in range(0, rows):
        print("    "*i, end="")
        for j in range(i+1,rows+1):
            print(j,"  ", end="")
        print()
        
def pattern_6(rows):
    print("\n\t\t\t ********* PATTERN F ******** ")
    for i in range(1, rows+1):
        if (i==1 or i==rows):
            print("* "*rows)
        else:
            print("*"," "*4," *")

print("\n \t ** THIS PROGRAM GENERATES 6 DIFFERENT PATTERNS ** \n")
r=int(input("Enter the number of rows : "))
pattern_1(r)
pattern_2(r)
pattern_3(r)
pattern_4(r)
pattern_5(r)
pattern_6(r)
