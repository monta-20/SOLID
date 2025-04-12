# SOLID Principles in Python - README

## Overview
This repository demonstrates the five fundamental SOLID principles of object-oriented design implemented in Python. SOLID is an acronym that represents five design principles intended to make software designs more understandable, flexible, and maintainable.

---

## The Five SOLID Principles

### 1. Single Responsibility Principle (SRP)
**Purpose:** A class should have only one reason to change, meaning it should have only one job or responsibility.

**Key Benefits:**
- Reduces class complexity  
- Improves code organization  
- Makes classes easier to test and maintain

**Example:**  
**Bad:** A class that handles both user authentication and data storage  
**Good:** Separate classes for authentication logic and data storage  

**Link:** [GeeksforGeeks - SRP](https://www.geeksforgeeks.org/single-responsibility-in-solid-design-principle/)

---

### 2. Open/Closed Principle (OCP)
**Purpose:** Software entities should be open for extension but closed for modification.

**Key Benefits:**
- Allows adding new features without changing existing code  
- Reduces risk of introducing bugs in existing functionality  
- Promotes code reuse through inheritance and polymorphism

**Example:**  
**Bad:** A shape calculator that needs modification for each new shape  
**Good:** A calculator that works with any shape implementing a common interface  

**Link:** [Medium - OCP](https://medium.com/@ahmedtahaelelemy/the-open-closed-principle-ocp-a-deep-dive-with-case-studies-and-code-examples-44485e5a11ba)

---

### 3. Liskov Substitution Principle (LSP)
**Purpose:** Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

**Key Benefits:**
- Ensures proper inheritance hierarchies  
- Prevents unexpected behavior when substituting types  
- Enables polymorphism to work reliably

**Example:**  
**Bad:** A `Square` class that inherits from `Rectangle` but violates rectangle behavior  
**Good:** Both `Square` and `Rectangle` implementing a common `Shape` interface  

**Link:** [Medium - LSP](https://medium.com/@ahmedtahaelelemy/understanding-the-liskov-substitution-principle-a-deep-dive-into-solid-principles-b02ac6a18ee3)

---

### 4. Interface Segregation Principle (ISP)
**Purpose:** Clients should not be forced to depend on interfaces they don't use.

**Key Benefits:**
- Prevents "fat" interfaces with too many methods  
- Reduces implementation burden on classes  
- Makes interfaces more focused and cohesive

**Example:**  
**Bad:** A `Worker` interface requiring robots to implement `eat()` and `sleep()`  
**Good:** Separate interfaces for `Workable`, `Eatable`, and `Sleepable`  

**Link:** [Reflectoring - ISP](https://reflectoring.io/interface-segregation-principle/)

---

### 5. Dependency Inversion Principle (DIP)
**Purpose:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Key Benefits:**
- Reduces coupling between components  
- Makes code more flexible and testable  
- Enables easier swapping of implementations

**Example:**  
**Bad:** A `Switch` class directly controlling a `LightBulb`  
**Good:** A `Switch` controlling any device implementing a `Switchable` interface  

**Link:** [GeeksforGeeks - DIP](https://www.geeksforgeeks.org/dependecy-inversion-principle-solid/)

---

## How to Use This Repository

### Clone the repository:
```bash
git clone https://github.com/monta-20/SOLID.git
cd SOLID
