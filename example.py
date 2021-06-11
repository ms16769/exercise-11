def myfunc(values, value, next):
    """
        This function will search an item in a list of values and return the neighbouring value -- either the successor or the predecessor.
    """
    # First: find the position of value
    i = -1
    for j in range(len(values)):
        index = values[j] # values[j] is define the index of value 
        if index == value:
            i = j
    # If next == True get the successor
    if next:
        if i < len(values) - 1:
            successor = i + 1 # Value is successor or not
            return values[successor]
    
    else:
        if i > 0:
            predecessor = i - 1 # Value is predecessor or not
            return values[predecessor]
