s = input('Write some text.\n')
with open('example.txt', 'w') as file:
    file.write(s)

r = open('example.txt')

print(r.read())

