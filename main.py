#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Opening The Template Letter
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_temp:
    all_lines = letter_temp.read()

# Opening the Names file
with open("./Input/Names/invited_names.txt", mode="r") as names:
    all_names = names.readlines()
    for name in all_names:
        stripped_name = name.strip()

        # Replacing the names
        final_letter = all_lines.replace("[name]", stripped_name)

        # Creating the new file for each Person
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as letter:
            letter.write(final_letter)

