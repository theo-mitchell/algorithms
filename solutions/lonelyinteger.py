'''
Given an array of integers, where all elements but one occur twice, find the unique element.

Function Description

lonelyinteger has the following parameter(s):

int a[n]: an array of integers

'''


def lonelyinteger(a):
    # dictreference = {}
    # for index, number in enumerate(a):
    #     if number in dictreference:
    #         dictreference[number] += 1
    #     else:
    #         dictreference[number] = 1
            
    # for key, value in dictreference.items():
    #      if value == 1:
    #          return key

    for value in a:
        if a.count(value) == 1:
            return value