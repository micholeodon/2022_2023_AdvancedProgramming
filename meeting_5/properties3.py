class Doggo:

    def __init__(self, name):
        self.__dogName = name # this is private with actual access constraint
        # by actually changing property to _ClassName__dogName


    def get_dogName(self):
       pass # some code to check access

   def set_dogName(self, value):
       pass # some code to check new value

   
dog1 = Doggo('Sparky')
dog2 = Doggo('Puszek')

# print(dog1._dogName) # produce error
print(dog1._Doggo__dogName) # will NOT produce error but is show that sb want to break into private stuff
