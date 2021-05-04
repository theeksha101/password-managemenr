import tkinter as tk
from tkinter.messagebox import showinfo
from Record import Record
from db import checkLogin, getEntries, signupInsert


class UI:
    def __init__(self):
        self._root = tk.Tk()
        self._root.geometry("600x300")
        self._root.title('Password Manager')
        self.frame = tk.Frame(self._root)
        self.frame.pack(side="top", expand=True, fill="both")
        self.frame.config(background='white')
        self.entries = []
        self.msg = ''

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def start(self):
        self.clear()
        self.welcome_screen()

    def welcome_screen(self):
        self.clear()

        login_button = tk.Button(self.frame, text='Login', bg='white', font=('calibre', 12, 'bold'),
                                 command=self.login, width=20).place(x=210, y=50)
        sign_up = tk.Button(self.frame, text='Sign Up', bg='white', font=('calibre', 12, 'bold'),
                            command=self.sign_up, width=20).place(x=210, y=100)
        go_back = tk.Button(self.frame, text='Exit', bg='white', font=('calibre', 12, 'bold'),
                            command=self.frame.destroy, width=20).place(x=210, y=150)

        self.frame.mainloop()

    def show_options(self):
        self.clear()

        button_show_pass = tk.Button(self.frame, text='Show All Entries', bg='white', font=('calibre', 12, 'bold'),
                                     command=lambda: self.show_entries(all=True), width=20).place(x=210, y=30)
        button_add_pass = tk.Button(self.frame, text='Add Password', bg='white', font=('calibre', 12, 'bold'), width=20,
                                    command=lambda: self.show_add_record_menu()).place(x=210, y=80)
        button_delete_pass = tk.Button(self.frame, text='Delete Entry', bg='white', font=('calibre', 12, 'bold'),
                                       command=lambda: self.show_delete_menu(), width=20).place(x=210, y=130)
        button_go_back = tk.Button(self.frame, text='Go Back', bg='white', font=('calibre', 12, 'bold'),
                                   command=self.login, width=20).place(x=210, y=180)

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
            invalid_label = tk.Label(self.frame, text='Username or Password is wrong!!', fg='red',
                                     font=('calibre', 10, 'bold')).place(x=200, y=70)
            login_again_button = tk.Button(self.frame, text='Try Again?', bg='white', font=('calibre', 10, 'bold'),
                                           command=self.login).place(x=190, y=140)
            sign_up = tk.Button(self.frame, text='Sign Up?', bg='white', font=('calibre', 10, 'bold'),
                                command=self.sign_up).place(x=330, y=140)

            self.frame.mainloop()

    def login(self):
        self.clear()

        name_var = tk.StringVar()
        passw_var = tk.StringVar()

        login_msg = tk.Label(self.frame, text='Login', fg='maroon', bg='white', font=('calibre', 15, 'bold')).place(
            x=250, y=30)
        name_label = tk.Label(self.frame, text='Username', bg='white', font=('calibre', 12, 'bold')).place(x=180, y=80)
        name_entry = tk.Entry(self.frame, textvariable=name_var, font=('calibre', 12, 'normal')).place(x=280, y=80)
        name_var.set("diksha")
        passw_label = tk.Label(self.frame, text='Password', bg='white',
                               font=('calibre', 12, 'bold')).place(x=180, y=115)
        passw_entry = tk.Entry(self.frame, textvariable=passw_var,
                               font=('calibre', 12, 'normal'), show='*').place(x=280, y=115)
        passw_var.set('0000')
        sub_btn = tk.Button(self.frame, text='Login', font=('calibre', 11, 'bold'),
                            command=lambda: self.on_login(name_var, passw_var)).place(x=250, y=170)
        go_back = tk.Button(self.frame, text='Exit', font=('calibre', 11, 'bold'),
                            command=self.welcome_screen).place(x=350, y=170)
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

        sign_up_msg = tk.Label(self.frame, text='Sign Up ', fg='blue', bg='white',
                               font=('calibre', 17, 'bold')).place(x=270, y=20)

        email_label = tk.Label(self.frame, text="Email", bg='white',
                               font=('calibre', 10, 'bold')).place(x=160, y=80)
        email_entry = tk.Entry(self.frame, textvariable=email, width=30,
                               font=('calibre', 10, 'normal')).place(x=310, y=80)

        name_label = tk.Label(self.frame, text='Username', bg='white',
                              font=('calibre', 10, 'bold')).place(x=160, y=120)
        name_entry = tk.Entry(self.frame, textvariable=name_var, width=30,
                              font=('calibre', 10, 'normal')).place(x=310, y=120)

        passw_label = tk.Label(self.frame, text='Password', bg='white',
                               font=('calibre', 10, 'bold')).place(x=160, y=160)
        passw_entry = tk.Entry(self.frame, textvariable=passw_var, width=30,
                               font=('calibre', 10, 'normal'), show='*').place(x=310, y=160)

        conf_passw_label = tk.Label(self.frame, text='Confirm Password', bg='white',
                                    font=('calibre', 10, 'bold')).place(x=160, y=200)
        conf_passw_entry = tk.Entry(self.frame, textvariable=conf_passw_var, width=30,
                                    font=('calibre', 10, 'normal'), show='*').place(x=310, y=200)

        sign_up = tk.Button(self.frame, text='Sign Up', bg='white', font=('calibre', 11, 'bold'),
                            command=lambda: self.on_sign_up(name_var, passw_var, conf_passw_var, email)).place(x=250, y=240)
        go_back = tk.Button(self.frame, text='Exit', font=('calibre', 11, 'bold'), bg='white',
                            command=self.welcome_screen).place(x=350, y=240)

        self.frame.mainloop()

    def show_entries(self, all=True):

        self.clear()
        # TODO: add PanedWindow to show list of buttons, beside them add Entries which will be editable and save changes
        #  button down those entries.
        search_value = tk.StringVar()

        paned_window = tk.PanedWindow(self.frame, orient=tk.VERTICAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        top_frame = tk.Frame(paned_window, width=300, height=20, relief=tk.SUNKEN)

        search_label = tk.Label(top_frame, text='Search entry by website', font=('calibre', 15, 'bold'))
        search_entry = tk.Entry(top_frame, textvariable=search_value, bd=4, width=50,
                                font=('calibre', 10, 'normal'))
        search_button = tk.Button(top_frame, text='Search Entry', bg='white', bd=3, font=('calibre', 12, 'bold'),
                                  width=50,
                                  command=lambda: self.search(search_value))

        search_label.pack(side=tk.TOP, fill=tk.BOTH)
        search_entry.pack(side=tk.LEFT, ipadx=0, ipady=0, fill=tk.BOTH, expand=True)
        search_button.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.entries = list(getEntries(self._id))

        bottom_frame = tk.Frame(paned_window, width=300, height=500, relief=tk.SUNKEN)

        listbox = tk.Listbox(bottom_frame, width=40)
        scrollbar = tk.Scrollbar(bottom_frame)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        name_label = tk.Label(bottom_frame, text='Username', font=('calibre', 12, 'bold'))
        name_var = tk.StringVar()
        name = tk.Entry(bottom_frame, bd=4, width=50, textvariable=name_var,
                        font=('calibre', 10, 'normal'))

        pass_label = tk.Label(bottom_frame, text='Password', font=('calibre', 12, 'bold'))
        password_var = tk.StringVar()
        passw = tk.Entry(bottom_frame, bd=4, width=50, textvariable=password_var,
                         font=('calibre', 10, 'normal'))

        web_label = tk.Label(bottom_frame, text='Website', font=('calibre', 12, 'bold'))
        web_var = tk.StringVar()
        web = tk.Label(bottom_frame, bd=5, width=50, textvariable=web_var, bg='white',
                       font=('calibre', 11, 'normal'))

        name_label.pack(side=tk.TOP, fill=tk.BOTH)
        name.pack(side=tk.TOP, fill=tk.BOTH)
        pass_label.pack(side=tk.TOP, fill=tk.BOTH)
        passw.pack(side=tk.TOP, fill=tk.BOTH)
        web_label.pack(side=tk.TOP, fill=tk.BOTH)
        web.pack(side=tk.TOP, fill=tk.BOTH)
        back = tk.Button(bottom_frame, text='Back', bg='white', bd=4, font=('calibre', 12, 'bold'),
                         command=self.show_options)
        update_button = tk.Button(bottom_frame, text='Update', bd=4, font=('calibre', 12, 'bold'),
                                  command=lambda: self.update(name_var.get(), password_var.get(), web_var.get())
                                  )

        back.pack(side=tk.BOTTOM, fill=tk.BOTH)
        update_button.pack(side=tk.BOTTOM, fill=tk.BOTH)
        i = 0
        if all:
            for obj in self.entries:
                web_name = obj['website']
                listbox.insert(i, web_name)
                i += 1

        paned_window.add(top_frame)
        paned_window.add(bottom_frame)

        def items_selected(event):

            selected_indices = listbox.curselection()

            selected_langs = ",".join([listbox.get(i) for i in selected_indices])
            self.msg = selected_langs

            result = list(Record(username='', password='', website='', search_value=self.msg).search())
            dictionary = result[0]

            user_name = dictionary['username']
            password = dictionary['password']
            website = dictionary['website']

            name_var.set(user_name)
            password_var.set(password)
            web_var.set(website)

        listbox.bind('<<ListboxSelect>>', items_selected)

    def show_delete_menu(self):
        self.clear()
        name_var = tk.StringVar()

        delete_label = tk.Label(self.frame, text='Enter the user name you want to delete', fg='red', bg='white',
                                font=('calibre', 15, 'bold')).place(x=100, y=30)

        name_label = tk.Label(self.frame, text='Username', bg='white',
                              font=('calibre', 12, 'bold')).place(x=150, y=80)
        name_entry = tk.Entry(self.frame, textvariable=name_var,
                              font=('calibre', 12, 'normal')).place(x=270, y=80)

        delete_button = tk.Button(self.frame, text='Delete', bg='white', font=('calibre', 10, 'bold'),
                                  command=lambda: self.on_delete(name_var)).place(x=250, y=150)
        back_btn = tk.Button(self.frame, text='Back', font=('calibre', 11, 'bold'), bg='white',
                             command=self.show_options).place(x=360, y=150)

    def show_add_record_menu(self):
        self.clear()
        name_var = tk.StringVar()
        passw_var = tk.StringVar()
        email = tk.StringVar()

        add_label = tk.Label(self.frame, text='Enter Username and Password', bg='white',
                             font=('calibre', 15, 'bold')).place(x=200, y=30)
        name_label = tk.Label(self.frame, text='Username', bg='white',
                              font=('calibre', 12, 'bold')).place(x=180, y=80)
        name_entry = tk.Entry(self.frame, textvariable=name_var,
                              font=('calibre', 12, 'normal')).place(x=280, y=80)
        passw_label = tk.Label(self.frame, text='Password', bg='white',
                               font=('calibre', 12, 'bold')).place(x=180, y=115)
        passw_entry = tk.Entry(self.frame, textvariable=passw_var,
                               font=('calibre', 12, 'normal'), show='*').place(x=280, y=115)
        email_label = tk.Label(self.frame, text='Website', bg='white',
                               font=('calibre', 12, 'bold')).place(x=180, y=150)
        email_entry = tk.Entry(self.frame, textvariable=email,
                               font=('calibre', 12, 'normal')).place(x=280, y=150)
        sub_btn = tk.Button(self.frame, text='Save', font=('calibre', 11, 'bold'),
                            command=lambda: self.add(name_var.get(), passw_var.get(), email.get())).place(x=260, y=190)
        back_btn = tk.Button(self.frame, text='Back', font=('calibre', 11, 'bold'),
                             command=self.show_options).place(x=350, y=190)

    def search(self, search):
        self.clear()
        search_value = search.get()
        result = list(Record(username='', password='', website='', search_value=search_value).search())
        print(result)
        i = 1
        for dictionary in result:
            if dictionary['website'] == search_value:
                my_string_var = dictionary["username"]
                username = tk.Label(self.frame, text='Username: ' + my_string_var, bg='white',
                                    font=('calibre', 10, 'bold'))
                my_string_var = dictionary["password"]
                password = tk.Label(self.frame, text='Password: ' + my_string_var, bg='white',
                                    font=('calibre', 10, 'bold'))
                my_string_var = dictionary["website"]
                website = tk.Label(self.frame, text='website: ' + my_string_var, bg='white',
                                   font=('calibre', 10, 'bold'))
                partition = tk.Label(self.frame, text='===========================')

                username.grid(row=i, column=0)
                i += 1
                password.grid(row=i, column=0)
                i += 1
                website.grid(row=i, column=0)
                i += 1
                partition.grid(row=i, column=0)
                i += 1
            elif dictionary['website'] != search_value:
                showinfo(message='**No such entry**')

        go_back = tk.Button(self.frame, text='Back', font=('calibre', 10, 'bold'), command=self.show_entries)
        go_back.grid(row=6, column=0)

    def show(self, website):
        website = website.get()
        Record(username='', password='', website=website).delete()

        saved_msg = tk.Label(self.frame, text='Deleted !', font=('calibre', 10, 'bold'))
        go_back = tk.Button(self.frame, text='Go Back', command=self.show_options)

        saved_msg.grid(row=0, column=0)
        go_back.grid(row=1, column=1)

    def add(self, username, password, website):

        if username == "" or password == "":
            showinfo(
                title='Error',
                message='Username Password can not be empty')
        else:
            Record(username, password, website).save()
            showinfo(message='Information has been saved successfully')

        # Record(user_name, pass_word, website).save()

        # saved_msg = tk.Label(self.frame, text='Entry saved successfully!!', fg='green',
        #                      font=('calibre', 15, 'bold')).place(x=250, y=50)
        # go_back = tk.Button(self.frame, text='Go Back', command=self.show_options).place(x=250, y=100)

    def on_delete(self, username):
        username = username.get()
        if username == "":
            showinfo(
                title='Error',
                message='Username can not be empty')
        else:
            Record(username, password='', website='').save()
            showinfo(message='Information has been successfully deleted')
        # Record(username, password='', website='').delete()
        #
        # saved_msg = tk.Label(self.frame, text='Entry by the name ' + username + ' has been deleted',
        #                      font=('calibre', 10, 'bold'))
        # go_back = tk.Button(self.frame, text='Go Back', command=self.show_options, font=('calibre', 10, 'bold'))
        #
        # saved_msg.grid(row=4, column=0)
        # go_back.grid(row=3, column=2)

    def update(self, name_var, pass_var, website):
        msg = 'Entry Updated!'

        if name_var.strip() == "" or pass_var.strip() == "":
            msg = "Username, password cannot be empty"
        else:
            Record(name_var, pass_var, website).update()

        showinfo(
            title='Information',
            message=msg)


if __name__ == '__main__':
    ui = UI()
    ui.start()
