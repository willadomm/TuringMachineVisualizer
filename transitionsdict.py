def transitionsdict(listoftransitions):
    transdict = {}
    for transition in listoftransitions:
        transdict[tuple(transition[0:2])] = tuple(transition[2:])
    
    
