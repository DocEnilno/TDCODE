import random
import sys
import os

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

output = ''
def commandengine(command, cmdm=False):
    os_check = get_platform()
    if '#' in command[0]:
        return ''
    else:
        cmdlist = command.split()
        if cmdlist[0] == 'help':
            output = 'The Commands:\n-say <str:text>  (prints <str:text> into the console!)\n-rand <int:smallestnum> <int:biggestnum>  (generates a random number between <int:smallestnum> and <int:biggestnum>)\n-clear  (clears the console, only works in console mode)\n-color <int:color> (changes the color of the text inside of the Console (Colors  1-9) and only works under Windows in Console mode!)\n-run <str:filepath>  (runs the file from <str:filepath>, only works in Console Mode)'

        elif cmdlist[0] == 'say':
            cmdlist.pop(0)
            num = 0
            for element in cmdlist:
                num += 1
            if num < 0:
                output = 'Error while running say Command'
            elif num == 1:
                output = cmdlist[0]
            elif num > 1:
                output = ' '.join(cmdlist)
                
        elif cmdlist[0] == 'rand':
            output = random.randint(int(cmdlist[1]), int(cmdlist[2]))

        elif cmdlist[0] == 'clear':
            if cmdm == True:
                if os_check == 'Windows':
                    os.system('cls')
                    output = 'Clear Succesfull'
                else:
                    os.system('clear')
                    output = 'Clear Succesfull'
                print('TD-Code Console by TheDoctor @2021\n"help" for help!\n \n')
            else:
                output = 'This command is only Supportet in CMDmode'
        
        elif cmdlist[0] == 'color':
            if cmdm == True:
                if os_check == 'Windows':
                    os.system(f'color {cmdlist[1]}')
                    output = 'Color Succesfully Changed'
                else:
                    output = 'This command is only Supportet in Windows Terminal/Powershell'
            else:
                output = 'This command is only Supportet in CMDmode'

        elif cmdlist[0] == 'run':
            output = 'This command is only Supportet in CMDmode'

        else:
            output = f'ERROR - Command "{cmdlist[0]}" not found!'

        return f'{output}\n'