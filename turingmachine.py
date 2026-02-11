import time
import json

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
        self.timecontrol = "N"
        self.fastfowardint = None
        self.transitionsdict()
        self.createtape()
        self.mainloop()

    
    def tapedisplay(self):
        printable = ""
        for character in self.tape:
                printable += character
        printable = printable[::-1]

        while (printable[0] == "_"):
            printable = printable[1:]

        printable = printable[::-1]
        
        ontopprintstring = " " * (self.headlocation + 1)+ "^" + " " * (len(printable) -self.headlocation)
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

        print()

        print("Initial Tape: ")
        self.tapedisplay()

        time.sleep(1)

        print("Enter a C instead of enter at any time to end the visualizer. (Very useful if the machine is not total)")
        print("Enter 'ff x' to fast forward through x transitions. ")
        print("Enter ff to skip to the end (Be careful when using a non-total TM!)")

        userinput = input("Press enter to begin: ")

        if "ff" in userinput:
            self.timecontrol = "ff"
        if " " in userinput:
            if userinput.split()[1].isnumeric():
                self.fastfowardint = int(userinput.split()[1])
            



       
        

    def transitionsdict(self):
        for transition in self.transitions:
            self.transdictobj[tuple(transition[0:2])] = tuple(transition[2:])
    
    def mainloop(self):
        
        print("Tape:")
        print()
        if (self.timecontrol != "ff"):
            time.sleep(0.5)
        self.tapedisplay()

        print("Current state: " + self.currentstate)
        print("Current character: " + self.tape[self.headlocation])

        if (self.timecontrol != "ff"):
            time.sleep(0.5)
        print()

        transition = (self.currentstate, self.tape[self.headlocation])

        print("Changing to state " + self.transdictobj[transition][0])
        print("Writing " + self.transdictobj[transition][1])
        if (self.transdictobj[transition][2] != None):
            print("Moving R/W head to the " + self.transdictobj[transition][2])

        self.currentstate = self.transdictobj[transition][0]
        self.tape[self.headlocation] = self.transdictobj[transition][1]
        if (self.transdictobj[transition][2] == "R"):
            self.headlocation += 1
        elif (self.transdictobj[transition][2] == "L"):
            self.headlocation = self.headlocation - 1
        elif (self.transdictobj[transition][2] == None):
            self.headlocation = self.headlocation
        
        print()

        if(self.currentstate == self.endstate):
            print("Acceptance state reached.")
            print("Your string is in the language!")
            print("Final Tape: ")
            self.tapedisplay()
            exit()
        
        if(self.currentstate == self.rejectstate):
            print("Rejection state reached.")
            print("Your string is not in the language.")
            print("Final Tape: ")
            self.tapedisplay()
            exit()


        if (self.headlocation == len(self.tape) -1):
            newblankarray = ["_"] * len(self.tape)
            self.tape.extend(newblankarray)

        if isinstance(self.fastfowardint, int):
            if self.fastfowardint > 0:
                self.fastfowardint = self.fastfowardint - 1
            if self.fastfowardint == 0:
                self.timecontrol = "N"
                self.fastfowardint = None

        
        
        if self.timecontrol != "ff":
            self.timecontrol = input("Press enter to see the next step. ")
        
        if self.timecontrol == "C":
            print("Halted by user.")
            exit()

        elif " " in self.timecontrol:
            if self.timecontrol.split()[1].isnumeric():
                self.fastfowardint = int(self.timecontrol.split()[1])
                self.timecontrol = "ff"
        
        elif "ff" in self.timecontrol:
            self.timecontrol = "ff"
            
        
        print()
        self.mainloop()

        
        



