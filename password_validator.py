from tkinter import messagebox
from string import punctuation


class PasswordValidator:
    def __init__(self, password, password_confirmation):
        self.password = password
        self.password_confirmation = password_confirmation

    def pass_validation(self):
        if len(self.password) == 0:
            return messagebox.showerror('Invalid password', 'Please insert password')
        if len(self.password) < 8:
            return messagebox.showerror('Invalid password', 'Password too short')
        rules = [0, 0, 0]
        for i in self.password:
            if i.isalpha():
                rules[0] += 1
            elif i.isdigit():
                rules[1] += 1
            elif i in punctuation:
                rules[2] += 1
            else:
                return messagebox.showerror('Error', 'Invalid input')

        if not all(rules):
            return messagebox.showerror('Invalid password', 'Password must contain at least 1 letter,'
                                                            ' 1 number and 1 special character.')

        if self.password != self.password_confirmation:  # check if both passwords are the same
            return messagebox.showerror('Invalid input', 'Passwords don\'t match.')
        else:
            return 1
