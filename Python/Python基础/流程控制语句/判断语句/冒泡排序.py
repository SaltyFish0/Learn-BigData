vec = [1, 2, 6, 0, 0.5, -1, 2.4]

# 编写嵌套循环
for i in range(len(vec)):
    for j in range(i):
        if vec[j] > vec[i]:
            vec[j], vec[i] = vec[i], vec[j]  # 调换元素位置
print(vec)
