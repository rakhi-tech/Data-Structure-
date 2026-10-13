def lcm(n1, n2):
    
    if n1 == 0 or n2 == 0:
        return 0
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    return abs(n1 * n2) // gcd(n1, n2)
