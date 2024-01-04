import random

def show_message():
  print()
  print("="*30)
  print("Welcome to the Hangman Game! \n A word will be chosen at random and you must try to guess the word correctly letter by letter before you run out of attempts. Good luck")
  print("="*30)
  print()

def play_game():
  play = True

  while play:
    #words to be choosen at random in the game
    words = ["hangman", "school", "computer", "coding", "python", "gaming", "football", "chairs", "backpack", "bodywash", "clothing", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo"
]
    chosen_word = random.choice(words).lower()
    player_guess = None      #to save the guess of the player
    guessed_letters = []
    word_guessed = []        #to save the guess of the player with each letter

    for letter in chosen_word:
      word_guessed.append(" - ")

    joined_word = None

    HANGMAN = (
    """
    -----
    |   |
    |
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    |  -+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  |
    |
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | 
    |
    --------
    """,
    """
    -----
    |   |
    |   0
    | /-+-\ 
    |   | 
    |   | 
    |  | | 
    |  | | 
    |
    --------
    """)

    print(HANGMAN[0])
    attempts = len(HANGMAN ) - 1

    while (attempts != 0 and " - " in word_guessed):
      print("\n ->> You have ", attempts , " attempts remaining!")
      joined_word = "".join(word_guessed)
      print("\t", joined_word)
      player_guess = input("\n>> Select a letter between a-z :: ")

      guessed_letters.append(player_guess)

      for letter in range(len(chosen_word)):
        if player_guess == chosen_word[letter]:
          word_guessed[letter] = player_guess

      if player_guess not in chosen_word:
        attempts -=1
        print(HANGMAN[(len(HANGMAN) - 1) - attempts])

    if "-" not in word_guessed:
      print("\n **  Congratulations!!", chosen_word, " was the word. **")
    else:
      print("\n **  Unlucky! The word was ", chosen_word)
      play = False
    


choice = "yes"
while (choice=="yes" or choice=="y"):
  show_message()
  play_game()
  choice = input("Would you like to play again? y/n : ")

print("\n ** PROGRAM ENDS HERE ** ")
