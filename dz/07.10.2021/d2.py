import re

s = "google.com and google.ru"
reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
print(re.sub(reg, r'http://\1', s))