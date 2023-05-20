import numba

@numba.jit
def pi_leibniz(n):
    sum = 0
    for i in range(n):
        sum += (-1)**i / (2*i + 1)
    return sum * 4

print(pi_leibniz(10**8))
