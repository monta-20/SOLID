from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on")
    
    def turn_off(self):
        print("LightBulb: turned off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on")
    
    def turn_off(self):
        print("Fan: turned off")

class ElectricPowerSwitch:
    def __init__(self, device: Switchable):
        self.device = device
        self.on = False
    
    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True

# Usage
bulb = LightBulb()
switch_for_bulb = ElectricPowerSwitch(bulb)
switch_for_bulb.press()  # Turns on bulb
switch_for_bulb.press()  # Turns off bulb

fan = Fan()
switch_for_fan = ElectricPowerSwitch(fan)
switch_for_fan.press()  # Turns on fan
switch_for_fan.press()  # Turns off fan

"""

Benefits:

     ElectricPowerSwitch now depends on the abstraction (Switchable), not concrete classes.

     New devices (e.g., Fan) can be added without modifying ElectricPowerSwitch.

     Loose coupling makes the system more flexible.



"""