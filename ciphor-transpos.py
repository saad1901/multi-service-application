#Transposition Ciphor
# key = input("enter key : ")
key = 'geca'
key = key.upper()
# msgx = input("Enter msg : ")
with open('input-transpos.txt', 'r') as file:
    msgx = file.read()
msgx = msgx.upper()
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
msg = ''
for m in msgx:
    if m in alpha:
        msg = msg+m 

buffer = ['X','Y','Z','W','Y']
    
while True:
    if len(msg)%len(key) == 0:
        l =  int(len(msg)/len(key))
        break
    else:
        msg = msg+buffer[0]
        buffer.pop(0)

matrix = [[0 for _ in range(len(key))] for _ in range(l)]

p = 0
for i in range(l):
    for j in range(len(key)):
        matrix[i][j] = msg[p]
        p+=1

print(list(key))
print("--------------------")
for row in matrix:
    print(row)
  
#now the cipher
cip = ''
lis = [char for char in key]
lis.sort()

for a in lis:
    for k in range(len(key)):
        if a == key[k]:
            for m in range(l):
                cip = cip + matrix[m][k]   


# print('ciphor text : ',cip)  
                
with open('output-transpos.txt', 'w') as file:
    file.write(cip)