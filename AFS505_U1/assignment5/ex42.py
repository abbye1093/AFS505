# animal is-a object
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ##??

        self.name = name

##??
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name
##??
class Person(object):

    def __init__(self, name):
        ##??
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

##??
class Fish(object):
    pass

##??
class Salmon(Fish):
    pass

##??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a pet satan
mary.pet = satan

## frank has a Employee name and salary
frank = Employee("Frank", 120000)

## frank has a pet rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()
