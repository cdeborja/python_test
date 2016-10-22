import os
import string

def find_element_in_string(element, string):
    try:
        index_element = string.index(element)
        return index_element
    except ValueError:
        return None

guesses_remaining = 5
valid_letters = string.lowercase
answer = raw_input("Input one secret word: ").lower()
shown = ""
os.system('clear')

for letter in answer:
    shown+= ("_")


while guesses_remaining > 0:
    print shown
    print "Guesses Remaining: " + str(guesses_remaining)
    guess = raw_input("Guess a letter: ").lower()
    os.system('clear')
    if len(guess) > 1 or len(guess) == 0 or find_element_in_string(guess,valid_letters) == None:
        print "Please enter valid character"
    elif find_element_in_string(guess, answer) >= 0:
        print "found a letter"
    else:
        print "Letter doesn't exist"
        guesses_remaining-= 1
