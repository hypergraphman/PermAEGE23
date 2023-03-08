print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
                    print(x, y, z, w)