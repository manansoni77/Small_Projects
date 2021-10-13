from os import system, path
import pickle
from types import MethodWrapperType

tasks = []

if path.isfile('tasks.txt'):
    with open('tasks.txt', 'rb') as fp:
        tasks = pickle.load(fp)

while True:
    system('cls')
    print('TO-DO')
    for i,t in enumerate(tasks):
        print(i+1,t)
    new_t = input()
    if new_t == 'exit':
        with open('tasks.txt', 'wb') as fp:
            pickle.dump(tasks, fp)
        exit()
    elif new_t == 'clear':
        tasks = []
    elif new_t.startswith('done'):
        new_t = new_t.split()[1]
        if new_t.isnumeric():
            new_t = int(new_t)
            if(new_t<1 or new_t>len(tasks)):
                continue
            tasks[new_t-1] = tasks[new_t-1][:-1] + u'\u2713'
    elif new_t.startswith('remove'):
        new_t = new_t.split()[1]
        if new_t.isnumeric():
            new_t = int(new_t)
            if(new_t<1 or new_t>len(tasks)):
                continue
            del(tasks[int(new_t)-1])
    else:
        tasks.append(new_t+' -')
