from faker import Faker

f = Faker()
f.name()

my_dict = {'name':f.name(), 'address':f.address(), 'email':f.email() }


class Person:
    def __init__(self, age=None):
        self.name = f.name()
        self.address = f.address()
        self.email = f.email()
        self.age = age

    def talk(self):
        print(f.word())

    def make_face(self):
        print(f.emoji())


first_person = Person()
second_person = Person(30)

print(f'Person one is {first_person.name} and the second person is {second_person.name}')

first_person.talk()
second_person.make_face()

