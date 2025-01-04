# Given a list, `lst` of dictionaries, write a function,
# `concatenate_dictionaries` that concatenates the contents of each dictionary
# into a single dictionary. If multiple dictionaries share the same key, use the
# value of the higher indexed dictionary in the list.

# Write your code here.
def concatenate_dictionaries(lst):
    results={}
    for d in lst:
        results.update(d)
    return results

lst = [
    {
        'a': 'this',
        'b': 'is'
    },
    {
        'c': 'the',
        'd': 'merged'
    },
    {
        'd': 'dictionary'
    }
]

print(concatenate_dictionaries(lst))
"""
Prints: 
{
    'a': 'this',
    'b': 'is',
    'c': 'the',
    'd': 'dictionary'
}
"""