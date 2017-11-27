import random

def goguess():
    print("I have a number between 1 and 20 inclusive.")
    
    answer = random.randint(1, 20)
    n = 1
    total = 0
    
    while n == 1:
        total += 1
        guess = int(raw_input("Guess: "))
        
        if guess < answer:
            print("%s is too low.") % (guess)
            
        elif guess > answer:
            print ("%s is too high.") % (guess)
            
        else:
            print("Right! My number is %s! You guessed it in %d guesses!") % (guess, total)
            n = 0
        
            
goguess()