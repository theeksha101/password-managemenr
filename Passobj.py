from db import store_collec


class Passobj():
    def __init__(self, username, password, website, id=None, search_value=None):
        self.username = username
        self.password = password
        self.website = website
        self.collection = store_collec
        self.search_value = search_value
        self._id = id

    def accept(self):
        print("===================================================")
        self.username = input("Enter Username : ")
        self.password = input("Enter Password : ")
        self.website = input("Enter Website : ")
        print("===================================================")

    def save(self):
        self.collection.insert({"username": self.username,
                                "password": self.password,
                                "website": self.website})

        print("Saved !!")

    def delete(self):
        self.collection.remove({"username": self.username})

        print("Deleted !!")

    def update(self):
        self.collection.update_one({"username": self.username}, {"$set": {"username": self.username,
                                                                          "password": self.password,
                                                                          "website": self.website}})
        print("Updated !!")

    def search(self):
        result = self.collection.find({"$or": [{"username": self.search_value}, {"email": self.search_value}]})
        return result
