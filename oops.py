# Empty function
def product(self):
    pass


# empty class
class Warehouse:
    pass

# Object is an instance of a class

# Ojects has
# State - Variables & Variable Objects
# Behavior - Methods of an Object
# Identity - Uique name to an Object

# First object
obj = Warehouse()


# __init__ Method is a constructor
# Consutructor run as soon as an object is instantiated. It is used if we want anything to use in the object initiated.

class Bookswarehouse:
    def __init__(self, book):
        self.maths = book

    def books(self, science, physics):
        self.science = science
        self.physics = physics
        exam = self.science + ' '+self.physics
        # print(f"final exams for {exam}")
        return f"final exams for {exam}"

# booksobj = Bookswarehouse('maths')
# booksobj
# print(booksobj.maths)

# exambooks = booksobj.books('sci', 'phy')
# print(exambooks)

# Inheritence

# main or super class, so I'm using Object in main class
class Exam(object):
    def __init__(self, mathss, phy, sci):
        self.mathss = mathss
        self.phy = phy
        self.sci = sci

    def maths(self):
        finalmaths = f"Final marks for math is {self.mathss}"
        return finalmaths

    def phy(self):
        return f"Final marks for phy is {self.phy}"

    def sci(self):
        return f"Final marks for sci is {self.sci}"


class Subexam(Exam):

    def __init__(self, mathss, phy, sci, soc, tel):
        self.soc = soc
        self.tel = tel

        Exam.__init__(self, mathss, phy, sci)


    def finalmarks(self):
        final_sub = f"final marks are {self.mathss}, {self.phy}, {self.sci}, {self.tel}, {self.soc}"
        return final_sub

markings = Subexam('one', 'two', 'three', 'four', 'five')
maaths = markings.maths()
# print(maaths)




# Polymorphism
class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()


# Encapsulation
# demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
# obj1 = Base()
# print(obj1.a)

# obj2 = Derived()
# print(obj2.__c)

# Abstraction
from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,name):
        self.name = name

    def description(self):
        print("This the description function of class car.")

    @abstractmethod
    def price(self,x):
        print(f"The print of the main class********")

    def prices(self, name):
        print(f"The pring of prices of main is {self.name}")

    def test(self):
        print("Test main func")

class new(Car):
    def __init__(self, name, values):
        self.values = values

        Car.__init__(self, values)
    def price(self,name):
        print(f"The {self.name}'s price is {name} lakhs----.")

    def prices(self, values):
        print("Values are {values}")

    def test(self):
        print("Test child func")

obj = new("Honda City", 'Values are ')
obj.description()
obj.price(30)
obj.prices(11)
obj.test()

painobj = Car('name')
painobj.test()

