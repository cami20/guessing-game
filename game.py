"""A number-guessing game."""

print "Hey, what's your name?"
user_name = raw_input("Input your name: ")
print "Your name is %s!" % (user_name)

import random
random_number = random.randint(0, 101)
print random_number

guess_number = raw_input("Please enter your number: ")
guess_number = int(guess_number)
while guess_number < 0 or guess_number > 100:
    print "Your number is not between 0 and 100."
    guess_number = raw_input("Please enter a new number between 0 and 100: ")
    guess_number = int(guess_number)