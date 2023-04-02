a = 1
run = True
while run:
    for x in range(0, 13):
        for y in range(0, 13):
            n = 6 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 9 * 13 + y
            m = 2 * 15 ** 5 + y * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
            if (m + a) % n == 0:
                run = False
                print(a)
    a += 1


for x in range(0, 13):
    for y in range(0, 13):
        for A in range(1, 20000):
            M = 2 * 15 ** 5 + y * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5 + A
            N = 6 * 13 ** 4 + 7 * 13 ** 3 + x * 13 ** 2 + 9 * 13 + y
            if M % N == 0:
                print(M // N, A, sep='; ')