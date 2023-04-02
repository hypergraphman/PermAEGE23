for a in range(0, 55):
    n = int('z', 36) * 55 ** 3 + a * 55 ** 2 + int('y', 36) * 55 + int('x', 36) - (2 * 55 ** 3 + int('x', 36) * 55 ** 2 + a * 55 + int('y', 36))
    if n % 29 == 0:
        print(a, n)