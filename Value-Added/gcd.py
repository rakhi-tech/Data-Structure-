def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1
