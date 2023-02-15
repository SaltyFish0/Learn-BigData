string1 = 'Python1'
string2 = "Python2"

# 三引号可无限换行，上下有换行符
string3 = '''
Python3
Python4
'''
print(string3)

# 字符串执行操作
string1 + string2  # 合并字符串
string1 * 3  # 重复字符串(复制)
int('9')  # 将字符串转换为数值

# 字符串索引及切片操作
print(string1)
print(string1[0])  # 正序索引，序号从0开始
print(string1[-1])  # 逆序索引，序号从-1开始
print(string1[1:3])  # 切片操作，左闭右开 yt(不包括3)
print(string1[:5])  # 从0开始取，到第五个元素(不包括5) Pytho
print(string1[3:])  # 从3开始取，到最后一个值 hon1
print(string1[:-5])  # 从0开始取，到第副五个元素(不包括-5) Py
print(string1[1:-3])  # yth
# 只要记住后面的式子就好了：[start_index: stop_index: step]
# start_index是切片的起始位置
# stop_index是切片的结束位置（不包括）
# step可以不提供，默认值是1，步长值不能为0，不然会报错ValueError
