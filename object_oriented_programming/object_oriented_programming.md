<!--
module_id: object_oriented_programming
author: Amir Kayhani
email: amir.kayhani@warwick.ac.uk
version: 1.1.0
current_version_description: Expanded version with detailed explanations and comprehensive examples for object-oriented programming in Python.
module_type: standard
docs_version: 1.1.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Object-Oriented Programming

comment: Learn the fundamentals of object-oriented programming in Python with detailed explanations and examples.

long_description: This module introduces learners to object-oriented programming (OOP) in Python. It covers the basics of classes and objects, as well as advanced OOP concepts such as inheritance, polymorphism, encapsulation, and abstraction. Detailed explanations and examples are provided to ensure a deep understanding of the concepts.

estimated_time_in_minutes: 90

@pre_reqs
Learners should be familiar with [basic Python syntax](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1) and [functions in Python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/functions_in_python/functions_in_python.md#1).
@end

@learning_objectives

- Understand the concepts of classes and objects.
- Implement inheritance, polymorphism, encapsulation, and abstraction in Python.
- Use OOP principles to design robust and reusable code.
- Apply advanced OOP techniques to solve real-world problems.

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_variables_functions_methods
coding_required: true
coding_level: intermediate
coding_language: python

@sets_you_up_for

- advanced_oop_exercises
- design_patterns_in_python

@end

@depends_on_knowledge_available_in

- python_basics_variables_functions_methods
- functions_in_python

@end

@version_history

Previous versions: 

- 1.0.0: Initial version introducing object-oriented programming concepts in Python.
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Python Basics: Object-Oriented Programming

@overview

In this module, you will learn the fundamentals of object-oriented programming (OOP) in Python. OOP is a programming paradigm that organizes code into reusable "blueprints" called classes. By the end of this module, you will be able to design and implement Python programs using OOP principles.

## Attribution

@attribution

## Lesson Preparation

@lesson_prep_python_pyodide

## Introduction

Object-oriented programming (OOP) is a powerful paradigm that allows you to structure your code into reusable and modular components. In Python, OOP is implemented using classes and objects. 

### Why Learn Object-Oriented Programming?

Imagine you're building a large software system like a hospital management system, an e-commerce platform, or a video game. Without OOP, your code would be a tangled mess of functions and variables scattered everywhere. OOP provides a way to organize code that mirrors how we think about the real world.

**Real-World Analogy:**
Think of a car manufacturing company. They don't build each car from scratch. Instead, they have:
- **Blueprints** (Classes) that define what a car should have
- **Actual Cars** (Objects) built from those blueprints
- **Different Models** (Inheritance) that share common features but have unique characteristics
- **Standard Interfaces** (Polymorphism) so any driver can operate any car
- **Hidden Complexity** (Encapsulation) - you don't need to know how the engine works to drive

### The Four Pillars of OOP

This module will cover the fundamental principles of OOP:

1. **Encapsulation**: Bundling data and methods together, hiding internal details
2. **Inheritance**: Creating new classes based on existing ones
3. **Polymorphism**: Using a single interface to represent different types
4. **Abstraction**: Hiding complex implementation details, showing only what's necessary

![Object-Oriented Programming Concepts](https://miro.medium.com/v2/da:true/resize:fit:1200/0*UmrkxwwbEt9WANMo)

### Real-World Applications of OOP

OOP is used extensively in:
- **Web Development**: Django, Flask frameworks use OOP for models and views
- **Game Development**: Characters, weapons, and items are objects
- **AI/Machine Learning**: Scikit-learn, Tensorflow and Pytorch models are objects with fit() and predict() methods
- **GUI Applications**: Buttons, windows, and menus are objects
- **Database Systems**: ORMs (Object-Relational Mappers) map database tables to objects
- **Mobile Apps**: iOS and Android development heavily rely on OOP

---

## Why Object-Oriented Programming Matters

Before diving into the details, let's understand WHY we need OOP through a practical example.

### Problem Without OOP

Imagine managing a school system without OOP:

```python
# Without OOP - messy and hard to maintain
student1_name = "Alice"
student1_age = 20
student1_grade = 85
student1_courses = ["Math", "Physics"]

student2_name = "Bob"
student2_age = 21
student2_grade = 90
student2_courses = ["Chemistry", "Biology"]

def calculate_average(grade):
    return grade

def enroll_course(courses_list, course_name):
    courses_list.append(course_name)
    return courses_list

# Hard to manage many students!
# What if we need 100 students?
# How do we ensure data consistency?
```

### Solution With OOP

```python
# With OOP - organized and scalable
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []
    
    def enroll_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} enrolled in {course_name}")
    
    def get_status(self):
        return "Pass" if self.grade >= 60 else "Fail"

# Creating students is clean and simple
students = [
    Student("Alice", 20, 85),
    Student("Bob", 21, 90),
    Student("Charlie", 19, 78)
]

# Easy to manage many students
for student in students:
    student.enroll_course("Computer Science")
    print(f"{student.name}: {student.get_status()}")
```
@Pyodide.eval

**Benefits of OOP Approach:**
1. **Organization**: Related data and functions are grouped together
2. **Reusability**: Create multiple students using the same class
3. **Maintainability**: Changes to Student class affect all students
4. **Scalability**: Easy to add new students or features
5. **Data Integrity**: Methods ensure data is modified correctly

---

## Classes and Objects

Classes are blueprints for creating objects. Objects are instances of classes that encapsulate data and behavior. For example:

### What is a Class?
A class is a user-defined data structure that acts as a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")
```
@Pyodide.eval

### What is an Object?
An object is an instance of a class. It is created using the class blueprint and can access the attributes and methods defined in the class.

```python
# Creating objects
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
```
@Pyodide.eval

In this example, `Dog` is a class, and `my_dog` is an object (instance) of the `Dog` class. The `__init__` method is a special method (constructor) that initializes the object's attributes.

---

### Example: Creating Multiple Objects

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.drive()
car2.drive()
```
@Pyodide.eval

**Quiz:**
What will the following code output?

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(f"A {self.species} makes a sound.")

cat = Animal("Cat")
cat.speak()
```

[( )] A Dog makes a sound.  
[(X)] A Cat makes a sound.  
[( )] An error occurs.  
[( )] None of the above.  

**Explanation:**
The `speak` method uses the `species` attribute to print the message. Since `cat` is an instance of `Animal` with `species` set to "Cat", the output is "A Cat makes a sound."

---

### Class Attributes vs Instance Attributes

Understanding the difference between class attributes and instance attributes is crucial in object-oriented programming.

**Instance Attributes**: Unique to each object instance. Defined in the `__init__` method using `self`.

**Class Attributes**: Shared across all instances of a class. Defined outside the `__init__` method.

```python
class Employee:
    # Class attribute (shared by all instances)
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, position):
        # Instance attributes (unique to each instance)
        self.name = name
        self.position = position
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"{self.name} works at {Employee.company_name} as a {self.position}")
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

# Creating employees
emp1 = Employee("Alice", "Data Scientist")
emp2 = Employee("Bob", "Software Engineer")

emp1.display_info()
emp2.display_info()
print(f"Total employees: {Employee.get_employee_count()}")
```
@Pyodide.eval

**Explanation:**
- `company_name` is a class attribute shared by all `Employee` instances
- `name` and `position` are instance attributes unique to each employee
- `employee_count` tracks the total number of employees created
- The `@classmethod` decorator allows `get_employee_count()` to access class attributes

---

### Example: Student Management System

Let's build a more comprehensive example that demonstrates various aspects of classes and objects.

```python
class Student:
    # Class attribute
    school_name = "Python Academy"
    
    def __init__(self, name, student_id, grade=0):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.courses = []
    
    def enroll_course(self, course_name):
        """Enroll student in a course"""
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} enrolled in {course_name}")
        else:
            print(f"{self.name} is already enrolled in {course_name}")
    
    def set_grade(self, new_grade):
        """Update student's grade"""
        if 0 <= new_grade <= 100:
            self.grade = new_grade
            print(f"Grade updated to {new_grade} for {self.name}")
        else:
            print("Invalid grade! Grade must be between 0 and 100.")
    
    def get_status(self):
        """Determine student's academic status"""
        if self.grade >= 90:
            return "Excellent"
        elif self.grade >= 80:
            return "Good"
        elif self.grade >= 70:
            return "Average"
        elif self.grade >= 60:
            return "Pass"
        else:
            return "Needs Improvement"
    
    def display_info(self):
        """Display complete student information"""
        print(f"\n--- Student Information ---")
        print(f"School: {Student.school_name}")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print(f"Status: {self.get_status()}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}")

# Creating student objects
student1 = Student("Emma Wilson", "S001")
student2 = Student("James Brown", "S002", 85)

# Using the methods
student1.enroll_course("Machine Learning")
student1.enroll_course("Data Structures")
student1.set_grade(92)
student1.display_info()

print("\n" + "="*40 + "\n")

student2.enroll_course("Web Development")
student2.display_info()
```
@Pyodide.eval

**Key Takeaways:**
1. Methods can perform various operations on object data
2. Default parameter values can be used in constructors (e.g., `grade=0`)
3. Methods can call other methods within the same class (e.g., `display_info()` calls `get_status()`)
4. Objects maintain their own state independently

---

### Advanced Example: Shopping Cart System

This example demonstrates a more complex real-world application using classes and objects.

```python
class Product:
    def __init__(self, product_id, name, price, stock=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def is_available(self, quantity):
        return self.stock >= quantity
    
    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False
    
    def __str__(self):
        return f"{self.name} (${self.price}) - Stock: {self.stock}"

class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}  # Dictionary: {product_id: (product, quantity)}
        self.total = 0
    
    def add_item(self, product, quantity=1):
        """Add items to the cart"""
        if not product.is_available(quantity):
            print(f"Sorry, only {product.stock} units of {product.name} available.")
            return False
        
        if product.product_id in self.items:
            current_qty = self.items[product.product_id][1]
            self.items[product.product_id] = (product, current_qty + quantity)
        else:
            self.items[product.product_id] = (product, quantity)
        
        print(f"Added {quantity} x {product.name} to cart")
        return True
    
    def remove_item(self, product_id):
        """Remove an item from the cart"""
        if product_id in self.items:
            product_name = self.items[product_id][0].name
            del self.items[product_id]
            print(f"Removed {product_name} from cart")
        else:
            print("Item not found in cart")
    
    def calculate_total(self):
        """Calculate total cart value"""
        self.total = sum(product.price * quantity 
                        for product, quantity in self.items.values())
        return self.total
    
    def checkout(self):
        """Process the checkout"""
        if not self.items:
            print("Cart is empty!")
            return False
        
        print(f"\n{'='*50}")
        print(f"Checkout for {self.customer_name}")
        print(f"{'='*50}")
        
        for product, quantity in self.items.values():
            if product.reduce_stock(quantity):
                subtotal = product.price * quantity
                print(f"{product.name} x {quantity} = ${subtotal:.2f}")
            else:
                print(f"Error: Insufficient stock for {product.name}")
                return False
        
        total = self.calculate_total()
        print(f"{'-'*50}")
        print(f"Total: ${total:.2f}")
        print(f"{'='*50}\n")
        
        # Clear cart after checkout
        self.items.clear()
        return True
    
    def display_cart(self):
        """Display current cart contents"""
        if not self.items:
            print("Your cart is empty")
            return
        
        print(f"\nShopping Cart for {self.customer_name}:")
        print("-" * 40)
        for product, quantity in self.items.values():
            print(f"{product.name} x {quantity} - ${product.price * quantity:.2f}")
        print("-" * 40)
        print(f"Cart Total: ${self.calculate_total():.2f}\n")

# Create products
laptop = Product("P001", "Gaming Laptop", 1200.00, 5)
mouse = Product("P002", "Wireless Mouse", 25.00, 15)
keyboard = Product("P003", "Mechanical Keyboard", 80.00, 10)

# Create shopping cart
cart = ShoppingCart("John Doe")

# Add items to cart
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)

# Display cart
cart.display_cart()

# Process checkout
cart.checkout()

