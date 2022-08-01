'''
Palindrome is a word or phase that reads the same forwards as backwards
'''

def is_palindrome(word):
    # return keyword return wither true or false where as [::-1] reverse the insert words
    return word == word[::-1]


word = input("Enter any word: ")
check = is_palindrome(word)


print(check)