class Doggo:

    numOfDoggos = 0 # doggos counter - class attribute

    def __init__(self, name, age, breed):
        self.name = name    # instance attribute
        self.age = age      # instance attribute
        self.breed = breed    # instance attribute
        Doggo.numOfDoggos += 1

    def woof(self):
        print(f'{self.name}: - Woof! Woof!')


myDog1 = Doggo('Sparky', 1, 'golden')
myDog1.woof()

myDog2 = Doggo(name='Puszek', age=3, breed='chihuahua')
myDog2.woof()

print(Doggo.numOfDoggos)
print(myDog1.numOfDoggos)
print(myDog2.numOfDoggos)
print(Doggo.name) # throws an error - there is no class attribute such name 
