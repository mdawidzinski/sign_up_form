from tkinter import messagebox


class UserValidator:
    def __init__(self, name, min_length, df):
        self.name = name
        self.min_length = min_length
        self.df = df

    def confirm(self):  # username min. length check
        if self.name == '':
            return messagebox.showerror('Invalid input', 'Username cannot be empty.')
        elif len(self.name) < self.min_length:
            return messagebox.showerror('Invalid input', 'Username too short.')
        else:
            return self.user_search()

    def user_search(self):  # check if username is available - binary search
        max_len = len(self.df['User']) - 1
        min_len = 0
        while min_len <= max_len:
            mid = (max_len + min_len) // 2
            if self.df['User'].values[mid] > self.name:
                max_len = mid - 1
            elif self.df['User'].values[mid] < self.name:
                min_len = mid + 1
            else:
                return messagebox.showerror('Username taken.', 'Sorry, this username is already taken.')
        return 1
