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
    input("Huh? Alright then. Change your mind? Press anything to continue.")
clear()

#get user input
adj1 = input("Please enter an adjective: ")
noun1 = input("A noun: ")
pronoun_obj = input("An objective pronoun (his, hers, their): ")
pronoun_sub = input("A subjective pronoun (he, she, they): ")
date = input("A date (Ex: 7th of July, 2007): ")
clear()
num = int(input("A number below 100: "))
name = input("A first name: ")
plural_noun1 = input("A plural noun: ")
adj2 = input("An adjective: ")
plural_noun2 = input("Another plural noun: ")
clear()
verb1 = input("A verb NOT ending in -ing: ")
plural_noun3 = input("Another another plural noun: ")
noun2 = input("A noun: ")
adj3 = input("An adjective: ")
noun3 = input("A noun: ")
clear()
verb2 = input("A verb: ")
plural_noun4 = input("One last plural noun: ")

#build story


#show results


#send the user your FONDEST regards and quit
input("Sorry for Homestucking you. Press anything to get the heck out of here.")