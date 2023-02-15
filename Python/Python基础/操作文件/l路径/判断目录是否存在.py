import os
# 判断目录是否存在
fpath = os.path.exists('d:\\pylianxi\\')
if fpath == False:
    # 如目录不存在则创建目录
    os.makedirs("d:\\pylianxi\\")
