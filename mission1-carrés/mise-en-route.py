c = 0
for a in range(1, 11):
    b = a ** 2
    c = c + b
    d = a * (a+1) * (2*a+1)/6
    print(a, "\t", b, "\t", c, "\t", int(d))
