# compile
# compile编译正则表达式

import re
message = 'SaltyFish呜呼呼~'
reRule = re.compile(r'[A-z]*')
print(re.search(reRule, message).group())
