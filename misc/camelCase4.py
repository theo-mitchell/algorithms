'''
Camel Case is a naming style common in many programming languages. 
In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). 
Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format:

Each line of the input file will begin with an operation (S or C). 
Then followed by a semi-colon, followed by M, C, or V, followed by a semi-colon followed by the words you'll need to operate on.
The operation will either be S (split) or C (combine)
M indicates method, C indicates class, and V indicates variable
In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. 
Methods should end with an empty set of parentheses to differentiate them from variable names.


Output Format:

For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).

'''

import sys
import re

def splitInput(inputType, inputString):
    result = re.split('(?=[A-Z])', inputString)
    
    result = [word.lower() for word in result]
    
    if inputType == 'C': result = result[1:]
    
    return ' '.join(result).strip('()')

def combineInput(inputType, inputString):
    result = ''
    
    for index, word in enumerate(inputString.split(' ')):
        result += word.capitalize()
    
    if inputType != 'C': result = result[0].lower() + result[1:]
    if inputType == 'M': result = result + "()"
    
    return result
    
    

def main():
    for line in sys.stdin:
        line = line.rstrip('\r\n')
        operation, inputType, inputString = line.split(';')
        
        if operation == 'S':
            print(splitInput(inputType, inputString))
        else:
            print(combineInput(inputType, inputString))
main()