def ReadFile(FileName):
    with open(FileName,"r") as JoltageData:
        JoltageList = []
        for line in JoltageData:
            JoltageList.append(int(line.strip()))
    JoltageList.insert(0,0)
    return sorted(JoltageList)

def ThreeAndOneProduct(JoltageList):
    ThreeCount = 0
    OneCount = 0
    for i in range(len(JoltageList)-1):
        difference = FindDifference(JoltageList[i],JoltageList[i+1])
        if difference == 3:
            ThreeCount += 1
        elif difference == 1:
            OneCount += 1
    return (ThreeCount+1)*OneCount

def FindDifference(Number1, Number2):
    return Number2 - Number1

def Main():
    print(ThreeAndOneProduct(ReadFile("2020/Day10/main_input.txt")))

if __name__ == "__main__":
    Main()