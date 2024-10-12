bestPlayerNumber = 7

def setBestPlayerNumber(num = 0):
    BestPlayerNumber = num
    if(num == 7 or num == 28 or num == 9):
        global bestPlayerNumber
        bestPlayerNumber = num
    
setBestPlayerNumber()
print(bestPlayerNumber)
setBestPlayerNumber(9)
print(bestPlayerNumber)
setBestPlayerNumber(10) # messiiiiiiiii 🙂
print(bestPlayerNumber)