# Verify stock levels
print("Remaining Stock:")
print(laptop)
print(mouse)
print(keyboard)
```
@Pyodide.eval

**Advanced Concepts Demonstrated:**
1. **Object Composition**: `ShoppingCart` contains multiple `Product` objects
2. **Data Structures**: Using dictionaries to manage cart items efficiently
3. **State Management**: Objects maintain and update their internal state
4. **Error Handling**: Checking stock availability before processing
5. **Special Methods**: `__str__` method for readable object representation
6. **Complex Logic**: Calculating totals, managing inventory, processing transactions

**Quiz:**
In the shopping cart example, what happens if you try to add 10 laptops when only 5 are in stock?

[( )] All 10 laptops are added to the cart  
[(X)] An error message is displayed and the item is not added  
[( )] The program crashes  
[( )] Only 5 laptops are added automatically  

**Explanation:**
The `add_item` method checks product availability using `is_available()` before adding items. If insufficient stock exists, it prints an error message and returns `False` without adding the items.

---

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and modularity. For example:

### What is Inheritance?
Inheritance is a mechanism where one class (child class or subclass) can derive properties and behaviors from another class (parent class or superclass). This allows you to create a hierarchy of classes that share common attributes and methods.

**Benefits of Inheritance:**
1. **Code Reusability**: Avoid duplicating code by inheriting common functionality
2. **Extensibility**: Easily extend functionality by adding new methods to child classes
3. **Maintainability**: Changes to parent class automatically propagate to child classes
4. **Logical Organization**: Create hierarchical relationships between classes

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(f"A {self.species} makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__("Dog")
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an object
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.speak()
my_dog.bark()
```
@Pyodide.eval

In this example, the `Dog` class inherits from the `Animal` class. The `super()` function is used to call the constructor of the parent class.

---

### Example: Overriding Methods

A subclass can override methods from the parent class to provide specialized behavior:

```python
class Bird(Animal):
    def speak(self):
        print(f"A {self.species} chirps.")

parrot = Bird("Parrot")
parrot.speak()
```
@Pyodide.eval

**Quiz:**
What will the following code output?

```python
class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def start(self):
        print("Car is starting.")

my_car = Car()
my_car.start()
```

[( )] Vehicle is starting.  
[(X)] Car is starting.  
[( )] An error occurs.  
[( )] None of the above.  

**Explanation:**
The `start` method in the `Car` class overrides the `start` method in the `Vehicle` class. Therefore, calling `my_car.start()` outputs "Car is starting."

---

### Advanced Example: Employee Management System with Inheritance

Let's build a comprehensive employee management system demonstrating inheritance with multiple levels.

```python
class Person:
    """Base class representing a person"""
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

class Employee(Person):
    """Employee class inheriting from Person"""
    employee_count = 0
    
    def __init__(self, name, age, email, employee_id, department, salary):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        """Override parent method to add employee-specific info"""
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
    
    def give_raise(self, percentage):
        """Give employee a raise"""
        raise_amount = self.salary * (percentage / 100)
        self.salary += raise_amount
        print(f"{self.name} received a {percentage}% raise of ${raise_amount:,.2f}")
        print(f"New salary: ${self.salary:,.2f}")

class Manager(Employee):
    """Manager class inheriting from Employee"""
    def __init__(self, name, age, email, employee_id, department, salary, team_size):
        super().__init__(name, age, email, employee_id, department, salary)
        self.team_size = team_size
        self.team_members = []
    
    def display_info(self):
        """Override to add manager-specific info"""
        super().display_info()
        print(f"Team Size: {self.team_size}")
        print(f"Team Members: {', '.join(self.team_members) if self.team_members else 'None'}")
    
    def add_team_member(self, employee_name):
        """Add a team member"""
        if len(self.team_members) < self.team_size:
            self.team_members.append(employee_name)
            print(f"{employee_name} added to {self.name}'s team")
        else:
            print(f"Team is full! Maximum size: {self.team_size}")
    
    def conduct_meeting(self):
        """Conduct a team meeting"""
        print(f"\n{self.name} is conducting a meeting with:")
        for member in self.team_members:
            print(f"  - {member}")

class Developer(Employee):
    """Developer class inheriting from Employee"""
    def __init__(self, name, age, email, employee_id, department, salary, programming_languages):
        super().__init__(name, age, email, employee_id, department, salary)
        self.programming_languages = programming_languages
        self.projects = []
    
    def display_info(self):
        """Override to add developer-specific info"""
        super().display_info()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")
        print(f"Current Projects: {', '.join(self.projects) if self.projects else 'None'}")
    
    def assign_project(self, project_name):
        """Assign a project to the developer"""
        self.projects.append(project_name)
        print(f"Project '{project_name}' assigned to {self.name}")
    
    def complete_project(self, project_name):
        """Mark a project as complete"""
        if project_name in self.projects:
            self.projects.remove(project_name)
            print(f"{self.name} completed project '{project_name}'")
        else:
            print(f"Project '{project_name}' not found in {self.name}'s projects")

# Create instances
print("="*60)
print("EMPLOYEE MANAGEMENT SYSTEM")
print("="*60)

manager = Manager("Sarah Johnson", 35, "sarah@company.com", "M001", "Engineering", 95000, 5)
dev1 = Developer("Alex Chen", 28, "alex@company.com", "D001", "Engineering", 75000, ["Python", "Java", "C++"])
dev2 = Developer("Maria Garcia", 26, "maria@company.com", "D002", "Engineering", 72000, ["JavaScript", "TypeScript", "React"])

# Display information
print("\n--- Manager Information ---")
manager.display_info()

print("\n" + "-"*60)
print("\n--- Developer 1 Information ---")
dev1.display_info()

print("\n" + "-"*60)
print("\n--- Developer 2 Information ---")
dev2.display_info()

# Perform operations
print("\n" + "="*60)
print("OPERATIONS")
print("="*60)

manager.add_team_member("Alex Chen")
manager.add_team_member("Maria Garcia")

dev1.assign_project("AI Chatbot")
dev1.assign_project("Data Pipeline")

dev2.assign_project("Web Dashboard")

manager.conduct_meeting()

dev1.give_raise(10)

print("\n--- Updated Developer Info ---")
dev1.display_info()

print(f"\nTotal Employees: {Employee.employee_count}")
```
@Pyodide.eval

**Key Concepts Demonstrated:**
1. **Multi-level Inheritance**: `Manager` and `Developer` inherit from `Employee`, which inherits from `Person`
2. **Method Overriding**: Each subclass overrides `display_info()` to add specialized information
3. **Super() Usage**: Child classes call parent constructors using `super().__init__()`
4. **Extending Functionality**: Child classes add new methods specific to their roles
5. **Inheritance Hierarchy**: Person → Employee → Manager/Developer

---

### Example: Wildlife Species Hierarchy

This example demonstrates inheritance with multiple derived classes and polymorphic behavior.

```python
class Animal:
    """Base class for all animals"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def make_sound(self):
        """Generic sound method to be overridden"""
        return "Some generic sound"
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

class Mammal(Animal):
    """Mammal class"""
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color
    
    def display_info(self):
        super().display_info()
        print(f"Fur Color: {self.fur_color}")

class Dog(Mammal):
    """Dog class"""
    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, "Dog", age, fur_color)
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def fetch(self):
        print(f"{self.name} is fetching the ball!")
    
    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")

class Cat(Mammal):
    """Cat class"""
    def __init__(self, name, age, fur_color):
        super().__init__(name, "Cat", age, fur_color)
    
    def make_sound(self):
        return "Meow!"
    
    def scratch(self):
        print(f"{self.name} is scratching the furniture!")

class Bird(Animal):
    """Bird class"""
    def __init__(self, name, species, age, can_fly):
        super().__init__(name, species, age)
        self.can_fly = can_fly
    
    def make_sound(self):
        return "Chirp! Chirp!"
    
    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying!")
        else:
            print(f"{self.name} cannot fly.")
    
    def display_info(self):
        super().display_info()
        print(f"Can Fly: {'Yes' if self.can_fly else 'No'}")

# Create animal instances
dog = Dog("Rex", 5, "Brown", "German Shepherd")
cat = Cat("Whiskers", 3, "White")
parrot = Bird("Polly", "Parrot", 2, True)
penguin = Bird("Pingu", "Penguin", 4, False)

# Demonstrate polymorphism
animals = [dog, cat, parrot, penguin]

print("="*50)
print("WILDLIFE SPECIES DEMONSTRATION")
print("="*50)

for animal in animals:
    print(f"\n{animal.name} ({animal.species}):")
    print(f"  Sound: {animal.make_sound()}")
    animal.eat()
    animal.sleep()
    
    # Demonstrate specialized methods
    if isinstance(animal, Dog):
        animal.fetch()
    elif isinstance(animal, Cat):
        animal.scratch()
    elif isinstance(animal, Bird):
        animal.fly()
    
    print()

# Display detailed information
print("="*50)
print("DETAILED ANIMAL INFORMATION")
print("="*50)

for animal in animals:
    print(f"\n--- {animal.name} ---")
    animal.display_info()
```
@Pyodide.eval

**Advanced Inheritance Concepts:**
1. **Inheritance Chain**: Animal → Mammal → Dog/Cat
2. **Parallel Inheritance**: Both Mammal and Bird inherit from Animal
3. **Method Overriding at Multiple Levels**: Each class overrides methods as needed
4. **Polymorphism**: Same method call produces different results based on object type
5. **Type Checking**: Using `isinstance()` to check object types

**Quiz:**
In the Wildlife Species example, what is the inheritance chain for the `Dog` class?

[( )] Animal → Dog  
[( )] Animal → Bird → Dog  
[(X)] Animal → Mammal → Dog  
[( )] Mammal → Animal → Dog  

**Explanation:**
The `Dog` class inherits from `Mammal`, which in turn inherits from `Animal`, creating the chain: Animal → Mammal → Dog.

---

## Understanding Inheritance in Depth

### What is Inheritance and Why Use It?

**Definition**: Inheritance is a mechanism that allows you to create a new class (child/derived class) based on an existing class (parent/base class), inheriting its attributes and methods.

**Real-World Analogy - Biological Inheritance:**
Just like you inherit traits from your parents (eye color, height), classes can inherit features from parent classes. You don't redefine everything about yourself; you build upon what you inherited.

**Real-World Analogy - Vehicle Manufacturing:**
- A vehicle company doesn't design each vehicle type from scratch
- They start with a basic "Vehicle" design (parent class)
- Then create specific types: Cars, Trucks, Motorcycles (child classes)
- Each inherits common features (wheels, engine, steering) but adds specific features

### Why Use Inheritance?

#### 1. **Code Reusability** - Don't Repeat Yourself (DRY)

Without inheritance, you duplicate code:

```python
# WITHOUT INHERITANCE - Code Duplication
class Manager:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        print(f"{self.name}, ID: {self.employee_id}")

class Developer:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        print(f"{self.name}, ID: {self.employee_id}")

# Notice the duplication? Same code repeated!
```

With inheritance, you write it once:

```python
# WITH INHERITANCE - No Duplication
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        print(f"{self.name}, ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

# Common code is in Employee, specialized code in child classes
manager = Manager("Alice", "M001", 90000, "Engineering")
developer = Developer("Bob", "D001", 75000, "Python")

manager.display_info()  # Uses inherited method
developer.display_info()  # Uses inherited method
```
@Pyodide.eval

**Key Benefit**: Changes to `Employee` automatically apply to all child classes!

---

#### 2. **Logical Hierarchy** - Models Real-World Relationships

Inheritance naturally represents "IS-A" relationships:
- A Dog IS-A Animal
- A Manager IS-AN Employee
- A Car IS-A Vehicle

```python
# Real-world hierarchy: Educational Institution
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self, topic):
        print(f"{self.name} is teaching {topic} in {self.subject}")

class TeachingAssistant(Student, Teacher):
    """Multiple inheritance - a TA is both a student and a teacher"""
    def __init__(self, name, age, student_id, subject):
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, subject)
    
    def assist(self):
        print(f"{self.name} is assisting in {self.subject}")

# Usage
student = Student("Emma", 20, "S001")
teacher = Teacher("Dr. Smith", 45, "Computer Science")
ta = TeachingAssistant("Alex", 24, "S999", "Mathematics")

student.introduce()  # From Person
student.enroll("AI Course")  # From Student

teacher.introduce()  # From Person
teacher.teach("Machine Learning")  # From Teacher

ta.introduce()  # From Person
ta.enroll("Advanced Math")  # From Student
ta.teach("Calculus")  # From Teacher
ta.assist()  # From TeachingAssistant
```
@Pyodide.eval

---

#### 3. **Extensibility** - Easy to Add New Features

Add new classes without modifying existing code:

