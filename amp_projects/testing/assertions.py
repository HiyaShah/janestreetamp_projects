#assert keyword - returns None if truthy, AssertionError if falsy
#accepts optional error message as a second message

def add_positive_num(x,y):
    assert x>0 and y>0, "both num must be positive" #error message if assertion statement is falsy
    return x+y
#if a python file is run with -O flag (optimize mode) assertions will be ignored
#python3 -O assertions.py