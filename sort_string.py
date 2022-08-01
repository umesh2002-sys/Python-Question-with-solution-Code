'''
Challange
writing python function to short the words in a string 

input:
string of words, sepratrd by space

output:
string of words, sorted alphabetically
'''

def sort_words(input):
    return ' '.join(sorted(input.split(), key = str.lower))

'''
Output:
>>> sort_words('Ansih alsiha AnIsha Pramish Umesh') #user input 
'alsiha AnIsha Ansih Pramish Umesh'
'''