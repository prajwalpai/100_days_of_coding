#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read Invitee Names
with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

print(names_list)
# Read Starting Letter
letter = open("Input/Letters/starting_letter.txt", 'r')
Lines = letter.readlines()

# Create custom contents and write
for invitee in names_list:
    invitee = invitee.strip('\n')
    filename = "Output/ReadyToSend/letter_for_"+invitee+".txt"
    invitation_letter = open(filename, mode='a')
    for line in Lines:
        line = line.replace("[name]", invitee)
        invitation_letter.writelines(line)




# Write the custom contents into induvidual files