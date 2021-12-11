# function to calculate equation

def bisection_method(equation, a, b, given_error):  # function, boundaries, Es
    try:
        li_a = deque()  # a
        li_b = deque()  # b
        li_c = deque()  # x root -> c
        li_fc = deque()  # f(xr)
        li_fa = deque()  # f(a)
        li_fb = deque()  # f(b)
        li_Ea = deque()  # estimated error

        data = {
            'Xl': li_a,
            'Xu': li_b,
            'Xr': li_c,
            'f(Xl)': li_fa,
            'f(Xu)': li_fb,
            'f(Xr)': li_fc,
            'Ea%': li_Ea,
        }

        global c

        def f(x):
            F = eval(equation)  # the x here when we f(a) a will be instead of x
            return F

        # substitute boundaries in function
        if f(a)*f(b) >= 0:
            showerror('Error', 'Bisection method is fail')
            for breaks in range(1):
                break

        # elif we have a different sign
        else:
            Estimated_Error = 0

            while Estimated_Error/100 <= given_error:
                c = (a + b) / 2
                if Estimated_Error == 0:
                    li_a.append(a)
                    li_b.append(b)
                    li_c.append(c)
                    li_fa.append(f(a))
                    li_fb.append(f(b))
                    li_fc.append(f(c))
                    li_Ea.append(None)

                if f(a)*f(c) < 0:
                    b = c
                    c1 = (a + b)/2
                    Estimated_Error = abs((c1 - c)/c1) * 100

                elif f(b)*f(c) < 0:
                    a = c
                    c1 = (a + b) / 2
                    Estimated_Error = abs((c1 - c) / c1) * 100

                else:
                    showerror('Error', 'something is wrong!')
                    break

            else:
                while Estimated_Error/100 >= given_error:
                    c = (a + b) / 2

                    # append data to to the list

                    li_a.append(a)
                    li_b.append(b)
                    li_c.append(c)
                    li_fa.append(f(a))
                    li_fb.append(f(b))
                    li_fc.append(f(c))
                    li_Ea.append('%.5f' % Estimated_Error+'%')

                    if f(a) * f(c) < 0:
                        b = c
                        c1 = (a + b) / 2
                        Estimated_Error = abs((c1 - c) / c1) * 100
                    elif f(b) * f(c) < 0:
                        a = c
                        c1 = (a + b) / 2
                        Estimated_Error = abs((c1 - c) / c1) * 100

                    else:
                        showerror('Error', 'something is wrong!')
                        break
                else:
                    c = (b + a)/2
                    li_a.append(a)
                    li_b.append(b)
                    li_c.append(c)
                    li_fa.append(f(a))
                    li_fb.append(f(b))
                    li_fc.append(f(c))
                    li_Ea.append('%.5f' % Estimated_Error+'%')

                    with asksaveasfile(mode='wb', filetypes=[('Text file', '.txt')],
                                       defaultextension=[('Text file', '.txt')]) as f:
                        f.write(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=1).encode('utf-8'))
                        f.write(f'\n\nthe final root is {li_c[len(li_c) - 1]}'.encode('utf-8'))
                        label1.config(text='The text file downloaded inside the project, you can see the data...')
    except (TypeError, NameError):
        showwarning('problem', 'you have a problem with interval')

    except ZeroDivisionError:
        showerror('ZeroDivisionError', 'Zero Division Error')


def false_position_method(equation, a, b, given_error):
    try:
            Xl = deque()
            Xu = deque()
            Xr = deque()
            f_Xl = deque()
            f_Xu = deque()
            f_Xr = deque()
            Ea = deque()

            data = {
                'Xl': Xl,
                'Xu': Xu,
                'Xr': Xr,
                'f(Xl)': f_Xl,
                'f(Xu)': f_Xu,
                'f(Xr)': f_Xr,
                'Ea': Ea
            }

            def f(x):
                F = eval(equation)
                return F

            # the first root is zero
            c_before = 0
            # the general rule in false position to find the root
            c = b - ((f(b))*(a - b) / (f(a) - f(b)))  # first iteration has this root

            # estimated_error = ((current root - old root)/current root) * 100
            estimated_error = abs(((c - c_before)/c))*100

            while estimated_error/100 > given_error:

                new_c = b - ((f(b))*(a - b) / (f(a) - f(b)))

                Xl.append(a)
                Xu.append(b)
                Xr.append(new_c)
                f_Xl.append(f(a))
                f_Xu.append(f(b))
                f_Xr.append(f(c))
                Ea.append(None if estimated_error == 100 else ('%.5f' % estimated_error + '%'))

                if f(a) * f(b) >= 0:
                    showerror("error", "False position is fail")
                    break

                elif f(a) * f(new_c) < 0:
                    b = new_c
                    c2 = b - ((f(b))*(a - b) / (f(a) - f(b)))
                    estimated_error = abs(((c2 - new_c)/c2))*100

                elif f(b) * f(new_c) < 0:
                    a = new_c
                    c2 = b - ((f(b)) * (a - b) / (f(a) - f(b)))
                    estimated_error = abs(((c2 - new_c) / c2)) * 100

                else:
                    showerror("error", "something is wrong!")
                    break
            else:
                new_c = b - ((f(b)) * (a - b) / (f(a) - f(b)))
                Xl.append(a)
                Xu.append(b)
                Xr.append(new_c)
                f_Xl.append(f(a))
                f_Xu.append(f(b))
                f_Xr.append(f(new_c))
                Ea.append('%.5f' % estimated_error + '%')

                with asksaveasfile(mode='wb', filetypes=[('Text file', '.txt')], defaultextension=[('Text file', '.txt')]) as f:
                    f.write(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=1).encode('utf-8'))
                    f.write(f'\n\nthe final root is {Xr[len(Xr)-1]}'.encode('utf-8'))
                    label1.config(text='The text file downloaded inside the project, you can see the data...')

    except (TypeError, NameError):
        showwarning('problem', 'try another numbers or intervals')

    except ZeroDivisionError:
        showerror('ZeroDivisionError', 'Zero Division Error')


