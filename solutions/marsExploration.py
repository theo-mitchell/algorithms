'''
A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.


Letters in some of the SOS messages are altered by cosmic radiation during transmission. 

Given the signal received by Earth as a string,s , determine how many letters of the SOS message have been changed by radiation.

Example:

s = 'SOSTOT'

The original message was SOSSOS. Two of the message's characters were changed in transit.

Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

string s: the string as received on Earth
Returns

int: the number of letters changed during transmission

'''

def marsExploration(s):
    acceptableLetters = ['S', 'O', 'S']
    changedLettersCount = 0
    

    for index, letter in enumerate(s):
        if letter != acceptableLetters[index % 3]:
            changedLettersCount += 1
        
    return changedLettersCount