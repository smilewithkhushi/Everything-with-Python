print(" ****** LETS PLAY WITH STRINGS ******* ")
userinput = input("Enter your string : ")
''' so program will tell various options to the user which will help user to perform operations on the string'''

print("\n ****** OPTIONS ****** ")
print("Press 1 to make Uppercase string")
print("Press 2 to make lowercase string")
print("Press 3 to count letters in string")
print("Press 4 to count vowels in string")

print()
choice = int(input("Enter your choice from the above: "))
print()

if (choice == 1):
  print("The uppercase string is : ", userinput.upper())
elif (choice == 2):
  print("The lowercase string is ", userinput.lower())
elif (choice == 3):
  l = len(userinput)
  print("The count of letters in string is ", l)

elif (choice == 4):
  count = 0
  for x in userinput:
    if x in "AEIOUaeiou":
      count = count + 1
  print("The count of vowels in string is ", count)

else:
  print("Invalid choice")

print("===================================")
print("Program ends here!!")
