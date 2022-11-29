def f(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def power(b, e):
    if e == 0:
        return 1
    half = power(b, e >> 1)
    return half * half * b if e & 1 else half * half


def matrix_mult(m1, m2):
    a, b, c, d = m1
    e, f, g, h = m2
    return [a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h]


def matrix_power(m, e):
    if e == 0:
        return [1, 0, 0, 1]
    half = matrix_power(m, e >> 1)
    return matrix_mult(matrix_mult(half, half), m) if e & 1 else matrix_mult(half, half)


def fibogood(n):
    return matrix_power([0, 1, 1, 1], n)[1]


fibogood(10**6)
