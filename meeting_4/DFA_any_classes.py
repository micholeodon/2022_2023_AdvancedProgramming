#%% classes

class DFA:

    
    def __init__(self, M):

        # extract elements
        self.Q = M[0]   # states indices
        self.S = M[1]   # alphabet
        self.d = M[2]   # transition function 
        self.q0 = M[3]  # start state
        self.F = M[4]   # set of accept states

        DFA.__validate(self)

    def __init__(self, Q, S, d, q0, F):

        # extract elements
        self.Q = Q    # states indices
        self.S = S    # alphabet
        self.d = d    # transition function 
        self.q0 = q0  # start state
        self.F = F    # set of accept states

        DFA.__validate(self)


    def __validate(self):
        ''' Private function that validate whether the input to the constructor is valid '''
        ''' See: https://www.geeksforgeeks.org/private-methods-in-python/ '''

        print('Called a private function!')
        pass # to be implemented later (skip in illustration)


    
    def processWord(self, inputWord):

        # extract elements
        Q = self.Q
        S = self.S
        d = self.d
        q0 = self.q0
        F = self.F

        currentState = q0

        for letter in inputWord:
            print(f'letter: {letter} | state: {currentState}')

            if letter not in S:
                return "REJECT"
        
            currentState = d[letter][currentState]
            print(f'Moved to state: {currentState}')

        # after processing all input letters
        if currentState in F:
            return "ACCEPT"
    
        return "REJECT"



#%% TEST

# create DFA

myDfa1 = DFA(
    Q = {0, 1 , 2},
    S = {'a', 'b'},
    d = {'a':(1,2,2), 'b':(0,0,2)},
    q0 = 0,
    F = {0})
# this automaton accepts words where each 'a' is followed immediately by 'b'


myDfa2 = DFA(
    Q = {0, 1},
    S = {'a', 'b'},
    d = {'a':(1,1), 'b':(0,0)},
    q0 = 0,
    F = {1})
# this automaton accepts words ending with 'a'


decision = 1

while decision:

    word = input('Give input word containing only letters a or b: \n')
    result = myDfa2.processWord(word)
    print(result)
    decision = int(input('Try again? (1 - yes, 0 - no) : '))

print('It was fun! Bye!')

