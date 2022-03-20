import numpy as np

# Create a class that can manage scraping pre-formatted files to serve a prompt
class PromptScraper():
    filename = ""
    word_bank = []

    # -------------------------------------- Constructors
    def __init__(fname):
        global filename, word_bank
        
        filename = fname
        word_bank = create_word_bank(fname)
    
    def __init__(fname, wordBnk):
        global filename, word_bank

        filename = fname
        word_bank = wordBnk

    # Take an Fname and creates a word bank if one is not used in the constructor
    def create_word_bank(fname):
        prompts = []

        with open(fname, "r") as file:
            word = ""
            while(word := file.readline()):
                prompts.append(word)

        return prompts

    # ------------------------------------------------ Class Methods

    # Serves a prompt as a return from the class word bank
    def give_prompt():
        global word_bank
        return word_bank[np.random.randint(0, len(word_bank))]
    
    # Serves a prompt of more than one word from the word bank
    def give_prompt(count):
        global word_bank
        prompt = ""

        for i in count:
            prompt += word_bank[np.random.randint(0, len(word_bank))] + " "
        return prompt

    # Getter method to pull the word bank out of the class
    def get_bank():
        return word_bank