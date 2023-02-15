a = input('第一位数：')
a = int(a)

c = input('运算符：')

b = input('第二位数：')
b = int(b)
if c == "+":
    print('a + b =', a+b)
elif c == "-":
    print('a - b =', a-b)
elif c == "*":
    print('a × b =', a*b)
elif c == "/":
    if b == 0:
        print("除数不能为0！")
    else:
        print('a ÷ b =', a/b)
else:
    print("请输入正确运算符！")
print('程序结束.')
