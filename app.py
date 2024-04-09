"""
Egbert Lib
by iridiumJester
Mad Lib-like project.
"""

#import statements and define functions
import time
import os
def wait():
    time.sleep(2.5)
def long_wait():
    time.sleep(4)
def clear():
    os.system('cls')
def line_break():
    print("\n")

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
silly_name = input("A very silly full name (C): ")
first_name = input("A first name (C): ")
last_name = input("A last name (C): ")
plural_noun1 = input("A plural noun (C): ")
clear()
plural_noun2 = input("Another plural noun (C): ")
adj2 = input("An adjective (C): ")
plural_noun3 = input("Another another plural noun (C): ")
verb1 = input("A verb NOT ending in -ing: ")
plural_noun4 = input("Another another another plural noun: ")
clear()
noun2 = input("An interest (C): ")
adj3 = input("An adjective (C): ")
noun3 = input("A noun (C): ")
verb2 = input("A verb: ")
plural_noun5 = input("One last plural noun (C): ")
clear()

#build story
sentence1 = "A " + adj1 + " " + noun1 + " stands in " + pronoun_obj + " bedroom. It just so happens that today, the " + date + ", is this " + adj1 + " " + noun1 + "'s birthday."
sentence2 = "Though it was " + str(num) + " years ago " + pronoun_sub + " was given life, it is only today " + pronoun_sub + " will be given a name!"
naming1 = "Enter name: "
naming2 = "TRY AGAIN!!!: "
sentence3 = "Your name is " + first_name + ". As was previously mentioned it is your BIRTHDAY."
sentence4 = "A number of " + plural_noun1 + " are scattered about your room. You have a variety of " + plural_noun2 + "."
sentence5 = "You have a passion for REALLY " + adj2 + " " + plural_noun3 + ". You like to " + verb1 + " " + plural_noun4 + " but you are NOT VERY GOOD AT IT."
sentence6 = "You have a fondness for " + noun2 + ", and are an aspiring " + adj3 + " " + noun3 + ". You also like to " + verb2 + " " + plural_noun5 + " sometimes."

#show results
input("Press enter to show results.")
clear()
print(sentence1)
long_wait()
print(sentence2)
line_break()
long_wait()
print(naming1)
print(silly_name)
wait()
print(naming2)
print(first_name + " " + last_name)
line_break()
wait()
long_wait()
print(sentence3)
long_wait()
print(sentence4)
long_wait()
print(sentence5)
long_wait()
print(sentence6)
line_break()
wait()
input("Press enter to continue.")
clear()

#send the user your FONDEST regards and quit
user_review = input("Did you like my awesome program? yes/no: ")
if user_review == "yes":
    print("Awwwww, thanks! :D")
else:
    print(":(")
wait()
input("Press enter to quit.")