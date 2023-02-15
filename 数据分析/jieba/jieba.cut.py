import jieba
# jieba.cut
# jieba.cut方法默认是精确模式。
# jieba.cut 给定中文字符串，分解后返回一个迭代器，需要用 for 循环访问。

# join
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# 语法 str.join( 要连接的元素序列。)

# 全模式
seg_list = jieba.cut("中国上海是一座美丽的国际性大都市", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))
# 全模式把句子中所有的可以成词的词语都扫描出来, 会出现一词多用、一词多意。

# 返回结果
# Full Mode: 中国 / 上海 / 是 / 一座 / 美丽 / 的 / 国际 / 国际性 / 大都 / 大都市 / 都市

# 精确模式
seg_list = jieba.cut("中国上海是一座美丽的国际性大都市", cut_all=False)
i = [i for i in seg_list]
print(i)
print("Full Mode: " + "/ ".join(seg_list))

print(type(seg_list))
# 返回结果
# Default Mode: 中国 / 上海 / 是 / 一座 / 美丽 / 的 / 国际性 / 大都市
# 精确模式将句子最精确的切分开，每个词都只有一种含义。
