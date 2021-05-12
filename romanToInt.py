def romanToInt(s: str) -> int:
    mapping = {
                'I': 1, 
                'V': 5, 
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                'IV': 4,
                'IX': 9,
                'XL': 40,
                'XC': 90,
                'CD': 400,
                'CM': 900
            }

    sum = 0
    i = 0

    while i < len(s):
        currentLetter = s[i]
        if i + 1 < len(s):
            nextLetter = s[i + 1]
        else:
            nextLetter = '$'

        if mapping.get(currentLetter + nextLetter):
            sum += mapping.get(currentLetter + nextLetter)
            # Since we added the value for two letters, next iteration should be skipped
            i += 2
        else:
            sum += mapping.get(currentLetter)
            i += 1
    return sum

print(romanToInt("MCMXCIV"))
