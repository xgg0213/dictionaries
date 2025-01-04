# Given two lists, `lst1` and `lst2`, write a function `merge_lists` that merges
# them into a dictionary where the `lst1` represents a list of the keys and
# `lst2` represents a list of the values. Assume the lists are of the same
# length.

# Write your code here.
def merge_lists(ls1,ls2):
    return {k:v for k,v in zip(ls1, ls2)}
    # return list(zip(ls1, ls2))

lst1 = ['a', 'b']
lst2 = [1, 2]
merged_dict = merge_lists(lst1, lst2)
print(merged_dict)      # { 'a': 1, 'b': 2 }