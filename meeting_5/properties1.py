class Doggo:

    def __init__(self, name):
        self.dogName = name



dog1 = Doggo('Sparky')
dog2 = Doggo('Puszek')

print(dog1.dogName)

dog1.dogName = range(1,10) # having public instancep properties is not safe