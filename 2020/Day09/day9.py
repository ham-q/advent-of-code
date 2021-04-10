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

def FindContiguousSum(ErrorNumber, NumberList):
    pointer = 0
    while NumberList[pointer] < ErrorNumber:
        sumlist = [NumberList[pointer]]
        i = 1
        while sum(sumlist) <= ErrorNumber:
            if sum(sumlist) == ErrorNumber:
                return min(sumlist)+max(sumlist)
            else:
                sumlist.append(NumberList[pointer+i])
                i += 1
        pointer += 1

def Main():
    InputFile = ReadFile("2020/Day9/main_input.txt")
    MissingNo = CalculateMissingLink(InputFile, 25)
    print(FindContiguousSum(MissingNo, InputFile))

if __name__ == "__main__":
    Main()