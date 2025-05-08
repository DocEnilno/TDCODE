#imports
from commandengine import *
print('TD-Code Console by TheDoctor @2021\n"help" for help!\n \n')

#loop
td_input = 1
while 1:
    cmd = input(f'In [{td_input}]: ')
    cmdlist = cmd.split()
    if cmdlist[0] == 'run':
        with open(f'{cmdlist[1]}') as code:
            for line in code:
                output = ''
                try:
                    output = commandengine(line, True)
                finally:
                    print(output)
    else:
        out = commandengine(cmd, True)
        print(f'Out [{td_input}]:\n{out}')
    td_input += 1