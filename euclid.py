# Euclid Algorithm
a = int(input('enter a : '))
b = int(input('enter b : '))

def gcd(a,b):
    while(b>0):
        r = a%b
        a = b
        b = r
    return a

print(f"GCD of ({a},{b}) is {gcd(a,b)}")