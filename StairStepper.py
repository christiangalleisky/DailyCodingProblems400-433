from itertools import permutations
'''
x = permutations('012')
for i in x:
    print(i)
'''
def makeStringArray(stairs):
    n = stairs // 2
    odd = stairs % 2
    arr = [[]]
    i = 0
    if odd:
        string = ('2' * n) + '1'
    else:
        string = ('2' * n)
    arr[i] = string
    i += 1
    while i <= n:
        if odd:
            arr.append(('2' * (n-i)) + ('1' * (i * 2)) + '1')
        else:
            arr.append(('2' * (n - i)) + ('1' * (i * 2)))
        i += 1
    return arr

def makePermutations(list):
    toBeReturned = []
    i = 0
    while i < len(list):
        string = list[i]
        perms = permutations(string)
        for x in perms:
            if x not in toBeReturned:
                toBeReturned.append(x)
        i += 1
    return toBeReturned

lists = makeStringArray(4)
print(lists)
perms = makePermutations(lists)
print(perms)