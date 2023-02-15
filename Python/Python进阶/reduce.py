from functools import reduce

# reduce
# Reduce语法： reduce（function,sequence[,initial]
# 根据传入的函数式子，按数列从左到右的顺序，不断迭代两个参数的累积值，直到最终输出"单一值"作为结果。
# function：有两个参数的额函数，           必需参数
# sequence: 元组、列表等可迭代对象，  必需参数
# inital： 初始值，                                     可选参数
print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))  # 阶乘操作
# 工作过程
# 首先把 前两个元素传给 函数参数，函数加工后，
# 然后把得到的结果和第三个元素作为两个参数传给函数参数，
# 函数加工后得到的结果又和第四个元素作为两个参数传给函数参数，依次类推
# 1*2
# (1*2)*3
# ((1*2)*3) * 4
# 如果传入了 initial 值， 那么首先传的就不是 sequence 的第一个和第二个元素，而是 initial值和 第一个元素。
print(reduce(lambda x, y: x*y, [1, 2, 3, 4], 4))  # 阶乘操作
# 1*4
# (1*4) *2
# ((1*4) *2)*3
# (((1*4) *2)*3) * 4
# 累计、迭代运算：lambda + reduce

# 把一个整数列表拼成整数
intList = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x*10+y, intList))
# 1*10+2
# 12*10 + 3
# 123*10 +4
# 1234*10 +5
# 12345


# 进阶
# https://blog.csdn.net/bailixuance/article/details/85098215