```python
# E-commerce System demonstrating extensibility
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_description(self):
        return f"{self.name}: ${self.price}"
    
    def calculate_total(self, quantity):
        return self.price * quantity

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    
    def calculate_shipping(self):
        # Shipping cost based on weight
        return self.weight * 0.5
    
    def get_description(self):
        return f"{super().get_description()}, Weight: {self.weight}kg"

class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size
    
    def download(self):
        return f"Downloading {self.name} ({self.file_size}MB)..."
    
    def get_description(self):
        return f"{super().get_description()}, Size: {self.file_size}MB"

class SubscriptionProduct(Product):
    def __init__(self, name, monthly_price, duration_months):
        super().__init__(name, monthly_price)
        self.duration_months = duration_months
    
    def calculate_total(self, quantity=1):
        # Override to calculate based on subscription duration
        return self.price * self.duration_months
    
    def get_description(self):
        return f"{self.name}: ${self.price}/month for {self.duration_months} months"

# Easy to add new product types without changing existing code!
products = [
    PhysicalProduct("Laptop", 1200, 2.5),
    DigitalProduct("E-book", 15, 5),
    SubscriptionProduct("Premium Plan", 9.99, 12)
]

print("="*60)
print("E-COMMERCE PRODUCT CATALOG")
print("="*60)

for product in products:
    print(f"\n{product.get_description()}")
    print(f"Total Cost: ${product.calculate_total(1):.2f}")
    
    if isinstance(product, PhysicalProduct):
        print(f"Shipping: ${product.calculate_shipping():.2f}")
    elif isinstance(product, DigitalProduct):
        print(f"Download: {product.download()}")
```
@Pyodide.eval

**Key Benefit**: Adding `SubscriptionProduct` didn't require changing `Product`, `PhysicalProduct`, or `DigitalProduct`!

---

#### 4. **Maintainability** - Fix Once, Fix Everywhere

```python
# Bug fix demonstration
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_age(self):
        # Bug: Wrong calculation!
        # return 2024 - self.year  # Before fix
        # Fix applied:
        from datetime import datetime
        return datetime.now().year - self.year  # After fix
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model} - Age: {self.get_age()} years")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

# When we fixed get_age() in Vehicle, 
# it automatically fixed it for Car and Motorcycle!
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Harley", "Sportster", 2018, 883)

car.display_info()
motorcycle.display_info()
```
@Pyodide.eval

**Key Benefit**: One fix in the parent class fixes the issue for ALL child classes!

---

### Types of Inheritance

#### 1. Single Inheritance
One child class inherits from one parent class.

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.breathe()  # Inherited from Animal
dog.bark()     # Defined in Dog
```
@Pyodide.eval

#### 2. Multiple Inheritance
One child class inherits from multiple parent classes.

```python
class Flyer:
    def fly(self):
        print("Flying in the sky")

class Swimmer:
    def swim(self):
        print("Swimming in water")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack quack!")

duck = Duck()
duck.fly()    # From Flyer
duck.swim()   # From Swimmer
duck.quack()  # From Duck
```
@Pyodide.eval

#### 3. Multilevel Inheritance
Chain of inheritance: GrandParent → Parent → Child

```python
class LivingBeing:
    def live(self):
        print("Living...")

