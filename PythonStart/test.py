a = 1
b = 1.2
c = b

print(id(a), id(1), id(b), id(c))  # 주소값
print(a is b, a == b)  # false
print(b is c, b == c)  # true