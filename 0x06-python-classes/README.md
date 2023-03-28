                          Note For PYTHON Classes
Python classes are a way of creating new types of objects that bundle data and functionality together. They allow you to define the attributes and methods of your own custom objects, as well as inherit from other classes or override their methods. Python classes are defined using the keyword class, followed by a name and a colon. Inside the class definition, you can use the special function init() to initialize the object’s state, and other functions to define the object’s behavior. You can also use the special function str() to control how the object is represented as a string. To create an instance of a class, you call the class name with parentheses and pass any arguments required by the init() function. To access or modify the object’s attributes or methods, you use the dot (.) operator. For example:

class Person: def init(self, name, age): self.name = name self.age = age

def str(self): return f"{self.name} ({self.age})"

def greet(self): print(f"Hello, my name is {self.name}.")

p1 = Person(“Alice”, 25) print(p1) # Alice (25) p1.greet() # Hello, my name is Alice.

This information is based on web search results

@PYTHON
The @ symbol in Python has two main uses: as a decorator and as a matrix multiplication operator. A decorator is a way of modifying or enhancing the behavior of a function or a class without changing its original code. It is usually written as @decorator_name before the function or class definition. A common example of a decorator is @property, which allows you to define getter and setter methods for a class attribute. A matrix multiplication operator is a way of performing matrix multiplication between two arrays or matrices. It is usually written as A @ B, where A and B are arrays or matrices. It was introduced in Python 3.5 as an alternative to the numpy.dot() function. This information is based on web search results
