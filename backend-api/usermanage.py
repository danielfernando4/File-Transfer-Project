import json

class UserManager():
    def __init__(self):
        file = open("users.json", "r")
        self.users:list = json.load(file)
        file.close()


    def find_user(self, username: str) -> int:
        for pos, user in enumerate(self.users):
            if user["name"] == username:
                return pos 
        return -1


    def save_user(self, indent: int = 2):
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=indent)
            print("user saved succesfully!!")


    def create_user(self, username: str, key: str):
        if self.find_user(username) < 0:
            self.users.append(
                {
                    "name": username,
                    "key": key,
                    "directories":[],
                    "permissions":[] 
                }
            )
        self.save_user()


    def remove_user(self, username):
        pos = self.find_user(username)
        if pos >= 0:
            self.users.pop(pos)
        self.save_user()


    def validate_user():
        pass


    def assign_dir_user(self, username: str, dir_name: str):
        pos = self.find_user(username)
        if pos >= 0:
            self.users[pos]["directories"].append(dir_name)
        self.save_user()


    def remove_dir_user(self, username: str, dir_name: str):
        pos = self.find_user(username)
        if pos >= 0:
            self.users[pos]["permissions"].remove(dir_name)
        self.save_user()


    def grant_user(self, username: str, permission: str):
        pos = self.find_user(username)
        if pos >= 0:
            self.users[pos]["permissions"].append(permission)
        self.save_user()

    def revoke_user(self, username: str, permission: str):
        pos = self.find_user(username)
        if pos >= 0:
            self.users[pos]["permissions"].remove(permission)
        self.save_user()

    