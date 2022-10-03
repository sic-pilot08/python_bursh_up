s = "Hello Text!!! 123 123"
c = [char for char in s if char.isupper()]
d = [char for char in s if char.islower()]
e = [char for char in s if char.isnumeric()]

import re
pattern = re.compile(r'[^a-zA-Z0-9]+')           #Regular_expression
f = pattern.findall(s)
g = [i for i in f[1]]

print(c)
print(d)
print(e)
print(f)