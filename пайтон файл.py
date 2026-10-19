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