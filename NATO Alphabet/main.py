import pandas

#  How to iterate through Dataframes:
# {new_key:new_value for (index, row) in df.iterrows()}

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_nato = {row.letter:row.code for (index, row) in nato_phonetic.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list_nato_names = [dict_nato[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters from alphabets allowed!")
        generate_phonetic()
    else:
        print(list_nato_names)


generate_phonetic()