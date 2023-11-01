import pandas

#  How to iterate through Dataframes:
# {new_key:new_value for (index, row) in df.iterrows()}

word = input("Enter a word: ")
list_word = list(word.upper())

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_nato = {row.letter:row.code for (index, row) in nato_phonetic.iterrows()}

list_nato_names = [dict_nato[letter] for letter in list_word if letter in dict_nato]
print(list_nato_names)