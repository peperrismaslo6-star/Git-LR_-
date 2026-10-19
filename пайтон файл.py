#задание 2-мат логика
print('x y z w  f')
for x in (0,1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (w and ((y<=x)<=z))==0:
                    print(x,y,z,w,' 0')
#задание 5 составление алгоритма
def f(n):
    s=''
    while n>0:
        s=str(n%5)+s
        n//=5
    return s
def g(x):
    x5=f(x)
    if x5[-1] in '024':
        x5+='2'
    else:
        x5='2'+x5+'3'
    r=int(x5,5)
    return r
for n in range(100000,0,-1):
    if g(n)<1000:
        print(n)
        break