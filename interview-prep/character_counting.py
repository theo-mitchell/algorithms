# String counting: Write a function to count occurrences of each character in a string
# In this example I am considerting empty space to be a character
# I am also ignoring character casing.

from typing import Dict


def character_occurrences(some_string: str) -> Dict:
    occurrences = {}

    for character in some_string:
        if character not in occurrences:
            occurrences[character] = 1
        else:
            occurrences[character] = occurrences[character] + 1

    return occurrences


print(character_occurrences("oh no? oh my"))
print(character_occurrences("this  Is A test 112!"))
