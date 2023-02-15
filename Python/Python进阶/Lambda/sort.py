# 正常写法
def add(a, b):
    return print(a + b)


add(2, 3)
# lambda定义匿名函数
# 调用lambda函数

# 括号
(lambda a, b: print(a+b))(4, 4)

# 作为参数
lst1 = ['Salty Fish', 'LL', 'Bob', 'Tom', 'alice', 'Jerry', 'Wendy']
lst2 = [5, 9, 3, 4, 5]
# sort
# sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
# list.sort(cmp=None, key=None, reverse=False)

# cmp - - 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key - - 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse - - 排序规则，reverse = True 降序， reverse = False 升序（默认）。

# 该方法没有返回值，但是会对列表的对象进行排序。(会改变原数组)
lst1.sort(key=lambda str: len(str.split()))
print(lst1)
lst2.sort(key=lambda a: -a)
print(lst2)
