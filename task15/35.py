for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        f = (x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0))
        if not f:
            is_a = False
            break
    if is_a:
        print(a)


for a in range(1, 1000):
    if all((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) for x in range(1, 1000)):
        print(a)
