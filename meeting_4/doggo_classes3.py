class Doggo:

    numOfDoggos = 0 # doggos counter - class attribute

    def __init__(self, name, age, breed):
        self.name = name    # instance attribute
        #self.__age = age    # private instance attribute
        self.set_age(age)   # setting using setter
        self.breed = breed    # instance attribute
        Doggo.numOfDoggos += 1

    def get_age(self):
        return self.__age
    
    def set_age(self, a):

        if a < 0:
            self.__age = -a
    def woof(self):
        print(f'{self.name}: - Woof! Woof!')


    def sniffOtherDog(self, otherDog):

        print(f'{self.name}: Sniff, sniff ...', end=' ')
        if otherDog.breed == self.breed:
            print('Woof! Woof! :))))')
        else:
            print('Grrr!!!!')


myDog1 = Doggo('Sparky', -1, 'golden')
myDog1.woof()

myDog2 = Doggo('Puszek', 3, 'chihuahua')
myDog2.woof()

myDog1.sniffOtherDog(myDog2)

print(myDog1.get_age())
