#задание 2-мат логика
print('x y z w  f')
for x in (0,1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (w and ((y<=x)<=z))==0:
                    print(x,y,z,w,' 0')