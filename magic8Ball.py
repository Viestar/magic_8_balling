"""
Creating a Python project of a Magic 8 Ball which is a toy used for fortune-telling or
seeking advice.
● Allow the user to input their question.
● Show an in progress message.
● Create 10/20 responses, and show a random response.
● Allow the user to ask another question/advice or quit the game.
"""
# importing the system for, random module for, and time module to depict processing time

import sys, random, time

# creating of responses for the random output

answers = ["Very sure", "go ahead", "Most likely", "Absolutely yes", "Outlook is good", "I see good things happening", 
"commit suicide","give 10m $", "give your chocolate to your sister", "Andela is stealing you from us", 
"hack them and hire yourself", "Alles Gute", "vielleicht", "go to hell this time", "concentrate and ask again", "Yes", 
"You in Andela already", "Possible, but not probable", "this game isnt real like that", "All the best in Andela"]

# Player's customised welcome package and a sense of a deeper process involved

print("Hey buddy, it's the legendary Magic 8 Ball:\n")
name = input('Can i know your name before we play?\n')
print('Great name!\n\nWelcome legendary ' + name.title()+ '!\n\n')
print("a moment " + name.title() +", let me tell the gods about your arrival.")
time.sleep(3)
print("Alright, you've been accepted\n")

# creating a method to run the game 
def magic8Ball():

    input("let's kick it then, question or advice? i'm ready for any!\n")
    time.sleep(3)
    print(". . .. ... ...")
    time.sleep(3)

    print("\n <-- ============ ======== ============ ++ > \n")
    print(random.choice(answers))
    print("\n <-- ============ ======== ============ ++ > ")

    reply = input('\nTap the "SPACE KEY" to continue with your quest or any key to exit')
    while reply == str(" "):
        magic8Ball()
    else:
        exit()

magic8Ball()