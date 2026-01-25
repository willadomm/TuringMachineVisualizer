import time

class TuringMachine:
    def __init__(self, states, inputalphabet, tapealphabet, transitions, startstate, endstate, rejectstate, startingstring):
        self.states = states
        self.inputalphabet = inputalphabet
        self.tapealphabet = tapealphabet
        self.transitions = transitions
        self.transdictobj = {}
        self.startstate = startstate
        self.endstate = endstate
        self.rejectstate = rejectstate
        self.startingstring = startingstring
        self.blanksymbol = '_'
        self.leftend = '|-'
        self.currentstate = self.startstate
        self.headlocation = 1
        self.tape = []
        self.transitionsdict()
        self.createtape()
        self.mainloop()
    
    def tapedisplay(self):
        printable = ""
        sizeoftape = 0
        for character in self.tape:
            if character != '_':
                printable += character
                sizeoftape += 1
        ontopprintstring = " " * (self.headlocation + 1)+ "^" + " " * (sizeoftape -self.headlocation)
        print(printable + "\n" + ontopprintstring)

    
    def createtape(self):
        blanktape = [0]*1000
        blanktape[0] = self.leftend
        blanktape[1:1000] = self.blanksymbol * 999
        tapecounter = 1
        for character in self.startingstring:
            blanktape[tapecounter] = character
            tapecounter += 1
        self.tape = blanktape

        print("Initial Tape: ")
        self.tapedisplay()

        print("Enter a C instead of enter at any time to end the visualizer. (Very useful if the machine is not total)")

        time.sleep(2)
        

    def transitionsdict(self):
        for transition in self.transitions:
            self.transdictobj[tuple(transition[0:2])] = tuple(transition[2:])
    
    def mainloop(self):
        
        print("Tape:")
        print()
        time.sleep(0.5)
        self.tapedisplay()

        print("Current state: " + self.currentstate)
        print("Current character: " + self.tape[self.headlocation])

        time.sleep(0.5)
        print()

        transition = (self.currentstate, self.tape[self.headlocation])

        print("Changing to state " + self.transdictobj[transition][0])
        print("Writing " + self.transdictobj[transition][1])
        print("Moving R/W head to the " + self.transdictobj[transition][2])

        self.currentstate = self.transdictobj[transition][0]
        self.tape[self.headlocation] = self.transdictobj[transition][1]
        if (self.transdictobj[transition][2] == "R"):
            self.headlocation += 1
        elif (self.transdictobj[transition][2] == "L"):
            self.headlocation = self.headlocation - 1
        
        print()
        
        if(self.currentstate == self.endstate):
            print("End Reached!")
            print("Final Tape: ")
            self.tapedisplay()
            exit()


        timecontrol = input("Press enter to see the next step. ")
        print()
        self.mainloop()

        
        



