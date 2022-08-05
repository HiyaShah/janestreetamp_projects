#write tests for func inside docstring
#write code like it's inside a repl

def add(a, b):
    """
    >>> add(2,3)
    5

    >>> add(100,200)
    300
    
    """
    return a+b

def double(values):
    """ doubles the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []
    >>> double(['a','b','c','d'])
    ['aa', 'bb', 'cc', 'dd']

    
    """
    return [x*2 for x in values] 

#issues
# strange syntax
