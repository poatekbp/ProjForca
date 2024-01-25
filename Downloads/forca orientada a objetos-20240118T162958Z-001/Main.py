from Hangman import Hangman
import random

class Main:

    def __init__(self):            
        #Instantiating the Hangman object
        self.hangman = Hangman()

    def play(self):
        #Calling the play function
        self.hangman.play()

if __name__ == "__main__":
    game = Main()
    game.play()
    word_list = game.hangman.read_file()
    word = game.hangman.define_word(word_list)
    trials = (len(word) * 2)
    hidden_word = game.hangman.anonymize_word(word)
    corrects = list(hidden_word)

    while (game.hangman.guessed == False or trials >= 1):
        
        guess = input("Provide a letter: ")
        game.hangman.check_corrects(word, corrects, guess)

        if (len(guess) > len(word)):
            guess = input("Provide a valid letter: ")
        
        elif guess == word or corrects == list(word):
            game.hangman.guessed = True
            print("Congratulations, you got it right!")
            break
        else: 
            trials = trials - 1
            if(trials > 0):
                print(f"You still have {trials} attempt(s)!")   
            elif (trials == 0):
                print("You lost!")
                print(f"The word was {word}")
                break