class Animal(LivingBeing):
    def move(self):
        print("Moving...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

dog = Dog()
dog.live()  # From LivingBeing
dog.move()  # From Animal
dog.bark()  # From Dog
```
@Pyodide.eval

#### 4. Hierarchical Inheritance
Multiple child classes inherit from one parent.

```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def draw(self):
        print(f"Drawing a {self.color} circle")

class Square(Shape):
    def draw(self):
        print(f"Drawing a {self.color} square")

class Triangle(Shape):
    def draw(self):
        print(f"Drawing a {self.color} triangle")

shapes = [Circle("red"), Square("blue"), Triangle("green")]
for shape in shapes:
    shape.draw()
```
@Pyodide.eval

---

### When to Use Inheritance

✅ **Use Inheritance When:**
- There's a clear "IS-A" relationship (Dog IS-A Animal)
- You need to reuse code from an existing class
- You want to create a hierarchy of related classes
- Child classes are specialized versions of the parent

❌ **Don't Use Inheritance When:**
- There's a "HAS-A" relationship (Car HAS-A Engine) - use composition instead
- Classes are unrelated
- You just want to share some methods - use composition or mixins

---

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables one interface to be used for a general class of actions.

### What is Polymorphism?
Polymorphism means "many forms." It allows the same interface (method name) to be used for different underlying forms (data types or classes). There are two main types:

1. **Method Overriding**: Subclasses provide specific implementation of methods defined in the parent class
2. **Method Overloading**: Multiple methods with the same name but different parameters (less common in Python)

**Benefits of Polymorphism:**
- Write more flexible and maintainable code
- Treat objects of different types uniformly
- Implement common interfaces across different classes
- Enable dynamic method dispatch at runtime

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
```
@Pyodide.eval

**Explanation:**
The `area()` method is called on different shape objects, and each executes its own version of the method. This demonstrates polymorphism in action.

---

### Advanced Example: Payment Processing System

Let's build a comprehensive payment system demonstrating polymorphism across different payment methods.

```python
from abc import ABC, abstractmethod
from datetime import datetime

class Payment(ABC):
    """Abstract base class for all payment methods"""
    def __init__(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()
        self.status = "Pending"
    
    @abstractmethod
    def process_payment(self):
        """Process the payment - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def validate(self):
        """Validate payment details - must be implemented by subclasses"""
        pass
    
    def get_receipt(self):
        """Generate a receipt"""
        return f"""
{'='*50}
PAYMENT RECEIPT
{'='*50}
Amount: ${self.amount:.2f}
Description: {self.description}
Status: {self.status}
Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
{'='*50}
"""

class CreditCardPayment(Payment):
    """Credit card payment implementation"""
    def __init__(self, amount, description, card_number, card_holder, cvv):
        super().__init__(amount, description)
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
    
    def validate(self):
        """Validate credit card details"""
        if len(self.card_number) != 16:
            return False, "Invalid card number"
        if len(self.cvv) != 3:
            return False, "Invalid CVV"
        if not self.card_holder:
            return False, "Card holder name required"
        return True, "Valid"
    
    def process_payment(self):
        """Process credit card payment"""
        is_valid, message = self.validate()
        if not is_valid:
            self.status = f"Failed: {message}"
            return False
        
        # Simulate payment processing
        masked_card = f"****-****-****-{self.card_number[-4:]}"
        print(f"Processing credit card payment...")
        print(f"Card: {masked_card}")
        print(f"Holder: {self.card_holder}")
        print(f"Amount: ${self.amount:.2f}")
        
        self.status = "Completed"
        return True

class PayPalPayment(Payment):
    """PayPal payment implementation"""
    def __init__(self, amount, description, email):
        super().__init__(amount, description)
        self.email = email
    
    def validate(self):
        """Validate PayPal details"""
        if "@" not in self.email or "." not in self.email:
            return False, "Invalid email address"
        return True, "Valid"
    
    def process_payment(self):
        """Process PayPal payment"""
        is_valid, message = self.validate()
        if not is_valid:
            self.status = f"Failed: {message}"
            return False
        
        # Simulate payment processing
        print(f"Processing PayPal payment...")
        print(f"Account: {self.email}")
        print(f"Amount: ${self.amount:.2f}")
        
        self.status = "Completed"
        return True

class BankTransferPayment(Payment):
    """Bank transfer payment implementation"""
    def __init__(self, amount, description, account_number, routing_number, bank_name):
        super().__init__(amount, description)
        self.account_number = account_number
        self.routing_number = routing_number
        self.bank_name = bank_name
    
    def validate(self):
        """Validate bank transfer details"""
        if len(self.account_number) < 8:
            return False, "Invalid account number"
        if len(self.routing_number) != 9:
            return False, "Invalid routing number"
        return True, "Valid"
    
    def process_payment(self):
        """Process bank transfer payment"""
        is_valid, message = self.validate()
        if not is_valid:
            self.status = f"Failed: {message}"
            return False
        
        # Simulate payment processing
        masked_account = f"****{self.account_number[-4:]}"
        print(f"Processing bank transfer...")
        print(f"Bank: {self.bank_name}")
        print(f"Account: {masked_account}")
        print(f"Amount: ${self.amount:.2f}")
        
        self.status = "Completed"
        return True

class CryptocurrencyPayment(Payment):
    """Cryptocurrency payment implementation"""
    def __init__(self, amount, description, wallet_address, crypto_type="Bitcoin"):
        super().__init__(amount, description)
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type
    
    def validate(self):
        """Validate cryptocurrency details"""
        if len(self.wallet_address) < 26:
            return False, "Invalid wallet address"
        return True, "Valid"
    
    def process_payment(self):
        """Process cryptocurrency payment"""
        is_valid, message = self.validate()
        if not is_valid:
            self.status = f"Failed: {message}"
            return False
        
        # Simulate payment processing
        masked_wallet = f"{self.wallet_address[:6]}...{self.wallet_address[-4:]}"
        print(f"Processing {self.crypto_type} payment...")
        print(f"Wallet: {masked_wallet}")
        print(f"Amount: ${self.amount:.2f}")
        
        self.status = "Completed"
        return True

# Payment processing function demonstrating polymorphism
def process_transaction(payment: Payment):
    """Process any type of payment using polymorphism"""
    print(f"\nProcessing {payment.__class__.__name__}...")
    print("-" * 50)
    
    if payment.process_payment():
        print(f" Payment successful!")
        print(payment.get_receipt())
    else:
        print(f"✗ Payment failed: {payment.status}")
        print("-" * 50)

# Create different payment types
payments = [
    CreditCardPayment(150.00, "Online Purchase", "1234567890123456", "John Doe", "123"),
    PayPalPayment(75.50, "Service Subscription", "user@example.com"),
    BankTransferPayment(500.00, "Invoice Payment", "987654321", "123456789", "First National Bank"),
    CryptocurrencyPayment(250.00, "Digital Product", "1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O")
]

print("="*50)
print("PAYMENT PROCESSING SYSTEM")
print("="*50)

# Process all payments using the same interface
for payment in payments:
    process_transaction(payment)
```
@Pyodide.eval

**Key Polymorphism Concepts:**
1. **Common Interface**: All payment classes implement `process_payment()` and `validate()`
2. **Different Implementations**: Each payment type has its own unique processing logic
3. **Uniform Treatment**: The `process_transaction()` function works with any payment type
4. **Dynamic Dispatch**: The correct method is called based on the object's actual type at runtime
5. **Abstraction**: Users don't need to know the specific payment type to process it

---

### Example: Data Exporter with Polymorphism

This example demonstrates polymorphism in a data export system supporting multiple file formats.

```python
from abc import ABC, abstractmethod

class DataExporter(ABC):
    """Abstract base class for data exporters"""
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
    
    @abstractmethod
    def export(self):
        """Export data - must be implemented by subclasses"""
        pass
    
    def validate_data(self):
        """Validate data before export"""
        if not self.data:
            print("Error: No data to export")
            return False
        return True

class CSVExporter(DataExporter):
    """Export data to CSV format"""
    def export(self):
        if not self.validate_data():
            return False
        
        print(f"Exporting to CSV: {self.filename}.csv")
        print("Format: Comma-separated values")
        
        # Simulate CSV export
        for i, row in enumerate(self.data):
            csv_row = ",".join(str(item) for item in row)
            if i == 0:
                print(f"Header: {csv_row}")
            else:
                print(f"Row {i}: {csv_row}")
        
        print("✓ CSV export completed\n")
        return True

class JSONExporter(DataExporter):
    """Export data to JSON format"""
    def export(self):
        if not self.validate_data():
            return False
        
        print(f"Exporting to JSON: {self.filename}.json")
        print("Format: JavaScript Object Notation")
        
        # Simulate JSON export
        print("[")
        for i, row in enumerate(self.data):
            json_obj = "{" + ", ".join(f'"{k}": "{v}"' for k, v in zip(["id", "name", "value"], row)) + "}"
            comma = "," if i < len(self.data) - 1 else ""
            print(f"  {json_obj}{comma}")
        print("]")
        
        print("✓ JSON export completed\n")
        return True

class XMLExporter(DataExporter):
    """Export data to XML format"""
    def export(self):
        if not self.validate_data():
            return False
        
        print(f"Exporting to XML: {self.filename}.xml")
        print("Format: Extensible Markup Language")
        
        # Simulate XML export
        print("<records>")
        for row in self.data:
            print("  <record>")
            print(f"    <id>{row[0]}</id>")
            print(f"    <name>{row[1]}</name>")
            print(f"    <value>{row[2]}</value>")
            print("  </record>")
        print("</records>")
        
        print("✓ XML export completed\n")
        return True

class ExcelExporter(DataExporter):
    """Export data to Excel format"""
    def export(self):
        if not self.validate_data():
            return False
        
        print(f"Exporting to Excel: {self.filename}.xlsx")
        print("Format: Microsoft Excel Spreadsheet")
        
        # Simulate Excel export
        print("Creating workbook...")
        print(f"Sheet: {self.filename}")
        print(f"Rows: {len(self.data)}")
        print(f"Columns: {len(self.data[0]) if self.data else 0}")
        
        print("✓ Excel export completed\n")
        return True

# Sample data
data = [
    [1, "Alice", 95],
    [2, "Bob", 87],
    [3, "Charlie", 92],
    [4, "Diana", 88]
]

# Create exporters for different formats
exporters = [
    CSVExporter(data, "student_grades"),
    JSONExporter(data, "student_grades"),
    XMLExporter(data, "student_grades"),
    ExcelExporter(data, "student_grades")
]

print("="*60)
print("DATA EXPORT SYSTEM - POLYMORPHISM DEMONSTRATION")
print("="*60 + "\n")

# Export data in all formats using polymorphism
for exporter in exporters:
    exporter.export()
```
@Pyodide.eval

**Polymorphism Benefits Demonstrated:**
1. **Single Interface**: All exporters use the same `export()` method
2. **Multiple Implementations**: Each format has unique export logic
3. **Easy Extension**: New export formats can be added without changing existing code
4. **Flexibility**: Client code doesn't need to know the specific exporter type

**Quiz:**
What is the main benefit of polymorphism in the payment processing system?

[( )] It makes the code run faster  
[(X)] It allows different payment types to be processed using the same interface  
[( )] It reduces the number of classes needed  
[( )] It eliminates the need for validation  

**Explanation:**
Polymorphism allows the `process_transaction()` function to work with any payment type using the same interface, making the code more flexible and maintainable.

---

## Understanding Polymorphism in Depth

### What is Polymorphism and Why Use It?

**Definition**: Polymorphism (from Greek: "many forms") allows objects of different classes to be treated as objects of a common type. The same operation behaves differently for different types.

**Real-World Analogy - Universal Remote Control:**
Think of a universal TV remote. The "power" button works on any TV brand:
- Samsung TV responds by turning on its display
- LG TV responds by turning on its display
- Sony TV responds by turning on its display

Same button (interface), different implementation for each TV brand. That's polymorphism!

**Real-World Analogy - Payment Methods:**
When you pay at a store, the cashier doesn't need to know if you're using:
- Credit card
- Debit card
- Mobile payment
- Cash

They just say "process payment" and each method handles it differently.

---

### Why Use Polymorphism?

#### 1. **Flexibility** - Write Code That Works with Future Types

Without polymorphism:

```python
# WITHOUT POLYMORPHISM - Rigid and hard to extend
def process_payment_credit_card(amount, card_number):
    print(f"Processing ${amount} via credit card")
    # Credit card specific logic

def process_payment_paypal(amount, email):
    print(f"Processing ${amount} via PayPal")
    # PayPal specific logic

def process_payment_bitcoin(amount, wallet):
    print(f"Processing ${amount} via Bitcoin")
    # Bitcoin specific logic

# Main code becomes messy
payment_type = "credit_card"
if payment_type == "credit_card":
    process_payment_credit_card(100, "1234-5678")
elif payment_type == "paypal":
    process_payment_paypal(100, "user@email.com")
elif payment_type == "bitcoin":
    process_payment_bitcoin(100, "1A2B3C")
# Need to modify this code every time we add a new payment method!
```

With polymorphism:

```python
# WITH POLYMORPHISM - Flexible and extensible
class Payment:
    def process(self, amount):
        pass  # To be implemented by subclasses

class CreditCardPayment(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via Credit Card")

class PayPalPayment(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via PayPal")

class BitcoinPayment(Payment):
    def process(self, amount):
        print(f"Processing ${amount} via Bitcoin")

class ApplePayPayment(Payment):  # Easy to add new payment methods!
    def process(self, amount):
        print(f"Processing ${amount} via Apple Pay")

# Main code stays the same, regardless of payment type!
def checkout(payment: Payment, amount):
    payment.process(amount)  # Polymorphic call

# Usage
payments = [
    CreditCardPayment(),
    PayPalPayment(),
    BitcoinPayment(),
    ApplePayPayment()
]

for payment in payments:
    checkout(payment, 100)  # Same interface, different behavior!
```
@Pyodide.eval

**Key Benefit**: Adding `ApplePayPayment` doesn't require changing the `checkout()` function!

---

#### 2. **Simplicity** - One Interface, Many Implementations

Real-world example: File handling system

```python
# File processing system demonstrating polymorphism
class FileProcessor:
    def process(self, filename):
        raise NotImplementedError("Subclass must implement process()")

class TextFileProcessor(FileProcessor):
    def process(self, filename):
        print(f"Processing text file: {filename}")
        print("- Reading lines")
        print("- Counting words")
        print("- Analyzing sentiment")
        return "Text processing complete"

class ImageFileProcessor(FileProcessor):
    def process(self, filename):
        print(f"Processing image file: {filename}")
        print("- Loading image")
        print("- Applying filters")
        print("- Resizing")
        return "Image processing complete"

class VideoFileProcessor(FileProcessor):
    def process(self, filename):
        print(f"Processing video file: {filename}")
        print("- Extracting frames")
        print("- Compressing")
        print("- Generating thumbnail")
        return "Video processing complete"

class AudioFileProcessor(FileProcessor):
    def process(self, filename):
        print(f"Processing audio file: {filename}")
        print("- Normalizing volume")
        print("- Removing noise")
        print("- Converting format")
        return "Audio processing complete"

# Polymorphic function - works with ANY file processor!
def batch_process_files(file_list):
    """Process multiple files regardless of their type"""
    print("="*60)
    print("BATCH FILE PROCESSING")
    print("="*60)
    
    for file_info in file_list:
        filename, processor = file_info
        print(f"\n[Processing {filename}]")
        result = processor.process(filename)
        print(f"Result: {result}\n")
        print("-"*60)

# Define files and their processors
files_to_process = [
    ("document.txt", TextFileProcessor()),
    ("photo.jpg", ImageFileProcessor()),
    ("movie.mp4", VideoFileProcessor()),
    ("song.mp3", AudioFileProcessor()),
    ("report.txt", TextFileProcessor()),
]

# Process all files with one simple function call!
batch_process_files(files_to_process)
```
@Pyodide.eval

**Key Benefit**: The `batch_process_files()` function doesn't need to know the specific file type!

---

#### 3. **Maintainability** - Easier to Update and Debug

Real-world example: Notification system

```python
# Notification system demonstrating maintainability through polymorphism
from datetime import datetime

class Notification:
    def __init__(self, message, recipient):
        self.message = message
        self.recipient = recipient
        self.timestamp = datetime.now()
    
    def send(self):
        raise NotImplementedError("Subclass must implement send()")
    
    def log(self):
        print(f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
              f"Notification to {self.recipient}: {self.message}")

class EmailNotification(Notification):
    def send(self):
        print(f"📧 Sending email to {self.recipient}")
        print(f"   Subject: Notification")
        print(f"   Body: {self.message}")
        self.log()
        return True

class SMSNotification(Notification):
    def send(self):
        print(f"📱 Sending SMS to {self.recipient}")
        print(f"   Message: {self.message}")
        self.log()
        return True

class PushNotification(Notification):
    def send(self):
        print(f"🔔 Sending push notification to {self.recipient}")
        print(f"   Alert: {self.message}")
        self.log()
        return True

class SlackNotification(Notification):
    def send(self):
        print(f"💬 Sending Slack message to {self.recipient}")
        print(f"   Message: {self.message}")
        self.log()
        return True

# Notification manager - polymorphic approach
class NotificationManager:
    def __init__(self):
        self.notifications = []
    
    def add_notification(self, notification: Notification):
        self.notifications.append(notification)
    
    def send_all(self):
        """Send all notifications regardless of type"""
        print("="*60)
        print("SENDING NOTIFICATIONS")
        print("="*60)
        
        successful = 0
        for notification in self.notifications:
            print()
            if notification.send():  # Polymorphic call
                successful += 1
            print("-"*60)
        
        print(f"\n✓ Sent {successful}/{len(self.notifications)} notifications")

# Usage
manager = NotificationManager()

# Add different types of notifications
manager.add_notification(EmailNotification(
    "Your order has shipped!", 
    "customer@email.com"
))

manager.add_notification(SMSNotification(
    "Your verification code is 123456", 
    "+1-555-0100"
))

manager.add_notification(PushNotification(
    "You have a new message!", 
    "user123"
))

manager.add_notification(SlackNotification(
    "Meeting in 15 minutes", 
    "#team-channel"
))

# Send all notifications with one method call!
manager.send_all()
```
@Pyodide.eval

**Key Benefit**: If we need to add a new notification type (e.g., WhatsApp), we just create a new class without modifying existing code!

---

#### 4. **Scalability** - Design Systems That Grow

Real-world example: Database connectors

```python
# Database system demonstrating scalability through polymorphism
class DatabaseConnector:
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connected = False
    
    def connect(self):
        raise NotImplementedError()
    
    def disconnect(self):
        raise NotImplementedError()
    
    def execute_query(self, query):
        raise NotImplementedError()

class MySQLConnector(DatabaseConnector):
    def connect(self):
        print(f"Connecting to MySQL database '{self.database}' at {self.host}")
        self.connected = True
        return "MySQL connection established"
    
    def disconnect(self):
        print("Disconnecting from MySQL")
        self.connected = False
    
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected"
        print(f"Executing MySQL query: {query}")
        return "MySQL query executed successfully"

class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        print(f"Connecting to PostgreSQL database '{self.database}' at {self.host}")
        self.connected = True
        return "PostgreSQL connection established"
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL")
        self.connected = False
    
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected"
        print(f"Executing PostgreSQL query: {query}")
        return "PostgreSQL query executed successfully"

class MongoDBConnector(DatabaseConnector):
    def connect(self):
        print(f"Connecting to MongoDB database '{self.database}' at {self.host}")
        self.connected = True
        return "MongoDB connection established"
    
    def disconnect(self):
        print("Disconnecting from MongoDB")
        self.connected = False
    
    def execute_query(self, query):
        if not self.connected:
            return "Error: Not connected"
        print(f"Executing MongoDB query: {query}")
        return "MongoDB query executed successfully"

# Database manager using polymorphism
class DatabaseManager:
    def __init__(self, connector: DatabaseConnector):
        self.connector = connector
    
    def perform_operation(self, query):
        """Perform database operation - works with ANY database!"""
        print(f"\n{'='*60}")
        print(f"DATABASE OPERATION")
        print(f"{'='*60}")
        
        result = self.connector.connect()
        print(f"Status: {result}")
        
        print()
        result = self.connector.execute_query(query)
        print(f"Result: {result}")
        
        print()
        self.connector.disconnect()
        print(f"{'='*60}\n")

# Usage - Same code works with different databases!
databases = [
    MySQLConnector("localhost", "customers_db"),
    PostgreSQLConnector("localhost", "analytics_db"),
    MongoDBConnector("localhost", "logs_db")
]

for db in databases:
    manager = DatabaseManager(db)
    manager.perform_operation("SELECT * FROM users")
```
@Pyodide.eval

**Key Benefit**: The application can work with multiple database systems without changing the core logic!

---

### Types of Polymorphism

#### 1. **Compile-time Polymorphism (Method Overloading)**
Python doesn't strictly support method overloading like Java/C++, but we can achieve similar results:

```python
class Calculator:
    def add(self, *args):
        """Polymorphic add - works with different numbers of arguments"""
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)

calc = Calculator()
print(f"2 + 3 = {calc.add(2, 3)}")
print(f"2 + 3 + 4 = {calc.add(2, 3, 4)}")
print(f"1 + 2 + 3 + 4 + 5 = {calc.add(1, 2, 3, 4, 5)}")
```
@Pyodide.eval

#### 2. **Runtime Polymorphism (Method Overriding)**
The most common type in Python:

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):  # Override
        return "Woof!"

class Cat(Animal):
    def make_sound(self):  # Override
        return "Meow!"

