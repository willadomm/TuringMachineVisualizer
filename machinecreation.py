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

    
    
    string = correctalphabetchecker(tapealphabet)
    

   
    
    turingmachine.TuringMachine(listofstates,inputalphabet,tapealphabet,listoftransitions,"q0","q1",None, string)


def ancnbn():

    listoftransitions = []
    listofstates = {"s, q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "t", "r"}
    tapealphabet = ["a", "b", "c"]
    inputalphabet = ["|-", "-|", "_"]

    inputalphabet = inputalphabet.extend(tapealphabet)


  

    # State s
    listoftransitions.append(("s", "|-", "s", "|-", "R"))
    listoftransitions.append(("s", "a", "s", "a", "R"))
    listoftransitions.append(("s", "b", "q1", "b", "R"))
    listoftransitions.append(("s", "c", "q2", "c", "R"))
    listoftransitions.append(("s", "_", "q3", "-|", "L"))

    # State q1
    listoftransitions.append(("q1", "a", "r", "a", None))
    listoftransitions.append(("q1", "b", "q1", "b", "R"))
    listoftransitions.append(("q1", "c", "q2", "c", "R"))
    listoftransitions.append(("q1", "_", "q3", "-|", "L"))

    # State q2
    listoftransitions.append(("q2", "a", "r", "a", None))
    listoftransitions.append(("q2", "b", "r", "b", None))
    listoftransitions.append(("q2", "c", "q2", "c", "R"))
    listoftransitions.append(("q2", "_", "q3", "-|", "L"))

    # State q3
    listoftransitions.append(("q3", "|-", "t", "|-", None))
    listoftransitions.append(("q3", "a", "r", "a", None))
    listoftransitions.append(("q3", "b", "r", "b", None))
    listoftransitions.append(("q3", "c", "q4", "_", "L"))
    listoftransitions.append(("q3", "_", "q3", "_", "L"))

    # State q4
    listoftransitions.append(("q4", "|-", "r", "|-", None))
    listoftransitions.append(("q4", "a", "r", "a", None))
    listoftransitions.append(("q4", "b", "q5", "_", "L"))
    listoftransitions.append(("q4", "c", "q4", "c", "L"))
    listoftransitions.append(("q4", "_", "q4", "_", "L"))

    # State q5
    listoftransitions.append(("q5", "|-", "r", "|-", None))
    listoftransitions.append(("q5", "a", "q6", "_", "L"))
    listoftransitions.append(("q5", "b", "q5", "b", "L"))
    listoftransitions.append(("q5", "_", "q5", "_", "L"))

    # State q6
    listoftransitions.append(("q6", "|-", "q7", "|-", "R"))
    listoftransitions.append(("q6", "a", "q6", "a", "L"))
    listoftransitions.append(("q6", "_", "q6", "_", "L"))

    # State q7
    listoftransitions.append(("q7", "a", "q8", "_", "R"))
    listoftransitions.append(("q7", "b", "r", "b", None))
    listoftransitions.append(("q7", "c", "r", "c", None))
    listoftransitions.append(("q7", "_", "q7", "_", "R"))
    listoftransitions.append(("q7", "-|", "t", "-|", None))

    # State q8
    listoftransitions.append(("q8", "a", "q8", "a", "R"))
    listoftransitions.append(("q8", "b", "q9", "_", "R"))
    listoftransitions.append(("q8", "c", "r", "c", None))
    listoftransitions.append(("q8", "_", "q8", "_", "R"))
    listoftransitions.append(("q8", "-|", "r", "-|", None))

    # State q9
    listoftransitions.append(("q9", "b", "q9", "b", "R"))
    listoftransitions.append(("q9", "c", "q10", "_", "R"))
    listoftransitions.append(("q9", "_", "q9", "_", "R"))
    listoftransitions.append(("q9", "-|", "r", "-|", None))

    # State q10
    listoftransitions.append(("q10", "c", "q10", "c", "R"))
    listoftransitions.append(("q10", "_", "q10", "_", "R"))
    listoftransitions.append(("q10", "-|", "q3", "-|", "L"))

    correctstring = False

    while (correctstring == False):

        string = correctalphabetchecker(tapealphabet)

        correctstring = True
        bboolean = False
        cboolean = False


        for character in string:
            if character == "b":
                bboolean = True
            elif character == "c":
                cboolean = True
            elif character == "a" and (bboolean == True or cboolean == True):
                print("String must be of form a\u207fb\u207fc\u207f.")
                correctstring = False
                break
            elif character == "b" and cboolean == True:
                print("String must be of form a\u207fb\u207fc\u207f.")
                correctstring = False
                break
        
            

    turingmachine.TuringMachine(listofstates,inputalphabet,tapealphabet,listoftransitions,"s","t","r", string)


def apowerof2():
    listoftransitions = []
    listofstates = {"s, q10", "q2", "q1", "q11", "q4", "q5", "q6", "q12", "q8", "q9", "t", "r"}
    tapealphabet = ["a"]
    inputalphabet = ["|-", "-|", "_", "x"]

    inputalphabet = inputalphabet.extend(tapealphabet)

    # State s
    listoftransitions.append(("s", "|-", "s", "|-", "R"))
    listoftransitions.append(("s", "a", "q10", "a", "R"))
    listoftransitions.append(("s", "_", "r", "_", None))

    # State q10
    listoftransitions.append(("q10", "a", "q2", "a", "R"))
    listoftransitions.append(("q10", "x", "q10", "x", "R"))
    listoftransitions.append(("q10", "_", "t", "_", None))
    listoftransitions.append(("q10", "-|", "t", "-|", None))

    # State q2
    listoftransitions.append(("q2", "a", "q1", "a", "R"))
    listoftransitions.append(("q2", "_", "q3", "-|", "L"))

    # State q1
    listoftransitions.append(("q1", "a", "q2", "a", "R"))
    listoftransitions.append(("q1", "_", "r", "_", None))

    # State q3
    listoftransitions.append(("q3", "|-", "r", "|-", None))
    listoftransitions.append(("q3", "a", "q11", "x", "L"))
    listoftransitions.append(("q3", "x", "q3", "x", "L"))

    # State q11
    listoftransitions.append(("q11", "a", "q4", "a", "L"))
    listoftransitions.append(("q11", "x", "q11", "x", "L"))
    listoftransitions.append(("q11", "|-", "t", "|-", None))

    # State q4
    listoftransitions.append(("q4", "|-", "q6", "|-", "R"))
    listoftransitions.append(("q4", "a", "q5", "a", "L"))
    listoftransitions.append(("q4", "x", "q4", "x", "L"))

    # State q5
    listoftransitions.append(("q5", "|-", "r", "|-", None))
    listoftransitions.append(("q5", "a", "q4", "x", "L"))
    listoftransitions.append(("q5", "x", "q5", "x", "L"))

    # State q6
    listoftransitions.append(("q6", "a", "q12", "x", "R"))
    listoftransitions.append(("q6", "x", "q6", "x", "R"))
    listoftransitions.append(("q6", "-|", "r", "-|", None))

    # State q12
    listoftransitions.append(("q12", "a", "q8", "a", "R"))
    listoftransitions.append(("q12", "x", "q12", "x", "R"))
    listoftransitions.append(("q12", "-|", "t", "-|", None))

    # State q8
    listoftransitions.append(("q8", "a", "q9", "x", "R"))
    listoftransitions.append(("q8", "x", "q8", "x", "R"))
    listoftransitions.append(("q8", "-|", "q3", "-|", "L"))

    # State q9
    listoftransitions.append(("q9", "a", "q8", "a", "R"))
    listoftransitions.append(("q9", "x", "q9", "x", "R"))
    listoftransitions.append(("q9", "-|", "r", "-|", None))

    string = correctalphabetchecker(tapealphabet)

    turingmachine.TuringMachine(listofstates, inputalphabet, tapealphabet, listoftransitions, "s", "t", "r", string)

    