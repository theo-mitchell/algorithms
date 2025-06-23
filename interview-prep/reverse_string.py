# Problem: Reverse String In-Place
# Reverse the characters of a string **in-place**.
# You may assume the input is a mutable list of characters (not a Python string, which is immutable).
# Example: ['h', 'e', 'l', 'l', 'o'] becomes ['o', 'l', 'l', 'e', 'h']


def reverse_string(char_list: list[str]) -> None:
    min_index = 0
    max_index = len(char_list) - 1

    while min_index < max_index:
        left = char_list[min_index]
        right = char_list[max_index]

        char_list[min_index] = right
        char_list[max_index] = left

        min_index += 1
        max_index -= 1

    return char_list


# Test cases for reverse_string (in-place)

print_result = lambda x: (reverse_string(x), print(x))  # utility to reverse and print

# Even-length word
print_result(["h", "e", "l", "l", "o"])  # Correct output: ['o', 'l', 'l', 'e', 'h']

# Palindrome word (same forwards and backwards)
print_result(
    ["H", "a", "n", "n", "a", "h"]
)  # Correct output: ['h', 'a', 'n', 'n', 'a', 'H']

# Single character
print_result(["A"])  # Correct output: ['A']

# Empty list
print_result([])  # Correct output: []

# Numbers and letters
print_result(["1", "2", "a", "b"])  # Correct output: ['b', 'a', '2', '1']

# Mixed casing
print_result(["T", "e", "S", "t"])  # Correct output: ['t', 'S', 'e', 'T']

# Symbols
print_result(["!", "@", "#", "$"])  # Correct output: ['$', '#', '@', '!']

# Whitespace
print_result(["a", " ", "b"])  # Correct output: ['b', ' ', 'a']
