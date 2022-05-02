side_length = int(input())

matrix = []

for _ in range(side_length):
    matrix.append(list(map(int, input().split())))

spiral = []


top = left = 0
bottom = right = side_length - 1


while 'bruh':
    if left > right:
        break

    for i in range(left, right + 1):
        spiral.append(matrix[top][i])
    top = top + 1

    if top > bottom:
        break

    for i in range(top, bottom + 1):
        spiral.append(matrix[i][right])
    right = right - 1

    if left > right:
        break

    for i in range(right, left - 1, -1):
        spiral.append(matrix[bottom][i])
    bottom = bottom - 1

    if top > bottom:
        break

    for i in range(bottom, top - 1, -1):
        spiral.append(matrix[i][left])
    left = left + 1


def negate_odd(x):
    return x[1] if x[0] % 2 == 0 else -x[1]


spiral = list(map(negate_odd, enumerate(spiral)))

print('Prize!' if sum(spiral[:-1]) == spiral[-1] else 'No Prize!')
