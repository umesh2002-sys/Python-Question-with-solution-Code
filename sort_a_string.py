'''
Challange
writing python function to short the words in a string 

input:
string of words, sepratrd by space

output:
string of words, sorted alphabetically
'''

def sort_words(input):
    return ' '.join(shorted(input.split(), key = str.lower))