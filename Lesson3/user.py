class User:

    def __init__(self, firstName, lastName):
        self.userFN = firstName
        self.userLN = lastName

    def firstName(self):
        print(self.userFN)

    def lastName(self):
        print(self.userLN)

    def allName(self):
        print(self.userFN, self.userLN)
        