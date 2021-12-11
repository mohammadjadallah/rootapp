from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    root.geometry('1200x600+80-80')
    root.config(bg="#95B2E8")
    root.title('root app')
    root.iconbitmap(r'roots.ico')
    choiceMethod = ('  Bisection method', '  False position method', '  Secant method')
    style = ttk.Style()

    def place_holder1(event):
        if str(entry1.get()) == '          Enter the function here':
            entry1.delete(0, END)

    def place_holder2(event):
        if str(entry2.get()) == '      X lower':
            entry2.delete(0, END)

    def place_holder3(event):
        if str(entry3.get()) == '      X upper':
            entry3.delete(0, END)

    def place_holder4(event):
        if str(entry4.get()) == '  given error':
            entry4.delete(0, END)

    def place_holder5(event):
        if str(entry2.get()) == '      Xi-1':
            entry2.delete(0, END)

    def place_holder6(event):
        if str(entry3.get()) == '          Xi':
            entry3.delete(0, END)

    def pre_space(e):
        # to entry1
        if entry1.get() == '':
            entry1.insert(0, ' ')
        elif entry1.get()[0] != ' ':
            entry1.insert(0, ' ')

        # to entry2
        if entry2.get() == '':
            entry2.insert(0, ' ')
        elif entry2.get()[0] != ' ':
            entry2.insert(0, ' ')

        # to entry2
        if entry2.get() == '':
            entry2.insert(0, ' ')
        elif entry2.get()[0] != ' ':
            entry2.insert(0, ' ')

        # to entry3
        if entry3.get() == '':
            entry3.insert(0, ' ')
        elif entry3.get()[0] != ' ':
            entry3.insert(0, ' ')

        # to entry4
        if entry4.get() == '':
            entry4.insert(0, ' ')
        elif entry4.get()[0] != ' ':
            entry4.insert(0, ' ')

    def check():
        for entries in [entry1, entry2, entry3, entry4]:
            entries.delete(0, END)

        if boxChoose.get() == choiceMethod[0] or boxChoose.get() == choiceMethod[1]:
            entry2.insert(0, '      X lower')
            entry3.insert(0, '      X upper')

            for entry, place in [(entry1, place_holder1), (entry2, place_holder2),
                                 (entry3, place_holder3), (entry4, place_holder4)]:
                entry.bind('<Button>', place)

        if boxChoose.get() == '  Secant method':
            entry2.insert(0, '      Xi-1')
            entry3.insert(0, '          Xi')

            entry2.bind('<Button>', place_holder5)
            entry3.bind('<Button>', place_holder6)

        entry1.insert(0, '          Enter the function here')
        entry4.insert(0, '  given error')

    entry1 = Entry(root, font='arial 30 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)
    entry2 = Entry(root, font='arial 22 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)
    entry3 = Entry(root, font='arial 22 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)
    entry4 = Entry(root, font='arial 22 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)

    btn1 = Button(root, text='Draw function', relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB')

    btn2 = Button(root, text='Get data', relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB')

    btn3 = Button(root, text='convert', relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB',
                  command=lambda: check())

    boxChoose = ttk.Combobox(root, font='arial 15 bold', value=choiceMethod, justify='center')

    entry1.place(x=300, y=210, height=100, width=640)
    entry2.place(x=300, y=130, height=70, width=200)
    entry3.place(x=520, y=130, height=70, width=200)
    entry4.place(x=740, y=130, height=70, width=200)

    btn1.place(x=300, y=320, height=100, width=300)
    btn2.place(x=640, y=320, height=100, width=300)
    btn3.place(x=20, y=80, height=60, width=250)

    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#5C88AB", background="#5C88AB")
    boxChoose.place(x=20, y=10, height=60, width=250)
    boxChoose.current(0)

    for entry, place in [(entry1, place_holder1), (entry2, place_holder2),
                         (entry3, place_holder3), (entry4, place_holder4)]:
        entry.bind('<Button>', place)

    for i in [entry1, entry2, entry3, entry4]:
        i.bind('<Key>', pre_space)

    entry1.insert(0, '          Enter the function here')
    entry2.insert(0, '      X lower')
    entry3.insert(0, '      X upper')
    entry4.insert(0, '  given error')

    root.mainloop()


#main()

