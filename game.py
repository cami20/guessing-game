"""A number-guessing game."""
import random

print "Hey, what's your name?"
user_name = raw_input("Input your name: ")
print "Your name is %s!" % (user_name)

play = True

scores = 0
turns = 1
while play:

    random_number = random.randint(0, 100)
    print random_number

    def check_valid_guess(guess_number):
        '''checks to make sure that input is a number'''

        try:
            guess_number = int(guess_number)
            return guess_number
        except:
            print "That is not a number."
            guess_number = raw_input("Please enter a new number between 0 and 100: ")
            return check_valid_guess(guess_number)

    #asks user for guess
    guess_number = (raw_input("Please enter your number: "))
    #calls function to check if valid guess
    guess_number = check_valid_guess(guess_number)

    tries = 1

    # checks if guessed correctly and allows to guess again
    while guess_number != random_number:
        #checks to see if guess is withing the range
        while guess_number < 0 or guess_number > 100:
            print "Your number is not between 0 and 100."
            guess_number = raw_input("Please enter a new number between 0 and 100: ")
            guess_number = check_valid_guess(guess_number)
        tries += 1
        print "That's not it!"
        if guess_number < random_number:
            print "that's too low!"
        else:
            print "that's too high!"
        guess_number = raw_input("Please enter another number: ")
        guess_number = check_valid_guess(guess_number)

    print "You got it!"
    print "It took %d tries." % (tries)
    if turns == 1:
        scores = tries
    else:
        if scores > tries:
            scores = tries

    print "Your best score is %d." % (scores)

    continue_on = (raw_input("Would you like to play again? ")).lower()
    if continue_on == 'no':
        play = False
    else:
        turns += 1
