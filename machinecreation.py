import turingmachine


def correctalphabetchecker(tapealphabet):
    properstring = False
    while properstring == False:
        stringinput = input("Please enter the string to be determined by the machine: ")
        properstring = True
        for char in stringinput:
            if char not in tapealphabet:
                properstring = False
                print("Please enter a string in the alphabet of the machine")

    return stringinput


def one1machine():

    listoftransitions = [] 
    listofstates = ["q0", "q1"]
    inputalphabet = ["0", "1"]
    tapealphabet = ["0", "1"]

    listoftransitions.append(["q0", "0", "q0", "0", "R"])
    listoftransitions.append(["q0","1", "q1", "1", "R"])
    listoftransitions.append(["q0", "_", "q0", "0", "R"])

    
    
    string = correctalphabetchecker(inputalphabet)
    

   
    
    turingmachine.TuringMachine(listofstates,inputalphabet,tapealphabet,listoftransitions,"q0","q1",None, string)