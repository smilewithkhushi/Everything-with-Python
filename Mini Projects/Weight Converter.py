"""
PROJECT OVERVIEW : A weight conversion project where you can convert weight from KGs to pound and vice versa

Task1 : how should we proceed with the weight conversion project??
THINK and BRAINSTORM
"""

def kg_to_pound(kg):
  pounds = kg * 2
  print(kg, "kg =", pounds, " pounds")

def pound_to_kg(pound):
  kg = pound * 0.4
  print(pound, "pound = ", kg, " kgs")


def weightUnits():
  print()
  print("="*30)
  print("The weight units and unit conversion available are : ")
  print("1 -> KGs to Pounds")
  print("2 -> Pounds to KGs")
  print("Select 1 or 2 to choose the conversion!")
  print("="*30)
  print()


choice = "yes"
while (choice=="yes" or choice=="y"):
  weightUnits()
  conversion = int(input("Which conversion do you want to perform? "))

  if (conversion ==1 ):
    print("\n -> Performing KG to Pounds Conversion")
    weight = float(input("Enter your weight in Kg : "))
    kg_to_pound(weight)

  elif (conversion == 2):
    print("\n -> Performing Pounds to KG Conversion")
    weight = float(input("Enter your weight in Pounds : "))
    pound_to_kg(weight)

  choice = input("\nDo you want to continue (y/n) : ")

print("\n PROGRAM ENDS HERE!!")
    

