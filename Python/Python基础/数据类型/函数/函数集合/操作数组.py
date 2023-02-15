def Ladd(listA, listB):
    result = []
    for eachA in listA:
        result.append(eachA)
        print(result)
    for eachB in listB:
        result.append(eachB)
        print(result)


# range() 函数可创建一个整数列表，一般用在 for 循环中。
numListA = range(8)
numListB = range(8)
Ladd(numListA, numListB)
# print(numListA)
# print(numListB)
