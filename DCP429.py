def makePascalTriangle(iters):
    arr = []
    newArr = []
    if iters == 1:
        arr.append(1)
        return arr
    if iters == 2:
        arr.append(1)
        arr.append(1)
        return arr
    if iters > 2:
        arr.append(1)
        arr.append(1)
        i = 3
        while(i <= iters):
            newArr = []
            for x in range(i - 2):
                newNum = arr[x] + arr[x+1]
                newArr.append(newNum)
            newArr.insert(0, 1)
            newArr.insert(len(newArr), 1)
            arr = newArr
            i += 1
        return newArr

obj = makePascalTriangle(5)
print(obj)