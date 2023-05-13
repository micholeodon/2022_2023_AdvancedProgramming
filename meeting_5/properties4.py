# THE PROPER WAY :)

class Doggo:

    def __init__(self, name):
        self.__dogName = name # private attribute 
        self.__dogName = name # this is also ok, more often approach; 
        # double underscores rather used to avoid collisions during inheritance


    @property
    def dogName(self):
        return self.__dogName
    
    @dogName.setter
    def dogName(self, value):

        if isinstance(value, str):
            self.__dogName = value
        else:
            print('wrong type! property not changed')
    


dog1 = Doggo('Sparky')
dog2 = Doggo('Puszek')

print(dog1.dogName)

dog1.dogName = range(1,20)
print(dog1.dogName)