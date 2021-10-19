def squares(a, b):
    c=0
    x=int(m.sqrt(a))
    while x<=m.sqrt(b):
        if pow(x,2)>=a and pow(x,2)<=b:                                 """hackerrank"""
            c+=1
        x+=1
    return c
