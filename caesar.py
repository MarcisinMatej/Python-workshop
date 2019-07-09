"""
In this excercise we will encrypt/decrypt input string with using Caesar cipher.
To do so we will iterate over input string and character by character we will encrypt it.
Other symbols we will ignore like white spaces, interpunction, etc
"""


encrypt_dict={'A':'D', 'B':'E', 'C':'F', 'D':'G', 'E':'H', 'F':'I', 'G':'J', 'H':'K', 'I':'L', 'J':'M', 'K':'N', 'L':'O', 'M':'P', 'N':'Q', 'O':'R', 'P':'S', 'Q':'T', 'R':'U', 'S':'V', 'T':'W', 'U':'X', 'V':'Y', 'W':'Z', 'X':'A', 'Y':'B', 'Z':'C'}

decrypt_dict={'A':'X', 'B':'Y', 'C':'Z', 'D':'A', 'E':'B', 'F':'C', 'G':'D', 'H':'E', 'I':'F', 'J':'G', 'K':'H', 'L':'I', 'M':'J', 'N':'K', 'O':'L', 'P':'M', 'Q':'N', 'R':'O', 'S':'P', 'T':'Q', 'U':'R', 'V':'S', 'W':'T', 'X':'U', 'Y':'V', 'Z':'W'}

# read input word with command input() and store it to variable called in_word

# read command with input() command and store it to variable called in_command

# to make it easier we can capitalize everything with command string_variable.upper() which returns capitalized string

# use if command to determine comand "E" as encrypt, "D" as decrypt
# just compare if they are equal

# prepare output variable which we will return -> empty string

# depending on command use specific dictionary
# iterate over each character in in_word with for i in my_string: command

# check if character is encryptable. We will use only characters, so we need to check if 
# character is propper char. To do so we can use my_string.isalpha()

# encrypt/decrypt single character

# add it to our output variable

# print output variable
