import turingmachine
import machinecreation

def main():
    
    print("Welcome to the Turing Machine Visualizer. Enter the corresponding number to visualize that TM.")
    print("1. L = any string in the alphabet (0, 1)\u02df that contains at least one 1. ")
    print("2. L = any string of the form a\u207fb\u207fc\u207f.")
    print("3. L = a repeated a power of two times.")
    
    
    choiceint = " "
    choicerange = ["1", "2", "3"]

    while not choiceint.isnumeric() or choiceint not in choicerange:
        choiceint = input("Type Here: ")
        if choiceint.isnumeric == False or choiceint not in choicerange:
            print("Please enter a valid number")

    match choiceint:
        case "1":
            machinecreation.one1machine()
        case "2":
            machinecreation.ancnbn()
        case "3":
            machinecreation.apowerof2()
    



main()