"""
Exercise 1: Dog and Owner
Create two classes:
Dog with:

Attributes: name, breed
A method bark() that prints something like "Rex says: Woof!"

Owner with:

Attributes: owner_name, dog (this should be a Dog object)
A method introduce_pet() that prints something like "Hi, I'm Alice and my dog is Rex!"
A method make_dog_bark() that calls the dog's bark() method through the owner object

Then create an Owner object (passing in a Dog object) and call both methods on it.
"""

class Dog():
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 

    def bark(self):
        print(f"{self.name} just barked!!")

class Owner():
    def __init__(self, owner_name, dog):
        self.name = owner_name 
        self.dog = dog  # Here dog is an already initialized object
        # But is it better to keep it as Dog(dog_name, breed) instead ? The init has to take dog name and breed as input then ?  NO
        # I feel giving the object directly is better because when creating an owner object, the dog has to already exist ???
        # In future, we can change the dog of the owner by just doing owner.dog = new_dog_object

    def introduce_pet(self):
        print(f"Meet my dog {self.dog.name}, belongs to breed {self.dog.breed}")

    def make_dog_bark(self):
        return self.dog.bark()


dog = Dog("Tommy", "Husky")
owner = Owner("James", dog)

owner.introduce_pet()
owner.make_dog_bark()