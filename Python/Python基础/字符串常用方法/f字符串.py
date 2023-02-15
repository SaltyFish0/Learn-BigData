from unicodedata import name


name = '陈海旺'
age = 23

# Python 3.0
print('{} is {} years old'.format(name, age))

# Python 3.6
print(f'我是你大爸{name}')

# 也可以将表达式放在括号之间
bags = 3
apples_in_bag = 12
print(f'There are total of {bags * apples_in_bag} apples')
