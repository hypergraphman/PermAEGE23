win = 45
lose = 112


def f(a, c, m):
    if a > lose:
        return c % 2 != m % 2
    if a >= win:
        return c % 2 == m % 2

    if c == m:
        return False
    moves = [f(a + 2, c + 1, m),
             f(a * 3, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for a in range(1, win):
    for m in range(1, 5):
        if f(a, 0, m):
            print(a, m)
            break