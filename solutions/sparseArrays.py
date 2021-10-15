'''

Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings
Returns

int[q]: an array of results for each query

'''

def matchingStrings(strings, queries):
    results = []
    
    for index, query in enumerate(queries):
        results.append(0)
        for string in strings:
            if string == query:
                results[index] += 1
    
    return results