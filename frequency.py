with open('frequencyfile.txt', 'r') as file:
    text = file.read()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = text.lower()
count = [0] * 26

# text = abcd

for t in text:
    if t in alpha:
        x = ord(t) - 97
        count[x] = count[x] + 1

space = " "
i = 0
print('FREQUENCY OF LETTERS:')
while(i<13):
    print(f'{alpha[i]} - {count[i]}{space*(8-len(str(count[i])))}{alpha[i+13]} - {count[i+13]}')
    i = i + 1 