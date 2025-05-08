# Imports
from tkinter import *
from tkinter import filedialog
from commandengine import commandengine

#variables
global path
path = './unnamed.tdco'
main = Tk()
main.title('TD-Code IDE')
main.iconbitmap('./assets/icon.ico')
textfeld = Text(bg='#eab676')
textfeld.pack()
console = Text(state='normal', bg='black', fg='#76b5c5')
console.insert(END, 'TD-Code Console by TheDoctor @2021\n"help" for help!\n \n')
console.config(state='disabled')
console.pack()


main.title(f'TD-Code IDE -- {path}')

#functions
def openfile():
    global path
    path = filedialog.askopenfilename()
    with open(path, 'r', encoding='utf8') as file:
        code = file.read()
        textfeld.delete('1.0', END)
        textfeld.insert(END, code)
        main.title(f'TD-Code IDE -- {path}')

def save():
    with open(path, 'w', encoding='utf8') as file:
        code = textfeld.get('1.0', END)
        file.write(f'{code}')

def saveas():
    path = filedialog.asksaveasfilename()
    main.title(f'TD-Code IDE -- {path}')
    with open(path, 'w', encoding='utf8') as file:
        code = textfeld.get('1.0', END)
        file.write(f'{code}')#

def cconsole():
    console.config(state='normal')
    console.delete('1.0', END)
    console.insert(END, 'TD-Code Console by TheDoctor @2021\n"help" for help!\n \n')
    console.config(state='disabled')

def newfile():
    textfeld.delete('1.0', END)
    path = './unnamed.tdco'
    main.title(f'TD-Code IDE -- {path}')
    cconsole()

def run():
    with open('./temp/scriptrunner.txt', 'w', encoding='utf8') as file:
        code = textfeld.get('1.0', END)
        file.write(f'{code}')
    with open('./temp/scriptrunner.txt') as code:
        global output
        for line in code:
            output = ''
            try:
                output = commandengine(line)
            finally:
                console.config(state='normal')
                console.insert(END, f'{output}')
                console.config(state='disabled')

#filemenu
filemenu = Menu(main)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=saveas)
filemenu.add_command(label="Run Code", command=run)
filemenu.add_command(label="Clear Console", command=cconsole)
main.config(menu=filemenu)

#end
main.resizable(False, False)
main.mainloop()