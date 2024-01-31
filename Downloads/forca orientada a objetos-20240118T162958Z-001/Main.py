from Hangman import Hangman
import random

if __name__ == "__main__":
    game = Hangman()
    game.play()
    word_list = game.hangman.read_file()
    word = game.define_word(word_list)
    trials = (len(word) * 2)
    hidden_word = game.anonymize_word(word)
    corrects = list(hidden_word)

    while (game.guessed == False or trials >= 1):
        
        guess = input("Provide a letter: ")
        verify = game.check_corrects(word, corrects, guess)

        if (len(guess) > len(word)):
            guess = input("Provide a valid letter: ")
        
        elif guess == word or corrects == list(word):
            game.guessed = True
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
