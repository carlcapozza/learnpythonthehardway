## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal, or rather Dog is a type of Animal
class Dog(Animal):
    def __init__(self, name):
    ## Self is an instance of a Dog
    self.name  

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat is an instance of a Cat
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Intialize the person object with a name.
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Create a person that has a name and a salary
        super(Employee, self).__init__(name)
        ## Set the persons salary to the passed value of salary.
        self.salary = salary

## Fish is a object
class Fish(object):
    pass

## Salmon is a type of Fish
class Salmon(Fish):
    pass

## Halibut is a type of Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has a pet named satan
mary.pet = satan

## frank is a Employee who earns 120000 
frank = Employee("Frank", 120000)

## frank also has a dog name rover
frank.pet = rover

## flipper is a Fish 
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is Fish
harry = Halibut()