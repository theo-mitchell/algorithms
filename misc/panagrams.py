'''
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. 
Ignore case. Return either 'pangram' or 'not pangram' as appropriate.
'''

import string

def pangrams(s):
    alphabetList = list(string.ascii_lowercase)
    s = s.lower()
    
    for letter in s:
        if letter in alphabetList:
            alphabetList.remove(letter)
            
    if alphabetList == []:
        return 'pangram'
    else:
        return 'not pangram'