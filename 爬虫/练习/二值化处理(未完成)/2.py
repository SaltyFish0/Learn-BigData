

# -*- coding: utf-8 -*-
# author：baoshan

from PIL import Image, ImageFilter

codeLib = '''@#$%&?*aeoc=<{[(/l|!-_:;,."'^~` '''
count = len(codeLib)
print(count)


def trans_photo(image_file):
    # 将彩色图片转化为黑白的图片
    image_file = image_file.convert("L")
    codePic = ''
    # 循环图片的宽高，并得到每一像素的灰度值
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            gray = image_file.getpixel((w, h))
            # 将对应的灰度值映射到字符
            codePic = codePic + codeLib[int(((count) * gray) / 256)]
        # 实现每行结尾处自动换行
        codePic = codePic + '\r\n'
    return codePic


def main():
    filename = '114x156.jpg'
    fp = open(filename, 'rb')
    image_file = Image.open(fp)

    image_file = image_file.resize(
        (int(image_file.size[0] / 2), int(image_file.size[1] / 4)))

    tmp = open('w2.txt', 'w')
    tmp.write(trans_photo(image_file))
    tmp.close()


if __name__ == '__main__':
    main()
