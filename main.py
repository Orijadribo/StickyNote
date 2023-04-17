from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import colorchooser


def openfile():
    filepath = filedialog.askopenfilename()

    if filepath == '':
        return
    else:
        file = open(filepath, "r")

    data = file.read()
    # print(data)
    file.close()


def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return

    filetext = str(text.get("1.0", END))
    file.write(filetext)
    file.close()


def newColor():
    def colorPicker():
        global colorHex
        colorN = colorchooser.askcolor()
        colorHex = colorN[1]
        colorHex = str(colorHex)
        return colorHex

    global color
    color = colorPicker()
    # print(color)
    return color


colorB = ['light yellow']
i = [0]


def asking():
    global colorB
    global i
    colorB.append(newColor())
    i[0] = len(colorB) - 1
    Text.config(text, bg=colorB[i[0]])


def select():
    pass


def cut():
    pass


def copy():
    pass


def paste():
    pass


def note():
    window = Tk()
    window.title("Sticky Note")

    menubar = Menu(window)
    window.config(menu=menubar)

    fileMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=fileMenu)

    fileMenu.add_command(label="New", command=note)
    fileMenu.add_command(label="Open", command=openfile)
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)

    editMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    editMenu.add_separator()
    editMenu.add_command(label="Choose background color", command=asking)

    global text
    text = Text(window,
                bg=colorB[i[0]],
                font=("ink free", 25),
                height=8,
                width=20,
                padx=20,
                pady=20)
    text.pack(expand=True, fill="both")

    window.mainloop()


note()
