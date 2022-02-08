import sys

command = sys.argv

with open('backery.csv', 'r', encoding='utf-8') as f:
    if len(command) == 2:
        start = int(command[1]) - 1
        lines = f.readlines()[start::]

    elif len(command) == 3:
        start = int(command[1]) - 1
        end = int(command[2])
        lines = f.readlines()[start:end]
        
    else:
        lines = [line for line in f]
    lines = [line.rstrip() for line in lines]
    print(*lines, sep='\n')
