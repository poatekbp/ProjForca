import random

class Hangman:
    #constructor method of the Hangman class
    def __init__(self):
        self.word_list = []
        self.word = ''
        self.hidden_word = ''
        self.trials = 1
        self.guessed = False
        self.file = ''
        self.corrects = ''

    #1
    def play(self):
        #Prints starting information on the screen
        print('===========================================')
        print('\tWELCOME TO HANGMAN')
        print('===========================================')

    #2
    def read_file(self):
        #Reads the file and returns a list with the words
        with open('C:\\Users\\Bruna Porto\\Desktop\\forca orientada a objetos-20240118T162958Z-001\\bd.txt') as file:
            word_list = file.readlines()
            return word_list
        
    #3
    def define_word(self, word_list):
        #Defines the random word from the list
        word = random.choice(word_list)
        word = word.strip()
        return word

    #4
    def anonymize_word(self, word):
        #Anonymizes word by replacing letters with dashes
        hidden_word = ''
        for _ in word:
            hidden_word += '*'
        print(f"The randomly chosen word is: {hidden_word} and it has {len(word)} characters.")
        print("You will have double the chances to guess correctly.")
        return hidden_word
    
    #5
    def check_corrects(self, word, corrects, guess):
    #Checks the correctness of the guess in relation to the word
        for index in range(len(word)):
            if guess == word[index]:
                corrects[index] = guess
        print(''.join(corrects))
        return corrects