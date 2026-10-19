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
        
#задание 6 Черепашка
from turtle import *
left(90)
tracer(-1)
k=18
down()
for i in range(7):
    fd(20*k)
    rt(240)
    fd(10*k)
    rt(240)
    fd(20*k)
    rt(120)
    fd(10*k)
    rt(120)
up()
for x in range(-10,10):
    for y in range(21):
        goto(x*k,y*k)
        dot(3,'red')
done()

#задание 8 комбинаторика
from itertools import product

k=0
for i in product('0123456789abcdef',repeat=5):
    x=''.join(i)
    if x[0]!='0' and x.count('6')==2 and all(a+'6'not in x for a in '02468ace') and all('6'+a not in x for a in '02468ace'):
        k+=1
        print(x,k)

#задание 9 работа с таблицей
s=0
for d in open('9a'):
    a=[int(n) for n in d.split()]
    a2=[n for n in a if a.count(n)==2]
    a1=[n for n in a if a.count(n)==1]
    if len(a2)==4 and len(a1)==3 and max(a) in a1:
        s=sum(a)
        print(a,s)
        break

#задание 11 инф объем фото, видео, звука
from math import log2, ceil

for a in range(100000,0,-1):
    bit=ceil(log2(a))
    bat=ceil(bit*23/8)
    if bat*500000<=21*1024*1024:
        print(a)
        break