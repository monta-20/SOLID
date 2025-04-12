class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on")
    
    def turn_off(self):
        print("LightBulb: turned off")

class ElectricPowerSwitch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb
        self.on = False
    
    def press(self):
        if self.on:
            self.bulb.turn_off()
            self.on = False
        else:
            self.bulb.turn_on()
            self.on = True

# Usage
bulb = LightBulb()
switch = ElectricPowerSwitch(bulb)
switch.press()  # Turns on
switch.press()  # Turns off


"""

Issues:

     ElectricPowerSwitch (high-level) directly depends on LightBulb (low-level).

     If we want to control a Fan instead, we must modify ElectricPowerSwitch.

"""