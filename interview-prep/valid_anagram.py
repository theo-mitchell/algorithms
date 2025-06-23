# Problem: Valid Anagram
# Check if two strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of another,
# such as "listen" and "silent".
# Ignore casing and assume only alphabetical characters.
# You may solve this by either sorting or counting letters.

def is_anagram(str1: str, str2: str) -> bool:
    return ''.join(sorted(str1.lower())) == ''.join(sorted(str2.lower()))

# Test cases
print(is_anagram("listen", "silent"))      # Correct output: True
print(is_anagram("Triangle", "Integral"))  # Correct output: True
print(is_anagram("apple", "pale"))         # Correct output: False
print(is_anagram("aabbcc", "abcabc"))      # Correct output: True
print(is_anagram("rat", "car"))            # Correct output: False
