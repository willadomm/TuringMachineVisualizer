import turingmachine


def main():
    listoftransitions = [] 
    listofstates = ["q0", "q1"]
    inputalphabet = ["0", "1"]
    tapealphabet = ["0", "1"]

    listoftransitions.append(["q0", "0", "q0", "0", "R"])
    listoftransitions.append(["q0","1", "q1", "1", "R"])
    turingmachine.TuringMachine(listofstates,inputalphabet,tapealphabet,listoftransitions,"q0","q1",None, "0011")


main()