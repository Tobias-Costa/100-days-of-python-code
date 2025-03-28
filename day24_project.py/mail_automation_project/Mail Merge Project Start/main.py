#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_model:
    letter_content = letter_model.read()

    for name in names_list:

        stripped_name = name.strip("\n")
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        formated_name = stripped_name.lower().replace(' ', '_')

        with open(f"./Output/ReadyToSend/letter_for_{formated_name}", "w") as letters_folder:
            letters_folder.write(new_letter)