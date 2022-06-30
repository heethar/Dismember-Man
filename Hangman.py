'''
Name: Heather Shirely
Application name: Hangman.py
Purpose: This application is a game of hangman, where the user will input random letters
in hopes to guess a correct letter of an 8-letter word to not dismember the ASCII man.
There is a list of random words (that will also be randomly selected) in a separate text
time named "words.txt" 
'''


import random 

#below is a tuple that Python will systematically go through once someone dismembers him by choosing a wrong letter.
HANGMAN = (
"""
      .-.
     (o.o)
      |u| <Hello, friend!
     __|__
   //.=|=.\\
  // .=|=. \\
  \\  .=|=. //
   \\ (_=_)//
    (:| |:)
     || ||
     () ()
     || ||
     || ||
    ==' '==
""",
"""
      .-.
     (o.o)
      |=|
     __|__
   //.=|=.\\
  // .=|=. \\
  \\  .=|=. //
   \\ (_=_)//
    (:| |:)
     || 
     () 
     || 
     || 
    ==' 
""",
"""
      .-.
     (o.o)
      |^|
     __|__
     .=|=.\\
     .=|=. \\
     .=|=. //
     (_=_)//
    (:| |:)
     || 
     () 
     || 
     || 
    ==' 
""",
"""
      .-.
     (;.;)
      |o|
     __|__
       |=.\\
     .=|   \\
       |=. //
     (_=_)//
    (:| |:)
     || 
     () 
     || 
     || 
    ==' 
""",
"""
      .-.
     (;.;)
      |^|
     __|__
       |=.
     .=|   
       | 
     (_=_)
    (:| |:)
     || 
     () 
     || 
     || 
    ==' 
""",
"""
      .-.
     (o,o)
      |^|
     __|__
       |=.
     .=|   
       | 
     (_=_)
    (:| |:)

""",
"""
      .-.
     (x,o)
      |o|<please help
     __|__
       |=.
     .=|   
""",
"""
      .-.
     (x,x)
      |||
      *dead*
""")

#open and retrieve the word list
with open("words.txt") as f:
#make the words a list of words
    WORDS = f.read().splitlines()
word = random.choice(WORDS)
Encouragement = ("Amazing!", "w00t!1!!", "Well done!", "Awesome!", "GO YOU!", "Nice!") #these are just nice to read
#The amount of lives depends on the length of the word. Therefore, all words are 8 charachers so the image fits appropriately
MAX_WRONG = len(word) - 1
so_far = ("-") * len(word)
#initiate an empty list for letters that will be used
used = []
#initiate a value for lives so MAX_WRONG works
wrong = 0 


print("\t \t Welcome to Hangman!") #\t is a tab or a indention for the title of this game
print()
input("Press any input key to START: ") #Just a blank input to cease beginning until user says so


while wrong < MAX_WRONG and so_far != word: #while the wrong amount of attempts are less than the maximum amount, the word can still be updated by the user.
    print()
    print(HANGMAN[wrong])#this will show the symbol in the tuple represented by the amount of incorrect attempts
    print("Word so far: ", so_far) #this updates each correct letter.
    print("Letters attempted: ", used) #this will output the letters that the users has attempted incorrectly.

    guess = input("Guess a letter: ").upper() #This will take any letter and make it capitalized to match the word list
    print()

    while guess in used: #when python sees a guess used more than once...
        print("You have already tried this letter!") #Python will then say this to the user
        guess = input("Guess a letter: ").upper() #and allow the user to try again. .upper() will take any letter used and make it capitalized
        print()
    used.append(guess)#Append will add each guess as they are guessed to a list

    if guess in word: #if the letter that was guessed was also found in the word, Python will output words of encouragement
        print(random.choice(Encouragement),"...Updating word...") #again, these are nice to read...

        new = "".join(
            guess if guess == word[i] else so_far[i] for i in range(len(word))
        )

        so_far = new #unless the letter does not match, it will return the previous word

    else:
        print("Whoops! Try again!")
        wrong += 1 #instead of subtracting lives, this adds to the wrong number of attempts


if wrong == MAX_WRONG: #if attempts matches the maximum, they have lost the game.
    print("       .-.")#I wanted to make sure the users knew that they have killed the ASCII man, it was not always guaranteed with the tuple.
    print("      (x,x)")
    print("       |||")
    print("     *dead*")
    print("Sorry, the word was", word,". Better luck next time.") #This gives the closure of finding out what the correct word would have been

else:
    print()
    print("Congratulations! The word was", word,". You have saved this man's life.")
    print()
print()
play_again = input("Do you want to restart? Yes or No:  ")
exec(open("./Hangman.py").read())
