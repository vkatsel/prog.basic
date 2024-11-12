import pickle
import os
with open(os.getcwd()+'\groups.csv', 'rb') as file:
    data = pickle.load(file)

for grade in data:
    print(f'---------- {grade} grade ----------')
    for language in data[grade]:
        print(f'---- {language}')
        for student in data[grade][language]:
            print('     ', end='')
            print(*student, sep=', ')
        print()