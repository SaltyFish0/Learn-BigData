import jieba

# lcut和jieba.cut使用方法一样，不过返回的是列表。

seg_list = jieba.lcut("中国上海是一座美丽的国际性大都市", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))


# 精确模式
seg_list = jieba.lcut("中国上海是一座美丽的国际性大都市", cut_all=False)
print("Full Mode: " + "/ ".join(seg_list))
print(seg_list)
print(type(seg_list))
