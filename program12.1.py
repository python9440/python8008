class animal:
    def sound(self):
        pass
class cat(animal):
    def sound(self):
        print("meow")
class dog(animal):
    def sound(self):
        print("woof")
def make_sound(animal):
    animal.sound()
cat=cat()
dog=dog()
make_sound(cat)
make_sound(dog)
