from sys import setrecursionlimit

numberOfRecursions = 0

def isEven(num):
    global numberOfRecursions

    if isEqual(num, 0):
        return True
    elif isEqual(num, 1):
        return False
    else:
        numberOfRecursions += 1
        return isEven(num - 2)

def isOdd(num):
    global numberOfRecursions

    if isEqual(num, 0):
        return False
    elif isEqual(num, 1):
        return True
    else:
        numberOfRecursions += 1
        return isOdd(num - 2)

def linearSearch(inputList, inputValue, i=0):
    global numberOfRecursions

    if isEqual(inputList[0], inputValue):
        out = i
        i = 0
        return out
    else:
        if isEqual(length(inputList), 1):
            i = 0
            return -1
        else:
            i += 1
            numberOfRecursions += 1
            return linearSearch(inputList[1:], inputValue)

def binarySearch(inputList, inputValue, iStart=0):
    global numberOfRecursions

    start = 0
    end = (start + length(inputList)) - 1
    middle = (start + end) // 2

    iEnd = (iStart + length(inputList)) - 1
    iMiddle = (iStart + iEnd) // 2

    if isEqual(inputList[middle], inputValue):
        return iMiddle
    else:
        if isEqual(length(inputList), 1):
            return -1

        numberOfRecursions += 1

        if isEqual(maximum(inputList[middle], inputValue), inputList[middle]):  
            return binarySearch(inputList[:middle], inputValue, iStart)
        elif isEqual(maximum(inputList[middle], inputValue), inputValue):
            return binarySearch(inputList[middle + 1:], inputValue, iMiddle+1)

def length(iterable, c=0):
    global numberOfRecursions

    try:
        iterable[0]
    except IndexError:
        return 0

    try:
        iterable[1]
    except IndexError:
        return 1

    numberOfRecursions += 1
    return c + length(iterable[1:], c) + 1

def maximum(numA, numB):
    global numberOfRecursions

    if isEqual(numA, 0) and not isEqual(numB, 0):
        return numB
    elif not isEqual(numA, 0) and isEqual(numB, 0):
        return numA
    elif isEqual(numA, 0) and isEqual(numB, 0):
        return numA
    else:
        numberOfRecursions += 1
        return maximum(numA - 1, numB - 1) + 1

def minimum(numA, numB):
    global numberOfRecursions

    if isEqual(numA, 0) and not isEqual(numB, 0):
        return numA
    elif not isEqual(numA, 0) and isEqual(numB, 0):
        return numB
    elif isEqual(numA, 0) and isEqual(numB, 0):
        return numA
    else:
        numberOfRecursions += 1
        return minimum(numA - 1, numB - 1) + 1

def isEqual(numA, numB):
    global numberOfRecursions

    if numA == 0 and numB == 0:
        return True
    elif (numA == 0 and numB != 0) or (numA != 0 and numB == 0):
        return False
    else:
        numberOfRecursions += 1
        return isEqual(numA - 1, numB - 1)

def sumList(inputList):
    global numberOfRecursions

    try:
        inputList[0]
    except IndexError:
        return 0

    numberOfRecursions += 1
    return inputList[0] + sumList(inputList[1:])

def rangeBetween(start, end, step=1, out=[]):
    global numberOfRecursions

    out.append(start)

    if isEqual(start, end):
        return out
    else:
        numberOfRecursions += 1
        return rangeBetween(start+step, end, step, out)