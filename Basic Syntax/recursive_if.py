b = 0
c = 0
d = 0
threshold = 4
while c < 10:
    a = b
    print(a, end=' ')
    
    if c <= threshold:
        b = c
        print(b, end=' ')
        c += 1
        print(c)
    else:
        b += d
        print(b, end=' ')
        d += b
        print(d)
        c += 1
        
    d = c - threshold
    