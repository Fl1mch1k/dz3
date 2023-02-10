import random


class animal:


    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.alive = True
        self.satiety = 10






    def to_walk(self):
        print("Time to walk!")
        self.gladness += 10
        self.satiety -= 2


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.satiety -= 1


    def to_eat(self):
        print("I am eating")
        self.satiety += 10





    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Satiety = {self.satiety}")


    def live(self, day):
        day = "Day " + str(day) + " Of " + self.name + " Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_walk()
        self.end_of_day()



nick = animal(name="Dog")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
