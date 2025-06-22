# First unique character: Find the first non-repeated character in a string
# For this example casing is ignored
# Space (' ') is NOT considered to be a character


def first_unique_character(some_string: str) -> str | None:
    counts = {}
    some_string = some_string.lower()

    for character in some_string:
        if not character == ' ':
            if character not in counts:
                counts[character] = 1
            else:
                counts[character] = counts[character] + 1

    for entry in counts:
        if counts[entry] == 1:
            return entry

    return None



print(first_unique_character("wolo lolo1"))
print(first_unique_character("1112223344 oOjjj!!w"))
print(first_unique_character("112233  44AaBb"))

