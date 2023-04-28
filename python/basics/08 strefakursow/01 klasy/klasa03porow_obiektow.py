class Person:
    def __init__(self, pname, surname, email, nickname):
        self.pname = pname
        self.surname = surname
        self.email = email
        self.nickname = nickname

    def printPersonInformation(self):
        print(f"Name: {self.pname}, Surname: {self.surname} \nemail: {self.email}, NICKNAME: {self.nickname}")