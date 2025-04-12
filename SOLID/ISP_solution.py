from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working...")
    
    def eat(self):
        print("Human eating...")
    
    def sleep(self):
        print("Human sleeping...")

class RobotWorker(Workable):
    def work(self):
        print("Robot working...")

# Usage
human = HumanWorker()
human.work()  # ✅ Works
human.eat()   # ✅ Works
human.sleep() # ✅ Works

robot = RobotWorker()
robot.work()  # ✅ Works
# robot.eat() → ❌ Not available (No forced dependency)

"""

Benefits:

     RobotWorker only implements Workable (no unnecessary methods).

     HumanWorker implements all relevant interfaces (Workable, Eatable, Sleepable).

     Follows ISP because clients depend only on the interfaces they need.

"""