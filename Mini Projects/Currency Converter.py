def showCurrency():
  print("="*30)
  print("Available currencies :")
  print("1 -> AED to INR ")
  print("2 -> INR to AED")
  print("="*30)

#This function converts the cash from AED to INR  currency
def AEDtoINR(cash):
  #1 AED = 22 INR
  #100 AED -> 22*100 INR -> 2200 INR
  totalINR = cash*22.00
  return totalINR  

#this function converts the cash from INR to AED Currency
def INRtoAED(cash):
  totalAED = cash/22
  return totalAED

choice = "yes"
while (choice=="yes" or choice=="y"):
  showCurrency()
  conversion = int(input("Which currency conversion do you want to perform? "))

  if (conversion == 1):
    print("\nYou have choosen AED to INR Conversion")
    cash = float(input("Enter your amount of cash/money : "))
    result = AEDtoINR(cash)
    print(result, "INR is the converted amount")
    
  elif (conversion == 2):
    print("\nYou have chosen INR to AED Conversion")
    cash = float(input("Enter your amount of cash/money : "))
    result = INRtoAED(cash)
    print(result, "AED is the converted amount")
    
  else:
    print("\n Invalid option")

  print()
  choice = input("Do you want to continue? (y/n) : ")

print("\tProgram ends here!!")  
