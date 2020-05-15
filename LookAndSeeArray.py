def makeNumber(string):
    print(string)
    nums = []
    for i in range(len(string)):
        nums.append(int(string[i]))
    return nums

def makeArray(nIterations):
    i = 0
    finalArr = []
    string = ""
    while i < nIterations:
        if(i == 0):
            finalArr.append([1])
        elif(i == 1):
            finalArr.append([1,1])
        else:
            x = 0
            count = 1
            string = ""
            while x < (len(finalArr[i-1]) - 1):
                if finalArr[i-1][x] == finalArr[i-1][x+1]:
                    count += 1
                else:
                    type = finalArr[i-1][x]
                    string += str(count) + str(type)
                    count = 1
                x += 1
                if x == (len(finalArr[i-1]) - 1):
                    type = finalArr[i - 1][x]
                    string += str(count) + str(type)
                    count = 1
                    string = makeNumber(string)
                    finalArr.append(string)

        i += 1
    return finalArr


its = 5
output = makeArray(its)
print(output)