punc_marks = [',', '.', '?', '!', '"', ':', '—']
exc_marks = ['!', '?']

file_name = 'strings.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()
    file.close()
text = text.split('\n')

for i in range(len(text)):
    c = 0
    e = 0
    for j in range(len(text[i])):
        if text[i][j] in punc_marks:
            c += 1
        if text[i][j] in exc_marks:
            e += 1
    if c % 2 == 0:
        if e % 2 == 0:
            print(text[i], '- ДА')
        else:
            print(text[i], '- НЕТ')
    else:
        if e % 2 == 0:
            print(text[i], '- НЕТ')
        else:
            print(text[i], '- ДА')
    with open('output.txt', 'a', encoding='utf-8') as file:
        if c % 2 == 0:
            if e % 2 == 0:
                file.write(text[i] + ' - ДА\n')
            else:
                file.write(text[i] + ' - НЕТ\n')
        else:
            if e % 2 == 0:
                file.write(text[i] + ' - НЕТ\n')
            else:
                file.write(text[i] + ' - ДА\n')
        file.close()