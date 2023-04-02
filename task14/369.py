for x in range(1, 10):
    n = 1 * int(f'1{x}234') + 3 + 1 * int(f'{x}1234') + 3
    if n % 13 == 0:
        print(n // 13)
