from tkinter import *
import pandas as pd
from password_validator import PasswordValidator
from user_validatior import UserValidator
from tkinter import messagebox


class SignUp:
    min_user_length = 4
    max_user_length = 24
    min_pass_length = 8
    max_pass_length = 20
    sign_lb_font = ('Arial', 18, 'bold')
    entry_font = ('Arial', 14)
    gui_color = '#96C8FA'

    def __init__(self, root):
        self.root = root
        self.root.title('Sign Up')
        self.root.iconbitmap('icon.ico')
        self.root.geometry('550x350+250+100')
        self.root.config(bg=SignUp.gui_color)

        self.df = None

        # row and column settings:
        for i in range(8):
            Grid.rowconfigure(self.root, i, weight=1)

        for i in range(3):
            Grid.columnconfigure(self.root, i, weight=1)

        # functions:
        def show_pass(buton, entry):
            if entry.cget('show') == '*':    # switching password from * to letters
                entry.config(show='')
                buton.config(text='Hide')
            else:                            # switching password from letters to *
                entry.config(show='*')
                buton.config(text='Show')

        def max_length(P, l):                # limitation of text length
            return len(P) <= int(l)

        def confirm():                       # username verification
            if self.df is None:
                self.df = pd.read_excel('Users.xlsx')
            user_validation = UserValidator(self.User_ent.get(), SignUp.min_user_length, self.df)
            if user_validation.confirm() == 1:
                pass_valid()

        def pass_valid():                     # password verification
            password_validation = PasswordValidator(self.Pass_ent.get(), self.Confirm_ent.get())
            if password_validation.pass_validation() == 1:
                save_data()

        def save_data():   # saving data in xlsx file
            df1 = pd.Series([self.User_ent.get(), self.Confirm_ent.get()],
                            index=['User', 'Password'])
            new_df = pd.concat([self.df, df1.to_frame().T], ignore_index=True)
            with pd.ExcelWriter('Users.xlsx', engine='openpyxl') as writer:
                new_df.to_excel(writer, sheet_name='Users', index=False)
            messagebox.showinfo("Done!", 'Sing up complete!')
            exit()

        vcmd = root.register(max_length)
        # main widgets
        self.Sign_lb = Label(self.root, bg=SignUp.gui_color, text='Sign Up', font=SignUp.sign_lb_font)
        self.Sign_lb.grid(row=0, column=0, columnspan=3, sticky='NSEW')

        self.User_lb = Label(self.root, bg=SignUp.gui_color, text='Username:', anchor=E)
        self.User_lb.grid(row=1, column=0, sticky='NSEW')

        self.User_ent = Entry(self.root, font=self.entry_font, validate='key', validatecommand=(vcmd, '%P',
                                                                                                SignUp.max_user_length))
        self.User_ent.grid(row=1, column=1, sticky='NSEW')

        self.User_rules = Label(self.root, bg=SignUp.gui_color, text='Username must have at between %s-%s characters.'
                                                          % (SignUp.min_user_length, SignUp.max_user_length))
        self.User_rules.grid(row=2, column=0, columnspan=3, sticky='NSEW')

        self.Pass_lb = Label(self.root, bg=SignUp.gui_color, text='Password:', anchor=E)
        self.Pass_lb.grid(row=3, column=0, sticky='NSEW')

        self.Pass_ent = Entry(self.root, font=SignUp.entry_font, show='*',
                              validate='key', validatecommand=(vcmd, '%P', SignUp.max_pass_length))
        self.Pass_ent.grid(row=3, column=1, sticky='NSEW')

        self.Pass_rules = Label(self.root, bg=SignUp.gui_color, text='Password rules: %s-%s characters, incl'
                                                          'uding at least 1 letter, 1 number and 1 special character.'
                                                          % (SignUp.min_pass_length, SignUp.max_pass_length))
        self.Pass_rules.grid(row=4, column=0, columnspan=3, sticky='NSEW')

        self.Confirm_lb = Label(self.root, bg=SignUp.gui_color, text='Confirm password:', anchor=E)
        self.Confirm_lb.grid(row=5, column=0, sticky='NSEW')

        self.Confirm_ent = Entry(self.root, font=SignUp.entry_font, show='*',
                                 validate='key', validatecommand=(vcmd, '%P', SignUp.max_pass_length))
        self.Confirm_ent.grid(row=5, column=1, sticky='NSEW')

        self.Confirm_btn = Button(self.root, text='Sign Up', command=confirm)
        self.Confirm_btn.grid(row=6, column=1, sticky='NSEW')

        # show/hide password buttons:

        self.Show_but1 = Button(self.root, width=4, text='Show', command=lambda: show_pass(self.Show_but1,
                                                                                           self.Pass_ent))
        self.Show_but1.grid(row=3, column=2, sticky='NSWE')

        self.Show_but2 = Button(self.root, width=4, text='Show', command=lambda: show_pass(self.Show_but2,
                                                                                           self.Confirm_ent))
        self.Show_but2.grid(row=5, column=2, sticky='NSWE')


if __name__ == '__main__':
    root = Tk()
    layout = SignUp(root)
    root.mainloop()
