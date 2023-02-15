# 根据key排序
d = {'d1': 2, 'd2': 4, 'd4': 1, 'd3': 3, }
# sorted
for k in sorted(d):
    print(k, d[k])
print()

# 根据value排序 降序
# __getitem__
for k in sorted(d, key=d.__getitem__):
    print(k, d[k])
print()
# 升序
for k in sorted(d, key=d.__getitem__, reverse=True):
    print(k, d[k])
