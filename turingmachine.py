class TuringMachine:
    def __init__(self, states, inputalphabet, tapealphabet, transitions, startstate, endstate, rejectstate, string):
        self.states = states
        self.inputalphabet = inputalphabet
        self.tapealphabet = tapealphabet
        self.transitions = transitions
        self.startstate = startstate
        self.endstate = endstate
        self.rejectstate = rejectstate
        self.string = string
        self.blanksymbol = '_'
        self.leftend = '|-'
        self.rightend = '-|'
        self.currentstate = self.startstate
        self.headlocation = 0
        self.tape = []
        self.createtape()
    
    def primitiveprint(self):
        printable = ""
        for character in self.tape:
            if character != '_':
                printable += character
        print(printable)

    
    def createtape(self):
        blanktape = [0]*1000
        blanktape[0] = self.leftend
        blanktape[1:1000] = self.blanksymbol * 999
        tapecounter = 1
        for character in self.string:
            blanktape[tapecounter] = character
            tapecounter += 1
        self.tape = blanktape

        self.primitiveprint()



