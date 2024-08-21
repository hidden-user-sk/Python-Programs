def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r

print(reverse_number(123))
