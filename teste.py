a = 10
b = -7 
c = 67
if a < b:
    d = a
    a = b
    b = d
if a < c:
    d = a
    a = c
    c = d
if b < c:
    d = b
    b = c
    c = d
print (f"{a},  {b},{c}")