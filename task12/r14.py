for x in range(0, 93 + 1):
    for y in range(0, 26 + 1):
        for z in range(0, 26 + 1):
            if 2 * x + 3 * y + 6 * z == 186 and y + z == 26:
                print(x, y, z)
                print(x + y + z + 2)