def secant_method(equation, a, b, given_error):
    Xis = deque()
    Xi_1s = deque()
    Xrs = deque()
    Eas = deque()

    data = {
        'Xi': Xis,
        'Xi_1': Xi_1s,
        'Xr': Xrs,
        'Ea': Eas
    }

    def f(x):
        F = eval(equation)
        return F

    try:
        before_c = 0
        Xi = a
        X_i_minus1 = b
        Xr = Xi - ((f(Xi) * (Xi - X_i_minus1)) / (f(Xi) - f(X_i_minus1)))
        Ea = abs((Xr - before_c) / Xr) * 100
        count = 1
        while Ea / 100 > given_error:

            Xr = Xi - ((f(Xi) * (Xi - X_i_minus1)) / (f(Xi) - f(X_i_minus1)))

            Ea = abs((Xr - Xi) / Xr) * 100
            X_i_minus1, Xi = Xi, Xr

            Xis.append(Xi)
            Xrs.append(Xr)
            Xi_1s.append(X_i_minus1)
            Eas.append(Ea)

            count += 1

        else:
            Xr = Xi - ((f(Xi) * (Xi - X_i_minus1)) / (f(Xi) - f(X_i_minus1)))
            Ea = abs((Xr - Xi) / Xr) * 100

            Xis.append(Xi)
            Xrs.append(Xr)
            Xi_1s.append(X_i_minus1)
            Eas.append(Ea)

        with asksaveasfile(mode='wb', filetypes=[('Text file', '.txt')], defaultextension=[('Text file', '.txt')]) as f:
            f.write(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=1).encode('utf-8'))
            f.write(f'\n\nthe final root is {Xrs[count - 1]}'.encode('utf-8'))
            label1.config(text='The text file downloaded inside the project, you can see the data...')

    except ZeroDivisionError:
        showerror('ZeroDivisionError', 'Zero Division Error')


def draw_function():
    try:
        st.use('ggplot')
        x, y, z, alpha, beta = symbols('x y z alpha beta', real=True)
        plot(eval(str(entry1.get())), (x, -10, 10), title=str(entry1.get()), show=True)

    except (TypeError, NameError):
        pass

    except SyntaxError:
        showwarning('Syntax Error', 'please fix the syntax of function')


