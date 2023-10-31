#readlines(): https://www.w3schools.com/python/ref_file_readlines.asp
#replace(): https://www.w3schools.com/python/ref_string_replace.asp
#strip(): https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt') as file:
    text = file.read()

with open('./Input/Names/invited_names.txt', "r") as file:
    name_list = file.readlines()

for i in name_list:
    name = i.strip("\n")
    final_text = text.replace("[name]", name)
    with open(f'./Output/ReadyToSend/Letter_for_{name}.txt', "w") as file:
        file.write(final_text)
