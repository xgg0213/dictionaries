# Given a string, write a function that returns the character that is the
# majority of the string. If there is no majority character, return None. A
# majority is considered as having more than `n / 2` instances where `n` is the
# length of the string.

# Write your code here.
def majority_char(str):
    results={}
    for n in list(str):
        if n in results:
            results[n]+=1
        else:
            results[n]=1
    return [k for k,v in results.items() if v>=len(str)/2]

str = 'all'
str2 = 'welcome to the jungle'
str3 = 'aaa'

print(majority_char(str))           # 'l'
print(majority_char(str2))          # None
print(majority_char(str3))