class Cow(Animal):
    def make_sound(self):  # Override
        return "Moo!"

# Polymorphism in action
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.make_sound())  # Different output for each animal
```
@Pyodide.eval

#### 3. **Duck Typing** (Python's Special Polymorphism)
"If it walks like a duck and quacks like a duck, it's a duck"

```python
# Duck typing - no inheritance needed!
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:  # Not an animal, but has speak()
    def speak(self):
        return "Beep boop!"

def make_it_speak(entity):
    """Works with ANY object that has a speak() method"""
    print(entity.speak())

# All three work, even though they don't inherit from a common class!
make_it_speak(Dog())
make_it_speak(Cat())
make_it_speak(Robot())
```
@Pyodide.eval

---

### When to Use Polymorphism

✅ **Use Polymorphism When:**
- You need to treat different types uniformly
- You want to write extensible code
- You have multiple implementations of the same interface
- You want to avoid long if-else chains checking types

❌ **Don't Use Polymorphism When:**
- Classes have completely different behaviors
- The added abstraction makes code harder to understand
- You're dealing with simple, unrelated operations

---

## Encapsulation

Encapsulation restricts access to certain attributes and methods, promoting data security and integrity. In Python, private attributes are prefixed with an underscore.

### What is Encapsulation?
Encapsulation is the practice of bundling data and methods that operate on the data within one unit (class), and restricting access to some of the object's components. This prevents external code from directly accessing and modifying the internal state of an object.

**Benefits of Encapsulation:**
1. **Data Protection**: Prevents unauthorized access and modification
2. **Data Validation**: Control how data is set and retrieved
3. **Flexibility**: Internal implementation can change without affecting external code
4. **Maintainability**: Reduces dependencies between different parts of code

**Access Modifiers in Python:**
- **Public**: Accessible from anywhere (default)
- **Protected** (`_variable`): Intended for internal use (convention only)
- **Private** (`__variable`): Name mangling makes it harder to access from outside

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
```
@Pyodide.eval

**Explanation:**
The `_balance` attribute is protected, indicating it shouldn't be accessed directly. Instead, we use methods like `deposit()`, `withdraw()`, and `get_balance()` to interact with it.

---

### Advanced Example: Secure Banking System

Let's build a comprehensive banking system demonstrating advanced encapsulation techniques.

```python
class BankAccount:
    """Secure bank account with encapsulation"""
    __account_count = 0  # Private class variable
    
    def __init__(self, account_holder, initial_balance=0, account_type="Savings"):
        self.__account_number = self.__generate_account_number()
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__account_type = account_type
        self.__transaction_history = []
        self.__is_active = True
        BankAccount.__account_count += 1
        
        self.__add_transaction("Account Created", initial_balance)
    
    @classmethod
    def __generate_account_number(cls):
        """Private method to generate unique account numbers"""
        cls.__account_count += 1
        return f"ACC{cls.__account_count:06d}"
    
    def __add_transaction(self, transaction_type, amount):
        """Private method to log transactions"""
        from datetime import datetime
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": self.__balance
        }
        self.__transaction_history.append(transaction)
    
    def __validate_amount(self, amount):
        """Private method to validate transaction amounts"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return True
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if not self.__is_active:
            print("Account is inactive!")
            return False
        
        try:
            self.__validate_amount(amount)
            self.__balance += amount
            self.__add_transaction("Deposit", amount)
            print(f"✓ Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
            return True
        except ValueError as e:
            print(f"✗ Deposit failed: {e}")
            return False
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if not self.__is_active:
            print("Account is inactive!")
            return False
        
        try:
            self.__validate_amount(amount)
            if amount > self.__balance:
                print("✗ Insufficient funds!")
                return False
            
            self.__balance -= amount
            self.__add_transaction("Withdrawal", -amount)
            print(f"✓ Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
            return True
        except ValueError as e:
            print(f"✗ Withdrawal failed: {e}")
            return False
    
    def transfer(self, recipient_account, amount):
        """Transfer money to another account"""
        if not self.__is_active:
            print("Account is inactive!")
            return False
        
        print(f"\nTransferring ${amount:.2f} to {recipient_account.get_account_holder()}...")
        
        if self.withdraw(amount):
            if recipient_account.deposit(amount):
                print(f"✓ Transfer successful!")
                return True
            else:
                # Rollback if recipient deposit fails
                self.deposit(amount)
                print("✗ Transfer failed - rollback completed")
                return False
        return False
    
    def get_balance(self):
        """Public method to get balance (getter)"""
        return self.__balance
    
    def get_account_number(self):
        """Public method to get account number (getter)"""
        return self.__account_number
    
    def get_account_holder(self):
        """Public method to get account holder name (getter)"""
        return self.__account_holder
    
    def get_account_type(self):
        """Public method to get account type (getter)"""
        return self.__account_type
    
    def set_account_type(self, new_type):
        """Public method to set account type (setter)"""
        valid_types = ["Savings", "Checking", "Business"]
        if new_type in valid_types:
            self.__account_type = new_type
            self.__add_transaction("Account Type Changed", 0)
            print(f"✓ Account type changed to {new_type}")
        else:
            print(f"✗ Invalid account type. Valid types: {', '.join(valid_types)}")
    
    def close_account(self):
        """Close the account"""
        self.__is_active = False
        self.__add_transaction("Account Closed", 0)
        print(f"✓ Account {self.__account_number} has been closed")
    
    def activate_account(self):
        """Reactivate the account"""
        self.__is_active = True
        self.__add_transaction("Account Activated", 0)
        print(f"✓ Account {self.__account_number} has been activated")
    
    def get_transaction_history(self, limit=None):
        """Get transaction history"""
        transactions = self.__transaction_history[-limit:] if limit else self.__transaction_history
        
        print(f"\n{'='*70}")
        print(f"TRANSACTION HISTORY - {self.__account_holder}")
        print(f"Account: {self.__account_number}")
        print(f"{'='*70}")
        
        for i, trans in enumerate(transactions, 1):
            print(f"{i}. {trans['type']}")
            print(f"   Amount: ${trans['amount']:.2f}")
            print(f"   Date: {trans['timestamp']}")
            print(f"   Balance After: ${trans['balance_after']:.2f}")
            print("-" * 70)
    
    def display_account_info(self):
        """Display complete account information"""
        print(f"\n{'='*70}")
        print(f"ACCOUNT INFORMATION")
        print(f"{'='*70}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Type: {self.__account_type}")
        print(f"Current Balance: ${self.__balance:.2f}")
        print(f"Status: {'Active' if self.__is_active else 'Inactive'}")
        print(f"Total Transactions: {len(self.__transaction_history)}")
        print(f"{'='*70}\n")
    
    @staticmethod
    def get_total_accounts():
        """Get total number of accounts created"""
        return BankAccount.__account_count

# Demonstrate encapsulation
print("="*70)
print("SECURE BANKING SYSTEM - ENCAPSULATION DEMONSTRATION")
print("="*70)

# Create accounts
account1 = BankAccount("Alice Johnson", 1000, "Savings")
account2 = BankAccount("Bob Smith", 500, "Checking")

# Display account info
account1.display_account_info()

# Perform transactions
account1.deposit(500)
account1.withdraw(200)
account1.deposit(1000)

# Transfer between accounts
account1.transfer(account2, 300)

# View transaction history
account1.get_transaction_history(limit=5)

# Change account type
account1.set_account_type("Business")

# Try to access private attributes (will not work as expected)
print("\n--- Testing Encapsulation ---")
print("Attempting to access private attributes...")

try:
    # This will not work - attribute is private
    print(account1.__balance)
except AttributeError:
    print("✗ Cannot access __balance directly (encapsulated)")

# Correct way to access balance
print(f"✓ Correct way: balance = ${account1.get_balance():.2f}")

# Display final state
print("\n--- Final Account States ---")
account1.display_account_info()
account2.display_account_info()

print(f"Total accounts created: {BankAccount.get_total_accounts()}")
```
@Pyodide.eval

**Key Encapsulation Concepts:**
1. **Private Attributes** (`__balance`): Cannot be accessed directly from outside
2. **Private Methods** (`__validate_amount()`): Internal helper methods
3. **Getters**: Public methods to retrieve private data (`get_balance()`)
4. **Setters**: Public methods to modify private data with validation (`set_account_type()`)
5. **Data Validation**: All modifications go through controlled methods
6. **Transaction Logging**: Private history tracking

---

### Example: Secure User Authentication System

This example demonstrates encapsulation in a password management system.

```python
import hashlib

class User:
    """Secure user class with password encapsulation"""
    def __init__(self, username, password):
        self.__username = username
        self.__password_hash = self.__hash_password(password)
        self.__is_locked = False
        self.__login_attempts = 0
        self.__max_attempts = 3
    
    def __hash_password(self, password):
        """Private method to hash passwords"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def __reset_login_attempts(self):
        """Private method to reset login attempts"""
        self.__login_attempts = 0
    
    def verify_password(self, password):
        """Verify if the password is correct"""
        if self.__is_locked:
            print("✗ Account is locked!")
            return False
        
        if self.__hash_password(password) == self.__password_hash:
            print("✓ Password correct!")
            self.__reset_login_attempts()
            return True
        else:
            self.__login_attempts += 1
            remaining = self.__max_attempts - self.__login_attempts
            
            if remaining > 0:
                print(f"✗ Incorrect password. {remaining} attempts remaining.")
            else:
                self.__is_locked = True
                print("✗ Account locked due to too many failed attempts!")
            
            return False
    
    def change_password(self, old_password, new_password):
        """Change user password"""
        if self.__is_locked:
            print("✗ Account is locked!")
            return False
        
        if self.verify_password(old_password):
            if len(new_password) < 8:
                print("✗ New password must be at least 8 characters!")
                return False
            
            self.__password_hash = self.__hash_password(new_password)
            print("✓ Password changed successfully!")
            return True
        else:
            print("✗ Password change failed!")
            return False
    
    def unlock_account(self, admin_password):
        """Unlock account (admin function)"""
        if admin_password == "admin123":  # Simplified for demo
            self.__is_locked = False
            self.__reset_login_attempts()
            print("✓ Account unlocked by administrator")
            return True
        else:
            print("✗ Invalid administrator password!")
            return False
    
    def get_username(self):
        """Get username (getter)"""
        return self.__username
    
    def is_locked(self):
        """Check if account is locked"""
        return self.__is_locked
    
    def display_status(self):
        """Display user account status"""
        print(f"\n--- User: {self.__username} ---")
        print(f"Status: {'Locked' if self.__is_locked else 'Active'}")
        print(f"Login attempts: {self.__login_attempts}/{self.__max_attempts}")
        print(f"Password hash: {self.__password_hash[:20]}... (hidden)")

# Demonstrate password encapsulation
print("="*60)
print("USER AUTHENTICATION SYSTEM")
print("="*60)

user = User("alice", "SecurePass123")
user.display_status()

print("\n--- Testing Password Verification ---")
user.verify_password("WrongPassword")
user.verify_password("WrongPassword")
user.verify_password("WrongPassword")  # This should lock the account

print("\n--- Attempting Actions on Locked Account ---")
user.verify_password("SecurePass123")  # Won't work - account locked

print("\n--- Unlocking Account ---")
user.unlock_account("admin123")

print("\n--- Changing Password ---")
user.change_password("SecurePass123", "NewSecurePass456")

user.display_status()
```
@Pyodide.eval

**Advanced Encapsulation Features:**
1. **Password Hashing**: Passwords are never stored in plain text
2. **Access Control**: Private attributes prevent direct manipulation
3. **Security Logic**: Login attempts and account locking
4. **Data Hiding**: Internal state is completely hidden
5. **Controlled Access**: All operations go through public methods

**Quiz:**
What is the main purpose of encapsulation in the banking system example?

[( )] To make the code run faster  
[( )] To reduce the number of methods  
[(X)] To protect sensitive data and control how it's accessed  
[( )] To eliminate the need for validation  

**Explanation:**
Encapsulation protects sensitive data like account balance and transaction history by making them private, and provides controlled access through public methods that include validation and security checks.

---

## Understanding Encapsulation in Depth

### What is Encapsulation and Why Use It?

**Definition**: Encapsulation is the bundling of data (attributes) and methods that operate on that data into a single unit (class), while restricting direct access to some of the object's components.

