import os 

d = os.environ 

with open('environ.txt', 'w+') as file:
    for key, value in d.items():
        file.write(f'{key} : {value}'+'\n')
