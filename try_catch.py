try :
    y = Exception.__cause__() # error
    print("fuck")
except Exception as x:
    print("Oh no!\n\t", x.args[0])