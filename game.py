"""A number-guessing game."""

print "Hey, what's your name?"
user_name = raw_input("Input your name: ")
print "Your name is %s!" % (user_name)

import random
random_number = random.randint(0, 100)
print random_number


def check_valid_guess(guess_number):
    try:
        guess_number = int(guess_number)
        while guess_number < 0 or guess_number > 100:
            print "Your number is not between 0 and 100."
            guess_number = raw_input("Please enter a new number between 0 and 100: ")
            guess_number = int(guess_number)
            check_valid_guess(guess_number)
        return guess_number
    except:
        print "That is not a number."
        guess_number = raw_input("Please enter a new number between 0 and 100: ")
        return check_valid_guess(guess_number)

guess_number = (raw_input("Please enter your number: "))
guess_number = check_valid_guess(guess_number)
tries = 1
while guess_number != random_number:
    tries += 1
    print "That's not it!"
    if guess_number < random_number:
        print "that's too low!"
    else:
        print "that's too high!"
    guess_number = int(raw_input("Please enter another number: "))
    check_valid_guess(guess_number)

print "You got it!"
print "It took %d tries." % (tries)


