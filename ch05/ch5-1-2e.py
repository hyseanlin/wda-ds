import re

str1 = "促銷價: $128.95"
match = re.findall(r"[0-9]+\.*[0-9]*", str1)
if match:
    print(match[0])
else:
    print("沒有找到符合的字串!")


