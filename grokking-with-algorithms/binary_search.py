def binary_search(list, searched_item):
    low = 0
    high = len(list) - 1

    while low <= high:
        # the floor division // rounds the result down to the nearest whole number
        mid = (low + high) // 2
        guess = list[mid]
        if guess == searched_item:
            return mid
        elif guess > searched_item:
            high = mid + 1
        else:
            low = mid + 1

    return None


print(binary_search([1, 2, 3, 4, 5, 6], 3))
