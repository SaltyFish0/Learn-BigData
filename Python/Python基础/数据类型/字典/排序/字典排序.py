x = {'x': 20, 'a': 12, 'b': 5}
# 按值降序排列
y2 = {k: v for k, v in sorted(
    x.items(), key=lambda item: item[1], reverse=True)}
print(y2)
