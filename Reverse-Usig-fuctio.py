def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r

a = int(input("Enter A Number To Find Its Reverse"))
print(reverse_number(a))
