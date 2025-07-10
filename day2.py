# #string data types
# #list and tuples
# #conditionals

# # slicing
# name = 'Anoj'
# name[0:3]
# print(name[0:3])
# remove = name[3:]
# print(remove)

# #length

# print(len(name))

# #find and replace

# print(name.find('A'))
# replaced = name.replace('A', 'B')
# print(replaced)

# #escapesequence characters
# text = "My name is ...milan....\n  \'here\' and \n i am learning python"
# print(text) 

#write a program to detect double spaces in a string
text = "This  is  a  sample  text  with  double  spaces."

def detect_double_spaces(text):
    if '  ' in text:
        print("Double spaces detected.")
    else:
        print("No double spaces detected.")

detect_double_spaces(text)


#replace the double spaces from problem 3 with single space
def replace_double_spaces(text):
    return text.replace('  ', ' ')

text = replace_double_spaces(text)
print(text)
#write a program to format the following letters using escape sequence characters
letter = "Dear students, this python course is going well. Thanks!"
letter = "Dear students,\n\tThis Python course is going well.\nThanks!"
print(letter)






