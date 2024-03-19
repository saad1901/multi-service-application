msg = input('enter msg : ')

# k1 = 345
keys = {345}

ciphor = ''
plain = ''

text = msg

for k in keys:
    for a in text:
        ciphor = ciphor + chr((ord(a)-ord('a')+(k%26))%26+ord('a'))
    text = ciphor

print(f"ciphor text E(P) : {ciphor}")

key = {345}
for k2 in key:
    for c in text:
        plain = plain + chr(((ord(c)-ord('a')-(k2%26))%26)+ord('a'))
    text = plain

print(f"plain text D(C)  : {plain}")



# # from gpt4
# msg = "hello"

# keys = {345, 54255, 4254656}

# ciphor = ''
# plain = ''

# for k in keys:
#     ciphor = ''
#     for a in msg:
#         ciphor += chr((ord(a) - ord('a') + (k % 26)) % 26 + ord('a'))
#     print(f"ciphor text E(P) with key {k}: {ciphor}")

#     plain = ''
#     for c in ciphor:
#         plain += chr(((ord(c) - ord('a') - (k % 26)) % 26) + ord('a'))
#     print(f"plain text D(C) with key {k}: {plain}")

