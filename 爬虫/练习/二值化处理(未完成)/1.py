from PIL import Image
import pytesseract
import os
path = os.path.split(os.path.realpath(__file__))[
    0] + "\\"+"9ee33a79851544cdae1e6978a8161f60.004.png"
image = Image.open(path)
imgry = image.convert('L')
imgry.show()

threshold = 140
def table(x): return 0 if x < threshold else 1


out = imgry.point(table, '1')
out.show()
code = pytesseract.image_to_string(out)
print(out)
code = pytesseract.image_to_string(imgry)
print(code)
input()
