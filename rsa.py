p = int(input('enter p : '))
q = int(input('enter q : '))
n = p * q

m = int(input('enter m:  '))
pn = (p-1)*(q-1)
e = int(input('enter e : '))

def binary(e):
    b = ''
    r = e
    while r != 0:
        b = str(r%2) + b
        r = int(r/2)
    return b[::-1]

def returny(l,m,n):
    y = 1
    for x in binary(l):
        if x == '1':
            y = (m*y) % n
        m = (m*m) % n
    return y
c = returny(e,m,n)
print('------------------------')
print(f"ciphor text : {c}")
print('------------------------')
d = 1

while True:
    if (e*d) % (pn) == 1:
        break
    d = d + 1
    
print("value of d :",d)

print('------------------------')
print(f"Plaintext text : {returny(d,c,n)}")
print('------------------------')

