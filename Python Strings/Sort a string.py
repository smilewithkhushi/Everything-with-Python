'''
ADVANCED PYTHON 

Ques : Write a python function to sort the words in a string
input : string of words, seperated by spaces
output : string of words, sorted alphabetically
Example input : string of words
example output : of string words

'''

def sortAString(words):
    return ''.join(sorted(words.split(), key=str.casefold))

words=input("Enter a string to sort it : ")
result = sortAString(words)
print(result)