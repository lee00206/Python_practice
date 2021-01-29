class BMI:
    def __init__(self, weight = 1, height = 1):
        self.weight = weight
        self.height = height

    def poundTokg(self):
        return self.weight*0.45359237

    def inchTom(self):
        return self.height*0.0254

    def getBMI(self):
        return self.poundTokg()/(self.inchTom()**2)

    def BMIvalue(self):
        if self.getBMI() >= 30.0:
            return "비만"
        elif self.getBMI() >= 25.0:
            return "과체중"
        elif self.getBMI() >= 18.5:
            return "정상"
        else:
            self.getBMI() < 18.5
            return "저체중"

