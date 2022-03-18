import numpy as np

# Create a class that can manage scraping pre-formatted files to serve a prompt
class PromptScraper():
    filename = ""
    word_bank = []

    def __init__(fname):
        global filename, word_bank
        
        filename = fname
        word_bank = create_word_bank(fname)
    
    def __init__(fname, wordBnk):
        global filename, word_bank

        filename = fname
        word_bank = wordBnk

    def create_word_bank(fname):
        prompts = []

        with open(fname, "r") as file:
            word = ""
            while(word := file.readline()):
                prompts.append(word)

        return prompts

    def give_prompt():
        pass
    
    def give_multi_prompt():
        pass