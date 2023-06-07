import random

def word_guess():
   
    
    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    
    word = random.choice(words)
    guessed_letters = []
    attemps = 12
    
    print("Welcome to the Guess word game")
    print(f"you have {attemps}")

    while attemps>0:
        print("\nCurrent word: ", end="")
        for letter in word:
            if letter in guessed_letters:
               print(letter,end=" ")

        guess = input("\n Enter your guess (one letter)").lower()
        
        if guess in guessed_letters:
            print("You have already guessed that letter. try again")
            continue
        guessed_letters.append(guess)
        
        if guess in word:
            print("correct guess")

            #check if all letters have been guessed
            if all(letter in guessed_letters for letter in word):
                print("congrats you guessed the word correctly")
                break
                
        else:
            attemps-=1
            print("wrong guess.")
    else:
        print(f"game over the word was {word}")
        
        
        
word_guess()