score = input('请输入你的成绩： ')
score = int(score)
if(score > 100 or score < 0):
    print('请输入正确分数！')
else:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print("不及格")
print("程序结束")
