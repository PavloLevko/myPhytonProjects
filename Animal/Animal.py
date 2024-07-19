class Animal:
    name = ''
    health = 0
    speed = 0

    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed


class Dog(Animal):
    def __init__(self, name, health, speed):
        super(Dog, self).__init__(name, health, speed)


class Cat(Animal):
    def __init__(self, name, health, speed):
        super(Cat, self).__init__(name, health, speed)
