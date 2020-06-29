import random

def NumberGuess():
    correct = random.randint(0,100)
    counter = 0
    print("I'm thinking of a number between 1 and 100 ... ")
    print("")
    guess = int(input("Please guess a number: "))
    counter +=1
    while guess != correct:
        if (guess < 1) or (guess > 100):
            print('Only guess numbers between 1 and 100.')
            guess = int(input("Please guess a number: "))
        if guess > correct:
            print(guess, 'is too high.')
            counter +=1
            guess = int(input("Please guess a number: "))
        if guess < correct:
            print(guess, 'is too low.')
            counter +=1
            guess = int(input("Please guess a number: "))
    if counter == 1:
        print("Congratulations! You guessed the number in 1 guess!")
    if counter > 1:
        print("Congratulations! You guessed the number in", counter, "guesses!\n")

    #Keep window open for viewing
    input('Press Enter to Exit...')
    
NumberGuess()
