import os
import re
path = os.path.split(os.path.realpath(__file__))[0] + "\\"+"tieba.csv"
ReadFile = open(path, 'r', encoding='utf-8', newline="")
text = re.sub('[,，]', ' | ', ReadFile.read())
print(text)
ReadFile.close()
