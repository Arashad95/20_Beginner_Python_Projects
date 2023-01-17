'''
have a python dictionary that has a key/value pair that requests a word and its definition
collect input from the user, import is a word 
check if the word is in the dictionary 
print the definition
'''

from PyDictionary import PyDictionary

dictionary = PyDictionary()

# def main():
#     word_dictionary = {
#         'hi': 'a way of greeting',
#         'eyes': 'an organ for seeing',
#         'earth': 'a planet in space'
#     }

#     while True:
#         word = input("Enter a word: ")

#         if word == "":
#             break
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])
# main()

while True:

    word = input("Enter your word: ")
    if word == "":
        break

    print(dictionary.meaning(word))