**Real-World Analogy - Medicine Capsule:**
A medicine capsule encapsulates the medicine inside. You:
- ✅ Can take the capsule (use the public interface)
- ❌ Cannot directly access the medicine inside (private data)
- ✅ The capsule protects the medicine from outside contamination
- ✅ You get the benefit without knowing the internal composition

**Real-World Analogy - ATM Machine:**
When using an ATM:
- You interact through a simple interface (keypad, screen)
- You cannot access the cash directly
- You cannot see the internal mechanisms
- All operations go through controlled processes (PIN verification, balance checks)
- The machine's internal state is protected

---

### Why Use Encapsulation?

#### 1. **Data Protection** - Prevent Unauthorized Access

Without encapsulation:

```python
# WITHOUT ENCAPSULATION - Dangerous!
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Public - anyone can modify!

account = BankAccount(1000)
print(f"Balance: ${account.balance}")

# DANGER! Direct modification - no validation!
account.balance = -5000  # Negative balance?!
account.balance = "hacked"  # String instead of number?!
print(f"Balance: ${account.balance}")  # System broken!
```
@Pyodide.eval

With encapsulation:

```python
# WITH ENCAPSULATION - Safe!
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private - protected!
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✓ Deposited ${amount}")
        else:
            print("✗ Invalid amount!")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"✓ Withdrew ${amount}")
        else:
            print("✗ Insufficient funds or invalid amount!")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(f"Balance: ${account.get_balance()}")

# Protected! These operations go through validation
account.deposit(500)     # ✓ Works
account.withdraw(200)    # ✓ Works
account.withdraw(5000)   # ✗ Blocked!
account.deposit(-100)    # ✗ Blocked!

# Cannot directly modify balance
# account.__balance = -5000  # Won't work!

print(f"Final Balance: ${account.get_balance()}")
```
@Pyodide.eval

**Key Benefit**: Data integrity is maintained through controlled access!

---

#### 2. **Data Validation** - Ensure Data Consistency

Real-world example: User profile system

```python
# User profile with validation through encapsulation
class UserProfile:
    def __init__(self, username, email, age):
        self.__username = None
        self.__email = None
        self.__age = None
        self.__account_status = "active"
        
        # Use setters for validation during initialization
        self.set_username(username)
        self.set_email(email)
        self.set_age(age)
    
    def set_username(self, username):
        """Setter with validation"""
        if len(username) >= 3 and username.isalnum():
            self.__username = username
            print(f"✓ Username set to: {username}")
        else:
            print("✗ Invalid username! Must be alphanumeric and at least 3 characters")
    
    def set_email(self, email):
        """Setter with validation"""
        if "@" in email and "." in email.split("@")[1]:
            self.__email = email
            print(f"✓ Email set to: {email}")
        else:
            print("✗ Invalid email format!")
    
    def set_age(self, age):
        """Setter with validation"""
        if isinstance(age, int) and 13 <= age <= 120:
            self.__age = age
            print(f"✓ Age set to: {age}")
        else:
            print("✗ Invalid age! Must be between 13 and 120")
    
    def get_username(self):
        return self.__username
    
    def get_email(self):
        # Don't reveal full email for privacy
        parts = self.__email.split("@")
        return f"{parts[0][:2]}***@{parts[1]}"
    
    def get_age(self):
        return self.__age
    
    def deactivate_account(self):
        self.__account_status = "deactivated"
        print("✓ Account deactivated")
    
    def display_profile(self):
        print(f"\n{'='*50}")
        print(f"USER PROFILE")
        print(f"{'='*50}")
        print(f"Username: {self.__username}")
        print(f"Email: {self.get_email()}")
        print(f"Age: {self.__age}")
        print(f"Status: {self.__account_status}")
        print(f"{'='*50}\n")

# Create user profile
user = UserProfile("john_doe", "john@example.com", 25)
user.display_profile()

# Try invalid operations - all blocked!
print("\n--- Testing Validation ---")
user.set_username("ab")  # Too short
user.set_username("valid_user123")  # Valid
user.set_email("invalid_email")  # Invalid format
user.set_age(150)  # Out of range
user.set_age(30)  # Valid

user.display_profile()
```
@Pyodide.eval

**Key Benefit**: Invalid data is rejected before it can corrupt the object's state!

---

#### 3. **Implementation Hiding** - Change Internal Without Breaking External Code

Real-world example: Temperature sensor

```python
# Temperature sensor with changing implementation
class TemperatureSensor:
    def __init__(self):
        # Internal implementation details (hidden)
        self.__celsius = 25.0
        self.__calibration_offset = 0.0
    
    def __convert_to_fahrenheit(self, celsius):
        """Private method - implementation detail"""
        return (celsius * 9/5) + 32
    
    def __apply_calibration(self, raw_value):
        """Private method - implementation detail"""
        return raw_value + self.__calibration_offset
    
    def get_temperature(self, unit="C"):
        """Public interface - users only see this"""
        calibrated_temp = self.__apply_calibration(self.__celsius)
        
        if unit.upper() == "C":
            return f"{calibrated_temp:.1f}°C"
        elif unit.upper() == "F":
            return f"{self.__convert_to_fahrenheit(calibrated_temp):.1f}°F"
        elif unit.upper() == "K":
            return f"{calibrated_temp + 273.15:.1f}K"
        else:
            return "Invalid unit"
    
    def calibrate(self, offset):
        """Public interface for calibration"""
        self.__calibration_offset = offset
        print(f"✓ Sensor calibrated with offset: {offset}°C")

# Version 1: Simple sensor
sensor = TemperatureSensor()
print("Temperature readings:")
print(sensor.get_temperature("C"))
print(sensor.get_temperature("F"))
print(sensor.get_temperature("K"))

# Now we can change the internal implementation without breaking external code!
# For example, we could:
# - Change how temperature is stored (Fahrenheit instead of Celsius)
# - Add network connectivity
# - Implement caching
# - Use different calibration algorithms
# Users don't need to change their code!
```
@Pyodide.eval

**Key Benefit**: Internal changes don't affect external code that uses the class!

---

#### 4. **Security** - Protect Sensitive Information

Real-world example: Credit card processing

```python
# Credit card with secure encapsulation
class CreditCard:
    def __init__(self, card_number, cvv, pin):
        self.__card_number = card_number
        self.__cvv = cvv
        self.__pin = self.__hash_pin(pin)
        self.__balance = 5000
        self.__is_blocked = False
        self.__failed_attempts = 0
    
    def __hash_pin(self, pin):
        """Private method to hash PIN"""
        # Simple hash for demonstration
        return str(hash(str(pin)))
    
    def __verify_pin(self, pin):
        """Private method to verify PIN"""
        return self.__hash_pin(pin) == self.__pin
    
    def __mask_card_number(self):
        """Private method to mask card number"""
        return f"****-****-****-{self.__card_number[-4:]}"
    
    def get_card_info(self):
        """Public method - returns safe information only"""
        return {
            "card_number": self.__mask_card_number(),
            "balance": f"${self.__balance:.2f}",
            "status": "Blocked" if self.__is_blocked else "Active"
        }
    
    def make_purchase(self, amount, pin):
        """Public method with security checks"""
        if self.__is_blocked:
            print("✗ Card is blocked!")
            return False
        
        if not self.__verify_pin(pin):
            self.__failed_attempts += 1
            print(f"✗ Incorrect PIN! Attempts: {self.__failed_attempts}/3")
            
            if self.__failed_attempts >= 3:
                self.__is_blocked = True
                print("✗ Card blocked due to multiple failed attempts!")
            return False
        
        if amount > self.__balance:
            print("✗ Insufficient funds!")
            return False
        
        self.__balance -= amount
        self.__failed_attempts = 0  # Reset on successful transaction
        print(f"✓ Purchase of ${amount:.2f} approved!")
        print(f"  Remaining balance: ${self.__balance:.2f}")
        return True
    
    def change_pin(self, old_pin, new_pin):
        """Public method to change PIN"""
        if self.__is_blocked:
            print("✗ Card is blocked!")
            return False
        
        if not self.__verify_pin(old_pin):
            print("✗ Incorrect current PIN!")
            return False
        
        if len(str(new_pin)) != 4:
            print("✗ PIN must be 4 digits!")
            return False
        
        self.__pin = self.__hash_pin(new_pin)
        print("✓ PIN changed successfully!")
        return True

# Usage
print("="*60)
print("SECURE CREDIT CARD SYSTEM")
print("="*60)

card = CreditCard("1234567890123456", "123", "1234")

# Display safe information
print("\nCard Information:")
info = card.get_card_info()
for key, value in info.items():
    print(f"  {key}: {value}")

# Try transactions
print("\n--- Transaction Tests ---")
card.make_purchase(100.00, "1234")  # Correct PIN
card.make_purchase(50.00, "0000")   # Wrong PIN
card.make_purchase(50.00, "1111")   # Wrong PIN
card.make_purchase(50.00, "2222")   # Wrong PIN - should block card

# Try accessing private data (won't work!)
print("\n--- Security Test ---")
try:
    print(card.__card_number)  # Won't work!
except AttributeError:
    print("✓ Card number is protected - cannot access directly")

try:
    print(card.__pin)  # Won't work!
except AttributeError:
    print("✓ PIN is protected - cannot access directly")

print("\nFinal card info:")
info = card.get_card_info()
for key, value in info.items():
    print(f"  {key}: {value}")
```
@Pyodide.eval

**Key Benefit**: Sensitive information like card numbers and PINs are completely protected!

---

### Levels of Access Control in Python

Python provides three levels of access control for class members: **public**, **protected**, and **private**. Understanding these levels helps you control how attributes and methods can be accessed from outside the class.

#### 1. Public (No Prefix) - Fully Accessible

**Explanation**: Public attributes and methods have no underscore prefix. They can be accessed from anywhere - inside the class, outside the class, and in subclasses.

**When to use**: Use public members for data and methods that are part of the class's official interface and should be accessible to all users.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.balance = balance      # Public attribute
    
    def get_info(self):            # Public method
        return f"Account owner: {self.owner}, Balance: ${self.balance}"
    
    def deposit(self, amount):     # Public method
        self.balance += amount
        print(f"✓ Deposited ${amount}. New balance: ${self.balance}")

# Usage - all members are accessible
account = BankAccount("John Doe", 1000)
print(account.owner)               # ✓ Direct access to public attribute
print(f"Balance: ${account.balance}")  # ✓ Direct access to public attribute
print(account.get_info())          # ✓ Call public method
account.deposit(500)               # ✓ Call public method
```
@Pyodide.eval

---

#### 2. Protected (Single Underscore _) - Convention-Based Access

**Explanation**: Protected attributes and methods have a single underscore prefix (e.g., `_variable`). This is a **convention** indicating that these members are intended for internal use within the class and its subclasses. However, Python doesn't enforce this - you can still access them from outside.

**When to use**: Use protected members for internal implementation details that subclasses might need to access, but external users should avoid.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name                    # Public
        self._salary = salary               # Protected - internal use
        self._employee_id = self._generate_id()  # Protected
    
    def _generate_id(self):                 # Protected method
        """Internal helper method"""
        import random
        return f"EMP{random.randint(1000, 9999)}"
    
    def get_info(self):                     # Public method
        return f"{self.name} (ID: {self._employee_id})"
    
    def _calculate_bonus(self):             # Protected method
        """Internal calculation - may be used by subclasses"""
        return self._salary * 0.10

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def get_total_compensation(self):
        # Subclass CAN access protected members
        bonus = self._calculate_bonus()     # ✓ Accessing protected method
        team_bonus = self.team_size * 100
        return self._salary + bonus + team_bonus  # ✓ Accessing protected attribute

# Usage
employee = Employee("Alice", 50000)
print(employee.get_info())                  # ✓ Public method - recommended
print(f"Salary: ${employee._salary}")       # ⚠️ Works but discouraged (protected)

manager = Manager("Bob", 80000, 5)
print(f"Total compensation: ${manager.get_total_compensation()}")
```
@Pyodide.eval

---

#### 3. Private (Double Underscore __) - Name Mangling

**Explanation**: Private attributes and methods have a double underscore prefix (e.g., `__variable`). Python uses **name mangling** to make these members harder to access from outside the class. The name is internally changed to `_ClassName__variable`.

**When to use**: Use private members for critical internal details that should not be accessed or modified from outside, even by subclasses.

