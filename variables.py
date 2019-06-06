class Dog:
    age_born = 1

    def __init__(self, age=0, nubmer_of_feet=4):
        self.age = age
        self.nubmer_of_feet = nubmer_of_feet


doggy = Dog()
print(doggy.age)
doggy.age += 1
print(str(doggy.age) + '\n')
print(doggy.age_born)
doggy.age_born += 1
print(doggy.age_born)
