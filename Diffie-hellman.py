qs = input("Enter q : ")
q = int(qs)
a = input('enter alpha : ')

lis = []
roots = []
def calalpha(q):
    for i in range(2,int(q)):
        lis.clear()
        lis.append(i^1)
        for j in range(2,int(q)):
            if (lis[-1]*i)%q in lis:
                break
            else:
                lis.append((lis[-1]*i)%q)
        
        if len(lis) == q-1:
            roots.append(i)
            # return i


if a == '':
    calalpha(q)

print(f"premitive roots of {q} are {roots}")

