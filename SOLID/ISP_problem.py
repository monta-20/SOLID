from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human working...")
    
    def eat(self):
        print("Human eating...")
    
    def sleep(self):
        print("Human sleeping...")

class RobotWorker(Worker):
    def work(self):
        print("Robot working...")
    
    def eat(self):
        raise NotImplementedError("Robots don't eat!")
    
    def sleep(self):
        raise NotImplementedError("Robots don't sleep!")

# Usage
human = HumanWorker()
human.work()  # ✅ Works fine
human.eat()   # ✅ Works fine

robot = RobotWorker()
robot.work()  # ✅ Works fine
robot.eat()   # ❌ Throws NotImplementedError (Forced to implement unused methods)

"""

Issues:

RobotWorker is forced to implement eat() and sleep() even though they are irrelevant.

Violates ISP because RobotWorker depends on methods it doesn't use.

"""