a = 10
b = 20
c = 30
if a > b:
    max = a
else:
    max = b
# 使用 if else 实现三目运算符（条件运算符）的格式如下：
# exp1 if contion else exp2
max = a if a > b else b
print(max)
# condition 是判断条件，exp1 和 exp2 是两个表达式。如果 condition 成立（结果为真），就执行 exp1，并把 exp1 的结果作为整个表达式的结果；如果 condition 不成立（结果为假），就执行 exp2，并把 exp2 的结果作为整个表达式的结果。
# 前面的语句max = a if a > b else b的含义是：
# 如果 a > b 成立，就把 a 作为整个表达式的值，并赋给变量 max；
# 如果 a > b 不成立，就把 b 作为整个表达式的值，并赋给变量 max。

# 嵌套写法
max = a if a > b and a > c else b if b > a and b > c else c
print(max)
