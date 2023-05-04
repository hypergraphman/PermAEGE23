start = 13
# lose = ...


def f(a, b, c, m):
    # if a + b > lose:
    #     return c % 2 != m % 2
    if a == b:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = []
    if a < b:
        moves.append(f(a + 1, b, c + 1, m))
        moves.append(f(a + 3, b, c + 1, m))
    if b < a:
        moves.append(f(a, b + 1, c + 1, m))
        moves.append(f(a, b + 3, c + 1, m))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for b in range(1, 23):
    for m in range(1, 5):
        if f(start, b, 0, m):
            if m == 4:
                print(b, m)
            break