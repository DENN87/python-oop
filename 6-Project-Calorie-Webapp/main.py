from calorie import Calorie
from temperature import Temperature

if __name__ == "__main__":
    temp = Temperature("usa", "antioch").get()
    calories = Calorie(161*0.45359237, 5*30.48 + 6*2.54, 34, temp)
    print(calories.calculate())


