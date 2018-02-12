class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        self.other_person = other_person
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def contact_info(self):
        print('This is %s contact info email: %s and phone %s') % (self.name, self.email, self.phone)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
sonny.contact_info()
jordan.contact_info()

Class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def car_info(self)




