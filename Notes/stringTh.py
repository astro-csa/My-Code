#String theory

#To define a string, "" or '' are needed
text = 'Hello world'

#Strings are arrays of characters, and as an array, the elements of it can be acessed with []
print("The fifth letter of Text is:", text[4])

#Strings are immutable: text[0] = "D" would create an error.

#String's type is 'str'
print("The string's type is ", type(text))

#Strings can be converted to lower or upper case
print("Lower case: ", text.lower())
print("Upper case: ", text.upper())

#Strings can be summed
text1 = "Hello"
text2 = "World"
text = text1 + " " + text2
print("text: ", text)