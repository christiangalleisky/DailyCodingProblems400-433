def functionOne(x):
    binNumOne = bin(x)
    onesOne = countOnes(binNumOne)
    i = 1
    while True:
        binNumTwo = bin(x+i)
        onesTwo = countOnes(binNumTwo)
        if onesTwo == onesOne:
            break
        i += 1
    return int(x+i)

def countOnes(x):
    i = 0
    for y in range(2, len(x)):
        if x[y] == '1':
            i += 1
    return i

x = 9
obj = functionOne(x)
print(obj)
print(bin(x))
print(bin(obj))


