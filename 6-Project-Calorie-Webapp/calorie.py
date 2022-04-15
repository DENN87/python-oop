class Calorie:
    """
    Represents amount of calories
    BMR = 10*weight + 6.25*height - 5*age - 10*temp
    """
    def __init__(self, weight, height, age, temp):
        self.weight = weight
        self.height = height
        self.age = age
        self.temp = temp

    def calculate(self):
        pass
