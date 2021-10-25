a = 30
b = 23
c = 89
d = c + a
f = c - b
while True:
    a = a + 1
    b = b + 1
    c = c + a
    print(c)
    c = c - b
    if c > 1501:
        break