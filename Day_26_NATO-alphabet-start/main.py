import pandas as pd

phonetic_data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {v.letter:v.code for k,v in phonetic_data.iterrows()}

phonetic_list = []
while len(phonetic_list) == 0:
    try:
        input_word = input('Enter a word : ')
        phonetic_list = [phonetic_dict[alp.upper()] for alp in input_word]
        print(phonetic_list)
    except KeyError:
        print("Sorry, only letters in the alphabet pls")

