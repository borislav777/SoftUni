from project.animal import Animal


class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age}" \
               f" year old {self.gender} {type(self).__name__}"
