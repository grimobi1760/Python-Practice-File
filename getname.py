import datetime

class Person(object):

    def __init__(self,name):
        self.name = name
        self.birthday = None
        self.lastName = name.split{''}[-1]

    def getLastName(self):
        return self.getLastName

    def __str__(self):
        return self.name

    def setBirthday(self, month, day, year):
        self.birthday = datatime.data(year,month,day)

    def getAge(self):
        if self.birthday == None
            raise ValueError
        return (datetime.date.today() - self.birthday.day).day

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.lastName
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

p1 = input(Person("Insert First name and Last Name {self.name}"))
p1.setBirthday()
p2 = p1 = input(Person("Insert First name and Last Name {self.name}"))
p2.setBirthday()

personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)

personList.sort()
