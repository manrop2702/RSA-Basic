def egcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y 
    return old_r, old_s, old_t

gcd, x, y = egcd(26513, 32321)
print(gcd, end = "\n")
print(x, end = "\n")
print(y, end = "\n")
