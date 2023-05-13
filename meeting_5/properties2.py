class Doggo:

    def __init__(self, name):
        self._dogName = name # changed this to private but will not restrict access, only signifies intention

   def get_dogName(self):
       pass # some code to check access

   def set_dogName(self, value):
       pass # some code to check new value

dog1 = Doggo('Sparky')
dog2 = Doggo('Puszek')

print(dog1._dogName)

dog1._dogName = range(1,10) # still not so safe but at least explicitly reveals malicious intentions ^^
