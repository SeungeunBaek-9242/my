"""
변수선언
주소값 확인
값일치 확인
"""

a = 1
b = 1.2
c = b

print(id(a), id(1), id(b), id(c))  # 주소값
print(a is b, a == b)  # False False
print(b is c, b == c)  # True True


import sys
sys.path.append("/home")
print(sys.path)