class Fan:
    def __init__(self, speed = 1, radius = 5, color = "blue", on = False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = False

    def fanspeed(self, speed):
        if self.fanspeed == 1:
            return "Slow"
        elif self.fanspeed == 2:
            return "Medium"
        else:
            self.fanspeed == 3
            return "Fast"

    def fanradius(self, radius):
        self.radius = radius
        return self.radius

    def fancolor(self, color = "blue"):
        self.color = color
        return color

    def turnOn(self):
        self.on = True
        return "켜져있습니다."

    def turnOff(self):
        self.on = False
        return "꺼져있습니다."
