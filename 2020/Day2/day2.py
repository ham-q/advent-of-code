def ReadFile(FileName):
    DataList = []
    with open(FileName,"r") as InputFile:
        for line in InputFile:
            TempList = line.split()
            TempList[0] = TempList[0].split("-")
            TempList[1] = TempList[1][:-1]
            DataList.append(TempList)
    return DataList

def ValidatePasswordsOld(DataList):
    NoOfValid = 0
    for item in DataList:
        if int(item[0][0]) <= item[2].count(item[1]) and int(item[0][1]) >= item[2].count(item[1]):
            NoOfValid += 1
    return NoOfValid

def ValidatePasswordsNew(DataList):
    NoOfValid = 0
    for item in DataList:
        if (item[2][int(item[0][0])-1] == item[1]) ^ (item[2][int(item[0][1])-1] == item[1]):
            NoOfValid += 1
    return NoOfValid

print(ValidatePasswordsNew(ReadFile("2020/Day2/main_input.txt")))