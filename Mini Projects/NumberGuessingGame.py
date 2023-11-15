import random
#choose the range to select any random number
start = int(input("Enter the starting value : "))
end = int(input("Enter the ending value : "))
num = random.randint(start, end)
count = 5
i = 1
while (i <= count):
  print("\n ================================= \n")
  print(">> Trial Number : ", i)
  guess = int(input("Guess a number : "))
  if (guess == num):
    print("You guessed it right!")
  else:
    print("You guessed it wrong! try again...")
  i += 1

print()  #add leaderboard as well
print("The random number was : ", num)
print(" ****** Game ends here! thank you for playing ****** ")
