"""
Egbert Lib
by iridiumJester
Mad Lib-like project.
"""

#import statements and define functions
import time
import os
def wait_clear():
    time.sleep(3)
    os.system('cls')
def wait():
    time.sleep(3)
def clear():
    os.system('cls')

#welcome user
print("Greetings, user. Would you like to play a game? A word game?")
wait()
play = input("Seriously, would you like to play. yes/no: ")
clear()
if play == "yes":
    print("How wonderful!")
else:
    input("Huh? Alright then. Change your mind? Press enter to continue.")
clear()

#get user input
adj1 = input("Please enter an adjective: ")
noun1 = input("A noun: ")
pronoun_obj = input("An objective pronoun (his, hers, their): ")
pronoun_sub = input("A subjective pronoun (he, she, they): ")
date = input("A date (Ex: 7th of July, 2007): ")
num = int(input("A number below 100: "))
clear()
print("Prompts marked with (C) should be in ALL CAPS.")
name = input("A first name (C): ")
plural_noun1 = input("A plural noun (C): ")
plural_noun2 = input("Another plural noun (C): ")
adj2 = input("An adjective (C): ")
plural_noun3 = input("Another another plural noun (C): ")
verb1 = input("A verb NOT ending in -ing: ")
clear()
plural_noun4 = input("Another another another plural noun: ")
noun2 = input("An interest (C): ")
adj3 = input("An adjective (C): ")
noun3 = input("A noun (C): ")
verb2 = input("A verb: ")
plural_noun5 = input("One last plural noun (C): ")
clear()

#build story
sentence1 = "A " + adj1 + " " + noun1 + " stands in " + pronoun_obj + " bedroom. It just so happens that today, the " + date + ", is this " + adj1 + " " + noun1 + "'s birthday."
sentence2 = "Though it was " + num + " years ago " + pronoun_sub + " was given life, it is only today " + pronoun_sub + " will be given a name!"
sentence3 = "Your name is " + name + ". As was previously mentioned it is your BIRTHDAY."
sentence4 = "A number of " + plural_noun1 + " are scattered about your room. You have a variety of " + plural_noun2 + "."
sentence5 = "You have a passion for REALLY " + adj2 + " " + plural_noun3 + ". You like to " + verb1 + " " + plural_noun4 + " but you are NOT VERY GOOD AT IT."
sentence6 = "You have a fondness for " + noun2 + ", and are an aspiring " + adj3 + " " + noun3 + ". You also like to " + verb2 + " " + plural_noun5 + " sometimes."


#show results
input("Press enter to show results.")

#send the user your FONDEST regards and quit
input("Sorry for Homestucking you. Press enter to get the heck out of here.")