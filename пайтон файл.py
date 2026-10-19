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

#задание 13 IP адреса
from ipaddress import ip_network

k=0
net=ip_network('123.222.111.192/255.255.255.248',0)
for n in net:
    d=bin(int(n))[2:].zfill(32)
    if d[24:].count('0')%3!=0:
        k+=1
print(k)

#задание 14 системы счисления
for x in '0123456789abcdefghijk':
    a=int(f'82934{x}2',21)
    b=int(f'2924{x}{x}7',21)
    c=int(f'67564{x}8',21)
    if (a+b+c)%20==0:
        print((a+b+c)//20)
        break

print('А теперь самый сок')
#задание 24 работа со строками
s=open('242.txt').readline()
for c in '02468':s=s.replace(c,'2')
ks=m=l=0
for r in range(len(s)):
    if s[r]=='S':ks+=1
    if s[r]=='2':
        ks=0
        l=r
    if ks==31 and s[l]=='2':
        m=max(m,r-l+1)
print(m)

#задание 27
from math import dist

n=3
cl={1:[],2:[],3:[]}
for s in open('27'):
    s=s.replace(',','.')
    x,y,har=s.split()
    x,y=float(x),float(y)
    if y>23:
        cl[1]+=[[x,y,har]]
    elif x>20:
        cl[2]+=[[x,y,har]]
    elif x<20 and y<23:
        cl[3]+=[[x,y,har]]
for i in cl:
    print(i,len(cl[i]),cl[i])
def centr(cl):
    res=(0,0)
    su=10**10
    for a in cl:
        sua=0
        for b in cl:

            sua+=dist(a[:2],b[:2])
        if sua<su:
            res=a
            su=sua
    return res

cl18=[p for p in cl[1] if p[2]!='VII' and int(p[2][1])>=8 ]
cl28=[p for p in cl[2] if p[2]!='VII' and int(p[2][1])>=8]
cl38=[p for p in cl[3] if p[2]!='VII' and int(p[2][1])>=8]

b1=min([dist(p1[:2],p2[:2]) for p1 in cl18 for p2 in cl28]+
       [dist(p1[:2],p2[:2]) for p1 in cl28 for p2 in cl38]+
       [dist(p1[:2],p2[:2]) for p1 in cl18 for p2 in cl38])

f=([dist(p1[:2],p2[:2]) for p1 in cl18 for p2 in cl18 if p1!=p2]+
   [dist(p1[:2],p2[:2]) for p1 in cl28 for p2 in cl28 if p1!=p2]+
   [dist(p1[:2],p2[:2]) for p1 in cl38 for p2 in cl38 if p1!=p2])
b2=sum(f)/len(f)
print(int(b1*10000),int(b2*10000))
