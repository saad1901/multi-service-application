with open('output-subst.txt', 'r') as file:
    text3 = file.read()

if text3 == '':
    print('FILE IS EMPTY')
else:

    key2 = input('Enter key : ').upper()
    if key2 == '':
        key2 = "MONARCHY"
    text3 = text3.upper()

    matrix = [[0 for _ in range(5)] for _ in range(5)]
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    letter_order = []
    for char in key2:
        if char != ' ' and char not in letter_order:
            letter_order.append(char)

    key = ''
    for s in letter_order:
        key += s

    i = 0 ; j = 0
    for k in key:
        matrix[i][j] = k
        j += 1
        if j == 5:
            i += 1
            j = 0

    for m in range(5):
        for n in range(5):
            for p in range(len(alpha)):
                if matrix[m][n] == alpha[p]:
                    alpha.pop(p)
                    break

    for a in alpha:
        if a not in matrix and i < 5:
            matrix[i][j] = a
            j += 1
            if j == 5:
                i += 1
                j = 0

    def decrypt_text(text, matrix):
        text2 = ''
        r = 0
        while r < len(text):
            flag = 0
            for i in range(5):
                for j in range(5):
                    if text[r] == " ":
                        text2 += text[r]
                        r += 1
                        flag = 1
                        break
                    elif matrix[i][j] == text[r]:
                        flag = 1
                        break
                if flag == 1:
                    break

            flag = 0
            for m in range(5):
                for n in range(5):
                    if r < len(text) and text[r] == " ":
                        flag = 1
                        break
                    elif r + 1 < len(text) and text[r + 1] == " ":
                        text2 += text[r + 1]
                        r += 2
                        flag = 1
                        break
                    elif r + 1 < len(text) and matrix[m][n] == text[r + 1]:
                        flag = 1
                        break

                if flag == 1:
                    break

            if i == m:
                text2 += matrix[i][(j - 1) % 5]
                text2 += matrix[m][(n - 1) % 5]
            elif j == n:
                text2 += matrix[(i - 1) % 5][j]
                text2 += matrix[(m - 1) % 5][n]
            else:
                text2 += matrix[i][n]
                text2 += matrix[m][j]
            r += 2

        return text2

    decrypted_text = decrypt_text(text3, matrix)

    with open('output-subst-decrypted.txt', 'w') as file:
        file.write(decrypted_text)

    print("Decryption completed")
