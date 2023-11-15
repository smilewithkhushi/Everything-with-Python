def displayOperations():
  print("\n ================================== \n")
  print("\t *** ADVANCED CALCULATOR ** ")
  print("Operations available: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Factorial")
  print("6. Exponent")
  print("\n ================================== \n")


def addition(a, b):
  print("\n -->> Addition Operation <<--")
  res = a + b
  print("Result: ", res)


def subtraction(a, b):
  print("\n -->> Subtraction Operation <<--")
  res = a - b
  print("Result: ", res)


def multiplication(a, b):
  print("\n -->> Multiplication Operation <<--")
  res = a * b
  print("Result: ", res)


def division(a, b):
  print("\n -->> Division Operation <<--")
  res = a / b
  print("Result: ", res)


def exponent(a, b):
  print("\n -->> Exponent Operation <<--")
  res = a**b
  print("Result: ", res)

def factorial(num):
  num = int(num)
  print("\n -->> Factorial Operation <<--")
  fact = 1
  for i in range(1,num+1):
    fact = fact* i
  print("Factorial of ", num , " : ", fact)


response = "yes"
while (response in ["yes", 'y', "sure", "Yes", "YES"]):
  displayOperations()
  choice = int(input("Enter your choice: "))
  a = float(input("Enter a number here : "))
  b = float(input("Enter another number here: "))

  if (choice == 1):
    addition(a, b)
  elif choice == 2:
    subtraction(a, b)
  elif choice == 3:
    multiplication(a, b)
  elif choice == 4:
    division(a, b)

  elif choice == 5:
    factorial(a)
    factorial(b)
    
  elif choice == 6:
    exponent(a, b)

  else:
    print("Invalid Operation choosen!  TRY AGAIN")

  response = input("\n Do you want to continue? y/n : ")

print("\n !! PROGRAM ENDS HERE !! ")
