# Extended Euclid Algorithm
a = int(input('enter a : '))
b = int(input('enter b : '))
a = abs(a)
b = abs(b)

r1 = a
r2 = b
s1 = t2 = 1
s2 = t1 = 0

while(r2 > 0):
    q = int(r1 / r2)
    r = r1 - (q*r2)
    r1 = r2
    r2 = r

    s = s1 - (q*s2)
    s1 = s2
    s2 = s

    t = t1 - (q*t2)
    t1 = t2
    t2 = t


print(f"r = {r1}")

s = s1
t = t1
k = s*a + t*b
print(f"s*a + t*b = {k}")
print(f"x = s = {s}")
print(f"y = t = {t}")

