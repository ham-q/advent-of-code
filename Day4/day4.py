def CheckValid(code):
    """Used to validate codes
    Input: STR - since you can compare characters in strings
    Output: INT (0,1) - will update counter if valid"""
    doubles = 0
    for i in range(5):
        if code[i] == code[i+1]:
            try:
                if code[i] == code[i+2] or code[i] == code[i-1]:
                    pass
                else:
                    doubles += 1
            except:
                if code[i] == code[i-1]:
                    pass
                else:
                    doubles += 1
    if doubles > 0:
        for j in range(5):
            if int(code[j])>int(code[j+1]):
                return 0
        return 1    
    return 0

def CodesToCheck(start, end):
    """Iterates through codes within given range
    Input: 2xINT - used to specify start and end codes
    Output: INT - the number of valid codes found"""
    count = 0
    for i in range(start, end):
        count += CheckValid(str(i))
    return count

def Main():
    print(CodesToCheck(158126,624574))

if __name__ == "__main__":
  Main()