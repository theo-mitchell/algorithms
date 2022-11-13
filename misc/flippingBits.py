'''

You will be given a list of 32 bit unsigned integers. 
Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.

Function Description:

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns

int: the unsigned decimal integer result

'''


def flippingBits(n):
    n  = list('{:032b}'.format(n))
    
    for index, value in enumerate(n):
        n[index] = (int(value) + 1) % 2
    
    n = "".join(map(str, n))
    
    return int(n,2)