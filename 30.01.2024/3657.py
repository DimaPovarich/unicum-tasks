import json

dictionary = {"русский": "russian", "англиский": "english", "миша": "misha"}
inp = str(input('введите слова через пробел: '))
inp1 = inp.split(' ')
for i in dictionary:
    for j in inp1:
        if j == i:
            inp1[inp1.index(j)] = dictionary[i]

out = ""
for i in inp1:
    out += f'{i} '
print(out)
with open("s.json", 'w') as file:
    json.dump(out, file)