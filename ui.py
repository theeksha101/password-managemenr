import tkinter as tk
from tkinter import RIGHT, Y

from db import checkLogin, getEntries, signupInsert, store_collec, login_collec
from Passobj import Passobj


class UI:
    def __init__(self):
        self._root = tk.Tk()
        self._root.geometry("600x300")
        self._root.title('Password Manager')
        self.frame = tk.Frame(self._root)
        self.frame.pack(side="top", expand=True, fill="both")
        self.frame.config(background='white')
        self.entries = []

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def start(self):
        self.clear()
        self.welcome_screen()

    def welcome_screen(self):
        self.clear()

        login_button = tk.Button(self.frame, text='Login', bg='white', command=self.login).place(x=250, y=50)
        sign_up = tk.Button(self.frame, text='Sign Up', bg='white', command=self.sign_up).place(x=250, y=100)
        go_back = tk.Button(self.frame, text='Exit', bg='white', command=self.frame.destroy).place(x=250, y=150)

        # login_button.grid(row=0, column=1)
        # sign_up.grid(row=1, column=1)
        # go_back.grid(row=2, column=1)

        self.frame.mainloop()

    def show_options(self):
        self.clear()

        button_show_pass = tk.Button(self.frame, text='Show All Entries', font=('calibre', 10, 'bold'),
                                     command=lambda: self.printEntries(all=True))
        button_add_pass = tk.Button(self.frame, text='Add Password', font=('calibre', 10, 'bold'),
                                    command=lambda: self.getEntry())
        button_edit_pass = tk.Button(self.frame, text='Edit Entry', font=('calibre', 10, 'bold'),
                                     command=lambda: self.getEntry(update=True))
        button_delete_pass = tk.Button(self.frame, text='Delete Entry', font=('calibre', 10, 'bold'),
                                       command=lambda: self.getEntry(delete=True))
        button_go_back = tk.Button(self.frame, text='Go Back', font=('calibre', 10, 'bold'), command=self.login)

        button_show_pass.grid(row=0, column=0)
        button_add_pass.grid(row=1, column=0)
        button_edit_pass.grid(row=2, column=0)
        button_delete_pass.grid(row=0, column=2)
        button_go_back.grid(row=2, column=2)

        self.frame.mainloop()

    def on_login(self, name_var, passw_var):
        self.clear()
        username = name_var.get()
        password = passw_var.get()
        print(self.entries)
        self._id = checkLogin(username, password)
        if self._id is not None:
            self.show_options()
        else:
            invalid_label = tk.Label(self.frame, text='Username or Password is wrong!!', font=('calibre', 10, 'bold'))
            login_again_button = tk.Button(self.frame, text='Try Again?', font=('calibre', 10, 'bold'),
                                           command=self.login)
            sign_up = tk.Button(self.frame, text='Sign Up?', command=self.sign_up)

            invalid_label.grid(row=1, column=1)
            login_again_button.grid(row=2, column=1)
            sign_up.grid(row=3, column=1)

            self.frame.mainloop()

    def login(self):
        self.clear()

        name_var = tk.StringVar()
        passw_var = tk.StringVar()

        login_msg = tk.Label(self.frame, text='Login', bg='white', font=('calibre', 10, 'bold'))
        name_label = tk.Label(self.frame, text='Username', bg='white', font=('calibre', 10, 'bold'))
        name_entry = tk.Entry(self.frame, textvariable=name_var, font=('calibre', 10, 'normal'))
        passw_label = tk.Label(self.frame, text='Password',  bg='white', font=('calibre', 10, 'bold'))
        passw_entry = tk.Entry(self.frame, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
        sub_btn = tk.Button(self.frame, text='Login', command=lambda: self.on_login(name_var, passw_var))
        go_back = tk.Button(self.frame, text='Exit', command=self.frame.destroy)

        login_msg.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        name_entry.grid(row=1, column=1)
        passw_label.grid(row=2, column=0)
        passw_entry.grid(row=2, column=1)
        sub_btn.grid(row=3, column=1)
        go_back.grid(row=3, column=2)

        self.frame.mainloop()

    def on_sign_up(self, user_name, passw, conf_password, email_add):
        self.clear()

        username = user_name.get()
        password = passw.get()
        confirm_password = conf_password.get()
        email = email_add.get()

        if password == confirm_password:
            self._id = signupInsert(username, password, email)
            if self._id is not None:
                sign_up_done = tk.Label(self.frame, text='Sign Up Successful', font=('calibre', 10, 'bold'))
                login = tk.Button(self.frame, text='Login Now', font=('calibre', 10, 'bold'), command=self.login)

                sign_up_done.grid(row=1, column=2)
                login.grid(row=2, column=2)

                self.frame.mainloop()
            else:
                error = tk.Label(self.frame, text='An account with given Username already exists',
                                 font=('calibre', 10, 'bold'))
                try_again = tk.Button(self.frame, text='Try again?', font=('calibre', 10, 'bold'), command=self.sign_up)
                exit_now = tk.Button(self.frame, text='Exit?', font=('calibre', 10, 'bold'),
                                     command=self.welcome_screen)

                error.grid(row=1, column=2)
                try_again.grid(row=2, column=2)
                exit_now.grid(row=3, column=2)

                self.frame.mainloop()
        else:
            error = tk.Label(self.frame, text='Password and Confirm Password does not match',
                             font=('calibre', 10, 'bold'))
            try_again = tk.Button(self.frame, text='Try again?', font=('calibre', 10, 'bold'), command=self.sign_up)

            error.grid(row=1, column=2)
            try_again.grid(row=2, column=2)

            self.frame.mainloop()

    def sign_up(self):
        self.clear()
        name_var = tk.StringVar()
        passw_var = tk.StringVar()
        email = tk.StringVar()
        conf_passw_var = tk.StringVar()

        sign_up_msg = tk.Label(self.frame, text='Sign Up !! ', font=('calibre', 10, 'bold'))

        email_label = tk.Label(self.frame, text="Email", font=('calibre', 10, 'bold'))
        email_entry = tk.Entry(self.frame, textvariable=email, font=('calibre', 10, 'normal'))

        name_label = tk.Label(self.frame, text='Username', font=('calibre', 10, 'bold'))
        name_entry = tk.Entry(self.frame, textvariable=name_var, font=('calibre', 10, 'normal'))

        passw_label = tk.Label(self.frame, text='Password', font=('calibre', 10, 'bold'))
        passw_entry = tk.Entry(self.frame, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

        conf_passw_label = tk.Label(self.frame, text='Confirm Password', font=('calibre', 10, 'bold'))
        conf_passw_entry = tk.Entry(self.frame, textvariable=conf_passw_var, font=('calibre', 10, 'normal'), show='*')

        sign_up = tk.Button(self.frame, text='Sign Up',
                            command=lambda: self.on_sign_up(name_var, passw_var, conf_passw_var, email))

        sign_up_msg.grid(row=0, column=0)
        email_label.grid(row=1, column=0)
        email_entry.grid(row=1, column=1)
        name_label.grid(row=2, column=0)
        name_entry.grid(row=2, column=1)
        passw_label.grid(row=3, column=0)
        passw_entry.grid(row=3, column=1)
        conf_passw_label.grid(row=4, column=0)
        conf_passw_entry.grid(row=4, column=1)
        sign_up.grid(row=6, column=1)

        self.frame.mainloop()

    def printEntries(self, all=True, website=None):
        self.clear()

        search_value = tk.StringVar()
        search_label = tk.Label(self.frame, text='Search entry by username', font=('calibre', 10, 'bold'))
        search_entry = tk.Entry(self.frame, textvariable=search_value, font=('calibre', 10, 'normal'))
        search_button = tk.Button(self.frame, text='Search Entry', font=('calibre', 10, 'bold'),
                                  command=lambda: self.search(search_value))

        search_label.grid(row=0, column=0)
        search_entry.grid(row=1, column=0)
        search_button.grid(row=1, column=1)

        back = tk.Button(self.frame, text='Back', font=('calibre', 10, 'bold'), command=self.show_options)
        self.entries = list(getEntries(self._id))
        print(self.entries)
        i = 2
        if all:
            for obj in self.entries:
                my_string_var = obj["username"]
                username = tk.Label(self.frame, text='Username: ' + my_string_var, font=('calibre', 10, 'bold'))
                my_string_var = obj["password"]
                password = tk.Label(self.frame, text='Password: ' + my_string_var, font=('calibre', 10, 'bold'))
                my_string_var = obj["website"]
                website = tk.Label(self.frame, text='website: ' + my_string_var, font=('calibre', 10, 'bold'))
                partition = tk.Label(self.frame, text='===========================')

                username.grid(row=i, column=0)
                i += 1
                password.grid(row=i, column=0)
                i += 1
                website.grid(row=i, column=0)
                i += 1
                partition.grid(row=i, column=0)
                i += 1
            back.grid(row=4, column=1)

            return

    def getEntry(self, update=False, delete=False):
        self.clear()

        if delete:
            name_var = tk.StringVar()

            delete_label = tk.Label(self.frame, text='Enter the user name you want to delete',
                                    font=('calibre', 11, 'bold'))

            name_label = tk.Label(self.frame, text='Username', font=('calibre', 10, 'bold'))
            name_entry = tk.Entry(self.frame, textvariable=name_var, font=('calibre', 10, 'normal'))

            delete_button = tk.Button(self.frame, text='Delete', font=('calibre', 10, 'bold'),
                                      command=lambda: self.delete(name_var))

            delete_label.grid(row=0, column=0)
            name_label.grid(row=1, column=0)
            name_entry.grid(row=2, column=0)
            delete_button.grid(row=3, column=0)
            return

        if update:
            self.clear()

            name_var = tk.StringVar()
            passw_var = tk.StringVar()
            email = tk.StringVar()

            name_label = tk.Label(self.frame, text='Username', font=('calibre', 10, 'bold'))
            name_entry = tk.Entry(self.frame, textvariable=name_var, font=('calibre', 10, 'normal'))
            passw_label = tk.Label(self.frame, text='Password', font=('calibre', 10, 'bold'))
            passw_entry = tk.Entry(self.frame, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
            email_label = tk.Label(self.frame, text='Website', font=('calibre', 10, 'bold'))
            email_entry = tk.Entry(self.frame, textvariable=email, font=('calibre', 10, 'normal'))
            sub_btn = tk.Button(self.frame, text='Update',
                                command=lambda: self.update(name_var, passw_var, email))
            print(self.entries)
            name_label.grid(row=1, column=0)
            name_entry.grid(row=1, column=1)
            passw_label.grid(row=2, column=0)
            passw_entry.grid(row=2, column=1)
            email_label.grid(row=3, column=0)
            email_entry.grid(row=3, column=1)
            sub_btn.grid(row=4, column=1)

        else:
            self.clear()
            name_var = tk.StringVar()
            passw_var = tk.StringVar()
            email = tk.StringVar()

            name_label = tk.Label(self.frame, text='Username', font=('calibre', 10, 'bold'))
            name_entry = tk.Entry(self.frame, textvariable=name_var, font=('calibre', 10, 'normal'))
            passw_label = tk.Label(self.frame, text='Password', font=('calibre', 10, 'bold'))
            passw_entry = tk.Entry(self.frame, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
            email_label = tk.Label(self.frame, text='Website', font=('calibre', 10, 'bold'))
            email_entry = tk.Entry(self.frame, textvariable=email, font=('calibre', 10, 'normal'))
            sub_btn = tk.Button(self.frame, text='Save', command=lambda: self.add(name_var, passw_var, email))

            name_label.grid(row=1, column=0)
            name_entry.grid(row=1, column=1)
            passw_label.grid(row=2, column=0)
            passw_entry.grid(row=2, column=1)
            email_label.grid(row=3, column=0)
            email_entry.grid(row=3, column=1)
            sub_btn.grid(row=4, column=1)
        return

    def search(self, search):
        self.clear()
        search_value = search.get()
        result = list(Passobj(username='', password='', website='', search_value=search_value).search())
        i = 1
        for dictionary in result:
            if dictionary['username'] == search_value:
                my_string_var = dictionary["username"]
                username = tk.Label(self.frame, text='Username: ' + my_string_var, font=('calibre', 10, 'bold'))
                my_string_var = dictionary["password"]
                password = tk.Label(self.frame, text='Password: ' + my_string_var, font=('calibre', 10, 'bold'))
                my_string_var = dictionary["website"]
                website = tk.Label(self.frame, text='website: ' + my_string_var, font=('calibre', 10, 'bold'))
                partition = tk.Label(self.frame, text='===========================')

                username.grid(row=i, column=0)
                i += 1
                password.grid(row=i, column=0)
                i += 1
                website.grid(row=i, column=0)
                i += 1
                partition.grid(row=i, column=0)
                i += 1
        go_back = tk.Button(self.frame, text='Back', font=('calibre', 10, 'bold'), command=self.show_options)
        go_back.grid(row=1, column=2)

    def show(self, website):
        website = website.get()
        Passobj(username='', password='', website=website).delete()

        saved_msg = tk.Label(self.frame, text='Deleted !', font=('calibre', 10, 'bold'))
        go_back = tk.Button(self.frame, text='Go Back', command=self.show_options)

        saved_msg.grid(row=0, column=0)
        go_back.grid(row=1, column=1)

    def add(self, username, password, website):
        self.clear()
        user_name = username.get()
        pass_word = password.get()
        website = website.get()

        Passobj(user_name, pass_word, website).save()

        saved_msg = tk.Label(self.frame, text='Saved !', font=('calibre', 10, 'bold'))
        go_back = tk.Button(self.frame, text='Go Back', command=self.show_options)

        saved_msg.grid(row=0, column=1)
        go_back.grid(row=4, column=2)

    def delete(self, username):
        username = username.get()
        Passobj(username, password='', website='').delete()

        saved_msg = tk.Label(self.frame, text='Entry by the name ' + username + ' has been deleted',
                             font=('calibre', 10, 'bold'))
        go_back = tk.Button(self.frame, text='Go Back', command=self.show_options, font=('calibre', 10, 'bold'))

        saved_msg.grid(row=4, column=0)
        go_back.grid(row=3, column=2)

    def update(self, name_var, pass_var, email):
        self.clear()

        username = name_var.get()
        password = pass_var.get()
        website = email.get()

        Passobj(username, password, website).update()

        updated_msg = tk.Label(self.frame, text='Password Updated!', font=('calibre', 10, 'bold'))
        go_back = tk.Button(self.frame, text='Go Back', command=self.show_options)

        updated_msg.grid(row=0, column=1)
        go_back.grid(row=4, column=2)


if __name__ == '__main__':
    ui = UI()
    ui.start()