```python
class SecureAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner                  # Public
        self._account_number = "ACC123456"  # Protected
        self.__balance = balance            # Private - name mangling
        self.__pin = pin                    # Private - sensitive data
    
    def __verify_pin(self, entered_pin):    # Private method
        """Internal security check"""
        return entered_pin == self.__pin
    
    def withdraw(self, amount, pin):        # Public method
        if not self.__verify_pin(pin):      # ✓ Access private method internally
            print("✗ Invalid PIN!")
            return False
        
        if amount > self.__balance:         # ✓ Access private attribute internally
            print("✗ Insufficient funds!")
            return False
        
        self.__balance -= amount            # ✓ Modify private attribute internally
        print(f"✓ Withdrew ${amount}. Remaining balance: ${self.__balance}")
        return True
    
    def get_balance(self, pin):            # Public method with security
        if self.__verify_pin(pin):
            return self.__balance
        else:
            print("✗ Invalid PIN!")
            return None

# Usage
account = SecureAccount("Jane Smith", 5000, "1234")

# Public interface - works perfectly
print(f"Owner: {account.owner}")           # ✓ Public attribute
account.withdraw(1000, "1234")             # ✓ Public method with correct PIN
account.withdraw(500, "wrong")             # ✗ Public method with wrong PIN

# Try to access private members - won't work as expected
try:
    print(account.__balance)                # ✗ AttributeError - private!
except AttributeError as e:
    print(f"Error: Cannot access __balance directly")

try:
    print(account.__pin)                    # ✗ AttributeError - private!
except AttributeError as e:
    print(f"Error: Cannot access __pin directly")

# Name mangling - this is how Python actually stores it
# (You should NEVER do this in real code!)
print(f"\n⚠️ Name mangling example (don't use this!):")
print(f"Internal name: {account._SecureAccount__balance}")  # ⚠️ Workaround (bad practice)
```
@Pyodide.eval

---

#### Summary of Access Levels

| Access Level | Syntax | Accessible From | Use Case |
|-------------|--------|----------------|----------|
| **Public** | `name` | Everywhere | Public API, official interface |
| **Protected** | `_name` | Class & subclasses (by convention) | Internal helpers, subclass support |
| **Private** | `__name` | Only within the class (name mangling) | Critical internals, sensitive data |

```python
# Complete example showing all three levels
class SmartPhone:
    def __init__(self, model, price):
        # Public attributes
        self.model = model
        self.brand = "TechCorp"
        
        # Protected attributes (internal use, subclasses may access)
        self._price = price
        self._warranty_years = 2
        
        # Private attributes (truly internal, name mangled)
        self.__serial_number = self.__generate_serial()
        self.__encryption_key = "secret_key_12345"
    
    def __generate_serial(self):            # Private method
        """Internal - generates unique serial number"""
        import random
        return f"SN{random.randint(100000, 999999)}"
    
    def _calculate_discount(self):          # Protected method
        """Internal - may be used by subclasses"""
        return self._price * 0.05
    
    def get_price(self):                    # Public method
        """Official way to get price"""
        return self._price
    
    def get_info(self):                     # Public method
        """Public interface - shows safe information"""
        return f"{self.brand} {self.model} - ${self._price}"

# Usage demonstration
phone = SmartPhone("X Pro", 999)

# ✓ Public access - recommended
print(phone.model)
print(phone.brand)
print(phone.get_info())

# ⚠️ Protected access - works but discouraged
print(f"Direct protected access: ${phone._price}")

# ✗ Private access - fails (as intended)
try:
    print(phone.__serial_number)
except AttributeError:
    print("Cannot access private __serial_number")

try:
    print(phone.__encryption_key)
except AttributeError:
    print("Cannot access private __encryption_key")
```
@Pyodide.eval

### When to Use Encapsulation

✅ **Use Encapsulation When:**
- Data needs validation before being set
- You want to protect sensitive information
- You need to maintain data integrity
- You want flexibility to change internal implementation
- You're building APIs or libraries for others to use

❌ **Don't Use Encapsulation When:**
- Data is truly public and doesn't need protection
- Over-encapsulation makes simple code unnecessarily complex
- You're working on small, private scripts

---

## Abstraction

Abstraction is the process of hiding the implementation details and showing only the functionality to the user. It is achieved using abstract classes and methods in Python.

### What is Abstraction?
Abstraction focuses on what an object does instead of how it does it. Abstract classes cannot be instantiated directly.

### What is Abstraction and Why Use It?

**Definition**: Abstraction is the process of hiding complex implementation details and showing only the essential features of an object. It focuses on WHAT an object does rather than HOW it does it.

**Real-World Analogy - Driving a Car:**
When you drive a car:
- ✅ You know: Press accelerator → car moves forward
- ❌ You don't know: How the fuel injection system works, how the transmission shifts gears
- ✅ You interact with: Steering wheel, pedals, gear shift (abstract interface)
- ❌ You don't interact with: Engine internals, fuel pump, transmission gears

**Real-World Analogy - TV Remote:**
- ✅ You see: Volume up/down, channel change, power button
- ❌ You don't see: Signal processing, infrared transmission, frequency modulation
- The complex internal workings are abstracted away!

---

### Why Use Abstraction?

#### 1. **Simplicity** - Hide Complexity

Without abstraction:

```python
# WITHOUT ABSTRACTION - User needs to know all details
class EmailSender:
    def send_email(self, to, subject, body):
        # User must handle all these details
        print("1. Opening SMTP connection...")
        print("2. Authenticating with server...")
        print("3. Creating email headers...")
        print("4. Encoding email body...")
        print("5. Sending email...")
        print("6. Closing connection...")
        print(f"✓ Email sent to {to}")

# User needs to understand all steps
sender = EmailSender()
sender.send_email("user@example.com", "Hello", "Message body")
```

With abstraction:

```python
# WITH ABSTRACTION - Simple interface
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, to, message):
        """Abstract method - subclasses implement the details"""
        pass

class EmailSender(MessageSender):
    def send(self, to, message):
        # All complexity hidden inside
        self.__connect()
        self.__authenticate()
        self.__send_message(to, message)
        self.__disconnect()
        print(f"✓ Email sent to {to}")
    
    def __connect(self):
        pass  # Complex connection logic hidden
    
    def __authenticate(self):
        pass  # Complex auth logic hidden
    
    def __send_message(self, to, message):
        pass  # Complex sending logic hidden
    
    def __disconnect(self):
        pass  # Complex disconnection logic hidden

class SMSSender(MessageSender):
    def send(self, to, message):
        # Different implementation, same simple interface
        print(f"✓ SMS sent to {to}")

# Simple usage - complexity is abstracted!
email_sender = EmailSender()
sms_sender = SMSSender()

email_sender.send("user@example.com", "Hello!")
sms_sender.send("+1-555-0100", "Hello!")
```
@Pyodide.eval

**Key Benefit**: Users don't need to understand complex implementation details!

---

#### 2. **Code Organization** - Define Clear Contracts

Real-world example: Payment gateway system

```python
from abc import ABC, abstractmethod

# Abstract base class defines the contract
class PaymentGateway(ABC):
    """
    Abstract payment gateway - defines WHAT operations are needed
    without specifying HOW they should be implemented
    """
    
    @abstractmethod
    def initialize_payment(self, amount):
        """Initialize payment - must be implemented"""
        pass
    
    @abstractmethod
    def process_payment(self):
        """Process the payment - must be implemented"""
        pass
    
    @abstractmethod
    def verify_payment(self):
        """Verify payment status - must be implemented"""
        pass
    
    @abstractmethod
    def refund_payment(self):
        """Refund the payment - must be implemented"""
        pass

# Concrete implementation for Stripe
class StripeGateway(PaymentGateway):
    def __init__(self):
        self.amount = 0
        self.payment_status = "pending"
    
    def initialize_payment(self, amount):
        self.amount = amount
        print(f"[Stripe] Initializing payment of ${amount}")
        return True
    
    def process_payment(self):
        print(f"[Stripe] Processing payment of ${self.amount}")
        print("  - Connecting to Stripe API")
        print("  - Tokenizing payment method")
        print("  - Charging card")
        self.payment_status = "completed"
        return True
    
    def verify_payment(self):
        print(f"[Stripe] Verifying payment status: {self.payment_status}")
        return self.payment_status == "completed"
    
    def refund_payment(self):
        if self.payment_status == "completed":
            print(f"[Stripe] Refunding ${self.amount}")
            self.payment_status = "refunded"
            return True
        return False

# Concrete implementation for PayPal
class PayPalGateway(PaymentGateway):
    def __init__(self):
        self.amount = 0
        self.payment_status = "pending"
    
    def initialize_payment(self, amount):
        self.amount = amount
        print(f"[PayPal] Initializing payment of ${amount}")
        return True
    
    def process_payment(self):
        print(f"[PayPal] Processing payment of ${self.amount}")
        print("  - Redirecting to PayPal")
        print("  - Authenticating user")
        print("  - Completing transaction")
        self.payment_status = "completed"
        return True
    
    def verify_payment(self):
        print(f"[PayPal] Verifying payment status: {self.payment_status}")
        return self.payment_status == "completed"
    
    def refund_payment(self):
        if self.payment_status == "completed":
            print(f"[PayPal] Refunding ${self.amount}")
            self.payment_status = "refunded"
            return True
        return False

# High-level function using abstraction
def process_order(payment_gateway: PaymentGateway, amount):
    """
    Process an order - works with ANY payment gateway!
    We don't need to know HOW each gateway works
    """
    print(f"\n{'='*60}")
    print(f"PROCESSING ORDER")
    print(f"{'='*60}")
    
    if payment_gateway.initialize_payment(amount):
        if payment_gateway.process_payment():
            if payment_gateway.verify_payment():
                print(f"✓ Order completed successfully!")
                return True
    
    print(f"✗ Order failed!")
    return False

# Usage - same code works with different gateways!
print("="*60)
print("E-COMMERCE PAYMENT SYSTEM")
print("="*60)

stripe = StripeGateway()
paypal = PayPalGateway()

process_order(stripe, 99.99)
process_order(paypal, 149.99)
```
@Pyodide.eval

**Key Benefit**: Clear contract ensures all payment gateways have the same interface!

---

#### 3. **Flexibility** - Easy to Swap Implementations

Real-world example: Database abstraction layer

```python
from abc import ABC, abstractmethod

# Abstract database interface
class Database(ABC):
    """Abstract database - defines operations without implementation"""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def load(self, id):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass

# SQL Database implementation
class SQLDatabase(Database):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self):
        print(f"[SQL] Connecting to {self.connection_string}")
        self.connected = True
    
    def disconnect(self):
        print("[SQL] Disconnecting")
        self.connected = False
    
    def save(self, data):
        print(f"[SQL] INSERT INTO table VALUES ({data})")
        return f"SQL-{data['id']}"
    
    def load(self, id):
        print(f"[SQL] SELECT * FROM table WHERE id = {id}")
        return {"id": id, "data": "SQL data"}
    
    def delete(self, id):
        print(f"[SQL] DELETE FROM table WHERE id = {id}")

# NoSQL Database implementation
class NoSQLDatabase(Database):
    def __init__(self, cluster_url):
        self.cluster_url = cluster_url
        self.connected = False
    
    def connect(self):
        print(f"[NoSQL] Connecting to {self.cluster_url}")
        self.connected = True
    
    def disconnect(self):
        print("[NoSQL] Disconnecting")
        self.connected = False
    
    def save(self, data):
        print(f"[NoSQL] db.collection.insert({data})")
        return f"NoSQL-{data['id']}"
    
    def load(self, id):
        print(f"[NoSQL] db.collection.findOne({{_id: {id}}})")
        return {"id": id, "data": "NoSQL data"}
    
    def delete(self, id):
        print(f"[NoSQL] db.collection.remove({{_id: {id}}})")

# Application using database abstraction
class Application:
    def __init__(self, database: Database):
        self.db = database
    
    def start(self):
        print("\n[App] Starting application...")
        self.db.connect()
    
    def stop(self):
        print("[App] Stopping application...")
        self.db.disconnect()
    
    def create_user(self, user_data):
        print(f"\n[App] Creating user: {user_data['name']}")
        return self.db.save(user_data)
    
    def get_user(self, user_id):
        print(f"\n[App] Getting user: {user_id}")
        return self.db.load(user_id)
    
    def remove_user(self, user_id):
        print(f"\n[App] Removing user: {user_id}")
        self.db.delete(user_id)

# Test with SQL database
print("="*60)
print("TESTING WITH SQL DATABASE")
print("="*60)

sql_db = SQLDatabase("mysql://localhost:3306/mydb")
app1 = Application(sql_db)
app1.start()
app1.create_user({"id": 1, "name": "Alice"})
app1.get_user(1)
app1.stop()

# Switch to NoSQL - NO APPLICATION CODE CHANGES!
print("\n" + "="*60)
print("TESTING WITH NOSQL DATABASE")
print("="*60)

nosql_db = NoSQLDatabase("mongodb://localhost:27017")
app2 = Application(nosql_db)
app2.start()
app2.create_user({"id": 2, "name": "Bob"})
app2.get_user(2)
app2.stop()
```
@Pyodide.eval

