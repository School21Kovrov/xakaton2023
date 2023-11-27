n = int(input())
field = [['.'] * n for _ in range(n)]
j = 0 if n % 2 else 1
for i in range(n):
    field[i][j] = 'Ф'
    j = (j + 2) % n
    if n % 2 == 0 and i == (n // 2) - 1:
        j -= 1
for row in field:
    print(''.join(row))
