from db import checkLogin, getEntries, signupInsert, store_collec, login_collec
from Passobj import Passobj


class PasswordManager():
    def __init__(self):
        self.choice = 0
        self.sec_choice = 0
        self.entries = []
        self.printIntroForm()

    def printIntroForm(self):
        print("===================================================")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        self.choice = int(input("Enter Choice : "))
        print("===================================================")
        if (self.choice == 1):
            self.loginForm()
            self.printIntroForm()
        elif (self.choice == 2):
            self.signupForm()
        elif (self.choice == 3):
            exit(0)
        else:
            print("Invalid Choice")
            self.printIntroForm()

    def loginForm(self):
        print("===================================================")
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        print("===================================================")
        self._id = checkLogin(username, password)
        if self._id is not None:
            while self.sec_choice != 5:
                print("===================================================")
                print("1. Show All Passwords")
                print("2. Add Password")
                print("3. Edit Password")
                print("4. Delete Password")
                print("5. Search Password")
                print("6. Go Back")
                self.sec_choice = int(input("Enter Choice : "))
                print("===================================================")

                if self.sec_choice == 1:
                    self.printEntries(all=True)
                elif self.sec_choice == 2:
                    self.getEntry().save()
                elif self.sec_choice == 3:
                    self.getEntry(update=True)
                elif self.sec_choice == 4:
                    self.getEntry(delete=True)
                elif (self.sec_choice == 5):
                    website = input("Enter Website Name : ")
                    self.printEntries(all=False, website=website)
                elif (self.sec_choice == 6):
                    self._id = None
                    self.printIntroForm()

        else:
            print("Invalid Username / Password")

    def signupForm(self):
        print("===================================================")
        username = input("Enter Username : ")
        password = input("Enter Password : ")
        confirm_password = input("Confirm Password : ")
        email = input("Enter Email ID : ")
        print("===================================================")
        if (password == confirm_password):
            self._id = signupInsert(username, password, email)
            if (self._id is not None):
                self.loginForm()
            else:
                print("An account with given Username/password already exists")
                self.signupForm()
        else:
            print("Password and Confirm Password doesn't match")
            self.signupForm()

    def printEntries(self, all=True, website=None):
        self.entries = list(getEntries(self._id))
        print(self.entries)
        i = 1
        if (all):
            print("===================================================")
            for obj in self.entries:
                print("Password Index : " + str(i))
                print("Username : " + obj["username"])
                print("Password : " + obj["password"])
                print("Website : " + obj["website"])
                print("===================================================")
                i += 1
            return
        i = 0
        for obj in self.entries:
            i += 1
            if (website == obj["website"]):
                print("Password Index : " + str(i))
                print("Username : " + obj["username"])
                print("Password : " + obj["password"])
                print("Website : " + obj["website"])
                print("===================================================")

    def getEntry(self, update=False, delete=False):
        # self.printEntries(all=True)
        if (delete):
            index = int(input("Enter Password Index No : "))
            obj = self.entries[index - 1]
            return Passobj(self._id, obj["username"], obj["password"], obj["website"]).delete()

        if (update):
            index = int(input("Enter Password Index No : "))
            print("===================================================")
            username = input("Enter Username (Press Enter to keep previuos): ")
            password = input("Enter Password (Press Enter to keep previuos): ")
            website = input("Enter Website (Press Enter to keep previuos): ")
            print("===================================================")
            obj = self.entries[index - 1]
            return Passobj(self._id, obj["username"] if username == "" else username,
                           obj["password"] if password == "" else password,
                           obj["website"] if website == "" else website).update()

        print("===================================================")
        username = input("Enter Username ")
        password = input("Enter Password ")
        website = input("Enter Website ")
        print("===================================================")
        # return Passobj(self._id, username, password, website)
        return Passobj(username, password, website)


PasswordManager()