if __name__ == '__main__':
    from tkinter import *
    from tkinter import ttk
    from tkinter.messagebox import showerror, showwarning
    from tkinter.filedialog import asksaveasfile
    from collections import deque
    from tabulate import tabulate
    from sympy import *
    from webbrowser import open_new_tab
    from matplotlib.pyplot import style as st  # because tkinter has Style object and in this case python raise error

    # and because sympy based on matplotlib we can use style.use to show the grid with the style we want

    root = Tk()
    root.geometry('1200x600+80-80')
    root.config(bg="#95B2E8")
    root.title('root app')
    root.iconbitmap(r'C:\Users\mhmdj\PycharmProjects\rootapp\roots.ico')
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


    def place_holder_choose(event):

        for en in [entry1, entry2, entry3, entry4]:
            if str(en.get()) == '                      choose' or en.get() == '      choose':
                en.delete(0, END)


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

            for entries, places in [(entry1, place_holder1), (entry2, place_holder2),
                                    (entry3, place_holder3), (entry4, place_holder4)]:
                entries.bind('<Button>', places)

        if boxChoose.get() == '  Secant method':
            entry2.insert(0, '      Xi-1')
            entry3.insert(0, '          Xi')

            entry2.bind('<Button>', place_holder5)
            entry3.bind('<Button>', place_holder6)

        entry1.insert(0, '          Enter the function here')
        entry4.insert(0, '  given error')
        entry1.bind('<Button>', place_holder1)
        entry4.bind('<Button>', place_holder4)


    def call_back_func(event):
        boxChoose1 = event.widget.get()
        if boxChoose1 == choiceMethod[0]:
            btn2.config(command=lambda: bisection_method(entry1.get(), float(entry2.get()),
                                                         float(entry3.get()), float(entry4.get()) / 100))
        elif boxChoose1 == choiceMethod[1]:
            btn2.config(command=lambda: false_position_method(entry1.get(), float(entry2.get()),
                                                              float(entry3.get()), float(entry4.get()) / 100))
        elif boxChoose1 == choiceMethod[2]:
            btn2.config(command=lambda: secant_method(entry1.get(), float(entry2.get()),
                                                      float(entry3.get()), float(entry4.get()) / 100))

    def top_level():
        window = Toplevel()
        window.geometry('500x600')
        window.resizable(0, 0)
        label0 = Label(window, text='The methods and links: ', font='arial 15 bold', bg='black', fg='red')
        label2 = Label(window, text='    Bisection method', font='arial 15 bold', fg='blue', cursor='hand2')
        label3 = Label(window, text='           False position method', font='arial 15 bold', fg='blue', cursor='hand2')
        label4 = Label(window, text='Secant method', font='arial 15 bold', fg='blue', cursor='hand2')

        message = Message(window, text='The operation: \n'
                                       '    Multiplication = *\n'
                                       '    Subtraction = -\n'
                                       '    Plus = +\n'
                                       '    Power = **\n'
                                       '    Division = /\n'
                                       '    ln = log(put what you want)\n'
                                       '    e = exp(put what you want)\n'
                                       '    sin() cos() tan() sinh()...\n',
                          font='bold 20')

        label0.grid(row=0, column=0, pady=20)
        label2.grid(row=1, column=0, pady=5)
        label3.grid(row=2, column=0, pady=5)
        label4.grid(row=3, column=0, pady=5)
        message.place(x=50, y=200)

        label2.bind('<Button-1>', lambda e: link('https://en.wikipedia.org/wiki/Bisection_method'))
        label3.bind('<Button-1>', lambda e: link('https://en.wikipedia.org/wiki/Regula_falsi'))
        label4.bind('<Button-1>', lambda e: link('https://en.wikipedia.org/wiki/Secant_method'))

        def link(url):
            open_new_tab(url)

        window.mainloop()


    entry1 = Entry(root, font='arial 30 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)
    entry2 = Entry(root, font='arial 22 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)
    entry3 = Entry(root, font='arial 22 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)
    entry4 = Entry(root, font='arial 22 bold', insertbackground='purple',
                   fg='black', bg='#5C88AB', relief=FLAT)

    btn1 = Button(root, text='Draw function', relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB',
                  command=lambda: root.after(1, draw_function), cursor='hand2')

    btn2 = Button(root, text='Get data', relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB', cursor='hand2')

    btn3 = Button(root, text='convert', relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB',
                  command=lambda: check(), cursor='hand2')
    btn4 = Button(root, text="user's guide", relief=SOLID,
                  bg='#5C88AB', font='arial 20 bold', activebackground='#5C88AB',
                  command=lambda: top_level(), cursor='hand2')

    boxChoose = ttk.Combobox(root, font='arial 15 bold', value=choiceMethod, justify='center',
                             validate='focusout')

    label1 = Label(root, font='arial 15 bold', bg='#95B2E8', fg='#5C88AB')
    label1.place(x=300, y=460)

    entry1.place(x=300, y=210, height=100, width=640)
    entry2.place(x=300, y=130, height=70, width=200)
    entry3.place(x=520, y=130, height=70, width=200)
    entry4.place(x=740, y=130, height=70, width=200)

    btn1.place(x=300, y=320, height=100, width=300)
    btn2.place(x=640, y=320, height=100, width=300)
    btn3.place(x=20, y=80, height=60, width=250)
    btn4.place(x=20, y=520, height=60, width=250)

    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#5C88AB", background="#5C88AB")
    boxChoose.place(x=20, y=10, height=60, width=250)

    for entry, place in [(entry1, place_holder1), (entry2, place_holder2),
                         (entry3, place_holder3), (entry4, place_holder4)]:
        entry.bind('<Button>', place)

    for i in [entry1, entry2, entry3, entry4]:
        i.bind('<Key>', pre_space)

    entry1.insert(0, '          Enter the function here')
    entry2.insert(0, '      X lower')
    entry3.insert(0, '      X upper')
    entry4.insert(0, '  given error')

    boxChoose.set('Choose the method')
    for e in [entry1, entry2, entry3, entry4]:
        e.delete(0, END)
        if entry1 == e:
            e.insert(0, '                      choose')
        else:
            e.insert(0, '      choose')
        e.bind('<Button>', place_holder_choose)

    boxChoose.bind("<<ComboboxSelected>>", call_back_func)
    root.mainloop()
