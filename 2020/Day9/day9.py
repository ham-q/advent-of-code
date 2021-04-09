def ReadFile(FileName):
    with open(FileName) as EncryptedData:
        NumberList = []
        for line in EncryptedData:
            NumberList.append(int(line.strip()))
    return NumberList

def CalculateMissingLink(NumberList, PreambleLength):
    pointer = PreambleLength - 1
    NumberFound = False
    while not NumberFound:
        NumberFound = CheckIfNotSum(pointer, NumberList[pointer+1], NumberList, PreambleLength)
        pointer += 1
    return NumberList[pointer]

def CheckIfNotSum(pointer, currentNumber, NumberList, PreambleLength):
    for i in range(PreambleLength):
        for j in range(PreambleLength):
            if i == j:
                continue
            if NumberList[pointer-i] + NumberList[pointer-j] == currentNumber:
                return False
    return True

def Main():
    print(CalculateMissingLink(ReadFile("2020/Day9/main_input.txt"), 25))

if __name__ == "__main__":
    Main()