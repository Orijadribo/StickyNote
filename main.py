from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def openfile():
    filepath = filedialog.askopenfilename()

    if filepath == '':
        return
    else:
        file = open(filepath, "r")

    data = file.read()
    print(data)
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


def newfile():
    note()


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

    fileMenu.add_command(label="New", command=newfile)
    fileMenu.add_command(label="Open", command=openfile)
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)

    editMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)

    global text
    text = Text(window,
                bg='light yellow',
                font=("ink free", 25),
                height=8,
                width=20,
                padx=20,
                pady=20)
    text.pack(expand=True, fill="both")

    window.mainloop()


note()