**Key Benefit**: Can switch database implementations without changing application code!

---

#### 4. **Maintainability** - Changes Don't Break Dependent Code

Real-world example: Logging system

```python
```python
from abc import ABC, abstractmethod
from datetime import datetime

```python
# Abstract logger interface
from abc import ABC, abstractmethod
from datetime import datetime

class Logger(ABC):
    @abstractmethod
    def log(self, level, message):
        """Log a message - implementation varies"""
        pass
    
    @abstractmethod
    def info(self, message):
        pass
    
    @abstractmethod
    def warning(self, message):
        pass
    
    @abstractmethod
    def error(self, message):
        pass

# Console logger
class ConsoleLogger(Logger):
    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
    
    def info(self, message):
        self.log("INFO", message)
    
    def warning(self, message):
        self.log("WARNING", message)
    
    def error(self, message):
        self.log("ERROR", message)

# File logger
class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
        self.logs = []
    
    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_entry)
        print(f"[FileLogger] Logged to {self.filename}: {log_entry}")
    
    def info(self, message):
        self.log("INFO", message)
    
    def warning(self, message):
        self.log("WARNING", message)
    
    def error(self, message):
        self.log("ERROR", message)
    
    def get_logs(self):
        return "\n".join(self.logs)

# Application using logger abstraction
class WebServer:
    def __init__(self, logger: Logger):
        self.logger = logger
    
    def start(self):
        self.logger.info("Server starting...")
        self.logger.info("Listening on port 8080")
    
    def handle_request(self, request):
        self.logger.info(f"Handling request: {request}")
        if "error" in request:
            self.logger.error(f"Error processing {request}")
        elif "warn" in request:
            self.logger.warning(f"Warning for {request}")
    
    def stop(self):
        self.logger.info("Server stopping...")

# Usage with console logger
print("="*60)
print("WEB SERVER WITH CONSOLE LOGGING")
print("="*60)

console_logger = ConsoleLogger()
server1 = WebServer(console_logger)
server1.start()
server1.handle_request("GET /home")
server1.handle_request("POST /error")
server1.handle_request("GET /warn")
server1.stop()

# Usage with file logger - NO SERVER CODE CHANGES!
print("\n" + "="*60)
print("WEB SERVER WITH FILE LOGGING")
print("="*60)

file_logger = FileLogger("server.log")
server2 = WebServer(file_logger)
server2.start()
server2.handle_request("GET /api/users")
server2.handle_request("POST /api/error")
server2.stop()

print("\n--- Log File Contents ---")
print(file_logger.get_logs())
```
@Pyodide.eval


**Key Benefit**: Can change logging strategy without modifying the WebServer class!

---

### Abstraction vs Encapsulation

**Encapsulation**: Hides data and implementation (HOW)  
**Abstraction**: Hides complexity and shows only essential features (WHAT)

```python
# Example showing both concepts
from abc import ABC, abstractmethod

# ABSTRACTION - defines WHAT operations are available
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

# ENCAPSULATION - hides HOW the engine works
class Car(Vehicle):
    def __init__(self):
        self.__engine_running = False  # Encapsulated
        self.__fuel_level = 100        # Encapsulated
    
    def start_engine(self):
        """Public interface (Abstraction)"""
        if self.__check_fuel():      # Private method (Encapsulation)
            self.__ignite_engine()    # Private method (Encapsulation)
            self.__engine_running = True
            print("✓ Engine started")
        else:
            print("✗ Insufficient fuel")
    
    def stop_engine(self):
        """Public interface (Abstraction)"""
        self.__engine_running = False
        print("✓ Engine stopped")
    
    # Private methods (Encapsulation) - implementation details hidden
    def __check_fuel(self):
        return self.__fuel_level > 0
    
    def __ignite_engine(self):
        pass  # Complex ignition logic hidden

car = Car()
car.start_engine()  # Abstraction - simple interface
car.stop_engine()   # Abstraction - simple interface
# Cannot access __engine_running or __ignite_engine() - Encapsulation
```
@Pyodide.eval

---

### When to Use Abstraction

✅ **Use Abstraction When:**
- You want to define a contract for subclasses
- You're building a framework or library
- Multiple implementations share a common interface
- You want to hide complex implementation details

❌ **Don't Use Abstraction When:**
- You have a simple class with no variations
- Over-abstraction makes code harder to understand
- You're not planning multiple implementations

---

## Advanced Activities

### Activity 1: Create a Class Hierarchy

**Objective**: Design a class hierarchy for a library system. Include classes for `Book`, `Member`, and `Librarian`. Implement methods for borrowing and returning books.

**Requirements**:
1. Create a `Book` class with attributes: `title`, `author`, `isbn`, and `is_borrowed` (boolean).
2. Create a `Member` class with attributes: `name`, `member_id`, and `borrowed_books` (list).
3. Create a `Librarian` class that inherits from `Member` and has additional privileges.
4. Implement methods:
   - `borrow_book(book)`: Allow a member to borrow a book if it's available.
   - `return_book(book)`: Allow a member to return a borrowed book.
   - `display_books()`: Display all borrowed books for a member.

**Step-by-Step Guide**:
1. Start by defining the `Book` class with an `__init__` method.
2. Add a method to mark the book as borrowed or returned.
3. Define the `Member` class with an empty list for borrowed books.
4. Implement the `borrow_book` method to check if the book is available.
5. Implement the `return_book` method to remove the book from the member's list.
6. Create the `Librarian` class that inherits from `Member` and can view all members' borrowed books.

**Your Turn**: Write your code below.

```python
# Write your Book class here
class Book:
    def __init__(self, title, author, isbn):
        # Your code here
        pass

# Write your Member class here
class Member:
    def __init__(self, name, member_id):
        # Your code here
        pass
    
    def borrow_book(self, book):
        # Your code here
        pass
    
    def return_book(self, book):
        # Your code here
        pass

# Write your Librarian class here
class Librarian(Member):
    def __init__(self, name, member_id):
        # Your code here
        pass

# Test your implementation
book1 = Book("Python Programming", "John Doe", "123456")
member1 = Member("Alice", "M001")
member1.borrow_book(book1)
print(f"{member1.name} borrowed: {book1.title}")
```
@Pyodide.eval

**Expected Output**:
```
Alice borrowed: Python Programming
```

---

### Activity 2: Implement Polymorphism

**Objective**: Create a program that calculates the area of different shapes (e.g., `Triangle`, `Square`, `Circle`) using polymorphism.

**Requirements**:
1. Create a base class `Shape` with an abstract method `area()`.
2. Create subclasses `Triangle`, `Square`, and `Circle` that implement the `area()` method.
3. Use a loop to calculate and display the area of multiple shapes.

**Step-by-Step Guide**:
1. Import the `ABC` and `abstractmethod` from the `abc` module.
2. Define the `Shape` class as an abstract base class with an abstract method `area()`.
3. Create the `Triangle` class with attributes `base` and `height`.
4. Create the `Square` class with attribute `side`.
5. Create the `Circle` class with attribute `radius`.
6. Implement the `area()` method in each subclass.
7. Create a list of different shapes and iterate through them to calculate their areas.

**Your Turn**: Write your code below.

```python
from abc import ABC, abstractmethod

# Write your Shape abstract class here
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Write your Triangle class here
class Triangle(Shape):
    def __init__(self, base, height):
        # Your code here
        pass
    
    def area(self):
        # Your code here (Area = 0.5 * base * height)
        pass

# Write your Square class here
class Square(Shape):
    def __init__(self, side):
        # Your code here
        pass
    
    def area(self):
        # Your code here (Area = side * side)
        pass

# Write your Circle class here
class Circle(Shape):
    def __init__(self, radius):
        # Your code here
        pass
    
    def area(self):
        # Your code here (Area = 3.14 * radius * radius)
        pass

# Test your implementation
shapes = [Triangle(10, 5), Square(4), Circle(3)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
```
@Pyodide.eval

**Expected Output**:
```
Triangle area: 25.0
Square area: 16
Circle area: 28.26
```

---

### Activity 3: Secure Bank Account

**Objective**: Enhance the `BankAccount` class to include password protection for deposits and withdrawals.

**Requirements**:
1. Add a `password` attribute to the `BankAccount` class.
2. Modify the `deposit` and `withdraw` methods to require password verification.
3. Add a method `change_password(old_password, new_password)` to update the password.
4. Ensure that operations fail if the password is incorrect.

**Step-by-Step Guide**:
1. Modify the `__init__` method to accept and store a password.
2. Update the `deposit` method to accept a password parameter and verify it before proceeding.
3. Update the `withdraw` method similarly.
4. Implement the `change_password` method to verify the old password before setting a new one.
5. Add appropriate error messages for incorrect passwords.

**Your Turn**: Write your code below.

```python
# Write your secure BankAccount class here
class BankAccount:
    def __init__(self, balance, password):
        self._balance = balance
        self._password = password
    
    def deposit(self, amount, password):
        # Verify password and deposit
        # Your code here
        pass
    
    def withdraw(self, amount, password):
        # Verify password and withdraw
        # Your code here
        pass
    
    def change_password(self, old_password, new_password):
        # Verify old password and set new password
        # Your code here
        pass
    
    def get_balance(self, password):
        # Verify password and return balance
        # Your code here
        pass

# Test your implementation
account = BankAccount(1000, "secure123")
account.deposit(500, "secure123")
print(f"Balance: {account.get_balance('secure123')}")
account.withdraw(200, "wrong_password")  # Should fail
```
@Pyodide.eval

**Expected Output**:
```
Balance: 1500
Incorrect password. Withdrawal failed.
```

---

### Activity 4: Abstract Factory Pattern

**Objective**: Implement an abstract factory pattern to create different types of vehicles (e.g., `Car`, `Truck`, `Motorcycle`).

**Requirements**:
1. Create an abstract `Vehicle` class with methods `start_engine()` and `stop_engine()`.
2. Create concrete classes `Car`, `Truck`, and `Motorcycle` that inherit from `Vehicle`.
3. Create a `VehicleFactory` class with a method `create_vehicle(vehicle_type)` that returns the appropriate vehicle object.
4. Test the factory by creating different types of vehicles.

**Step-by-Step Guide**:
1. Define the abstract `Vehicle` class with abstract methods `start_engine()` and `stop_engine()`.
2. Create the `Car` class that implements these methods.
3. Create the `Truck` and `Motorcycle` classes similarly.
4. Define the `VehicleFactory` class with a `create_vehicle` method.
5. Use conditional logic in the factory method to return the appropriate vehicle type.
6. Test the factory by creating instances of different vehicles.

**Your Turn**: Write your code below.

```python
from abc import ABC, abstractmethod

# Write your abstract Vehicle class here
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

# Write your Car class here
class Car(Vehicle):
    def start_engine(self):
        # Your code here
        pass
    
    def stop_engine(self):
        # Your code here
        pass

# Write your Truck class here
class Truck(Vehicle):
    def start_engine(self):
        # Your code here
        pass
    
    def stop_engine(self):
        # Your code here
        pass

# Write your Motorcycle class here
class Motorcycle(Vehicle):
    def start_engine(self):
        # Your code here
        pass
    
    def stop_engine(self):
        # Your code here
        pass

# Write your VehicleFactory class here
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        # Your code here (use if-elif-else to return the right vehicle)
        pass

# Test your implementation
factory = VehicleFactory()
car = factory.create_vehicle("car")
truck = factory.create_vehicle("truck")
motorcycle = factory.create_vehicle("motorcycle")

car.start_engine()
truck.start_engine()
motorcycle.start_engine()
```
@Pyodide.eval

**Expected Output**:
```
Car engine started.
Truck engine started.
Motorcycle engine started.
```


---

## Additional Resources

- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Python OOP Concepts](https://realpython.com/python3-object-oriented-programming/)
- [Python Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Python Abstract Base Classes](https://docs.python.org/3/library/abc.html)

---

## Recap

@recap

---