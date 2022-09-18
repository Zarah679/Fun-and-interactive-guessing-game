#guess the number computer
import random

def guess(x):
    random_num = random.randint(1,x)

    #guess the number by using a while loop
    guess = 0 

    while guess != random_num:
        guess = int(input("Guess a number within the range of 1 and {}: ". format(x)))
        print(guess)

        #add some control flow to make it more fun!

        if guess < random_num:
            print("too low, guess again")
        elif guess > random_num:
            print("too high, guess agiain")
    
    print("Congratulations, your guess is {}!!".format(random_num))
            
guess(10)