#1. For two integers a and b, where a > b, divide a by b
#2. If the remainder, r, is 0, then stop: GCD is b.
#3. Otherwise, set a to b, b to r, and repeat at step 1 until r is 0

def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b

    return a

print(gcd(100, 84))
print(gcd(20, 81))