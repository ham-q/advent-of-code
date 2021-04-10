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

def FindAllLinks(Number, neighbours, Target):
    global LinkCount
    if Number == Target:
        LinkCount += 1
    else:
        for x in neighbours:
            if x[0] == Number:
                links = x[1]
        for item in links:
            FindAllLinks(item, neighbours, Target)

def SplitIntoNeighbours(JoltageList):
    NeighbourList = []
    for item in JoltageList:
        TempNeighbours = []
        if JoltageList[JoltageList.index(item)] == JoltageList[-1]:
            break
        i = 1
        while JoltageList[JoltageList.index(item)+i] - JoltageList[JoltageList.index(item)] < 4 and JoltageList[JoltageList.index(item)+i] - JoltageList[JoltageList.index(item)] > 0:
            TempNeighbours.append(JoltageList[JoltageList.index(item)+i])
            if JoltageList[JoltageList.index(item)+i] == JoltageList[-1]:
                break
            i += 1
        NeighbourList.append([JoltageList[JoltageList.index(item)],TempNeighbours])
    return NeighbourList

def CompressNeighbours(NeighbourList):
    complist = []
    templist = []
    maxnum = -1
    for item in NeighbourList:
        if item[0] == maxnum:
            if templist:
                complist.append(templist[:])
                templist.clear()
        elif len(item[1]) > 1 or item[0]<maxnum:
            if max(item[1]) > maxnum:
                maxnum = max(item[1])
                templist.append(item)
            else:
                templist.append(item)
    if templist:
        complist.append(templist[:])
        templist.clear()
    return complist

def Main():
    global LinkCount
    NList = SplitIntoNeighbours(ReadFile("2020/Day10/main_input.txt"))
    answer = 1
    for item in CompressNeighbours(NList):
        LinkCount = 0
        FindAllLinks(item[0][0], item, item[-1][1][0])
        answer = answer * LinkCount
    print(answer)

if __name__ == "__main__":
    LinkCount = 0
    Main()