import turingmachine
import machinecreation

def main():
    
    print("Welcome to the Turing Machine Visualizer. Enter the corresponding number to visualize that TM.")
    print("1. L = any string in the alphabet (0, 1)\u02df that contains at least one 1. ")
    
    
    choiceint = " "

    while not choiceint.isnumeric() or choiceint != "1":
        choiceint = input("Type Here: ")
        if choiceint.isnumeric == False or choiceint != "1":
            print("Please enter a valid number")

    match choiceint:
        case "1":
            machinecreation.one1machine()
    



main()