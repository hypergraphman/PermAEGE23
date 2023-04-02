for a in range(-100, 100):
    if all((y + 3 * x < a) or (2 * y + x > 50) or (4 * y - x < 40) for x in range(1, 100) for y in range(1, 100)):
        print(a)