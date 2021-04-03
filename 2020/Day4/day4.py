def ReadFile(FileName):
    FieldTypes = []
    FieldData = []
    count = 0
    with open(FileName, "r") as PassportData:
        for line in PassportData:
            if line == "\n":
                count += VerifyData(FieldTypes,FieldData)
                FieldTypes.clear()
                FieldData.clear()
            else:
                FieldTypes += line.split()
                FieldData += line.split()
                for i in range(len(FieldTypes)-len(line.split()), len(FieldTypes)):
                    FieldTypes[i] = FieldTypes[i][0:3]
                    FieldData[i] = FieldData[i][4:]
        count += VerifyData(FieldTypes,FieldData)
        return count

def VerifyData(FieldTypes,FieldData):
    if all(x in FieldTypes for x in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]):
        if 1920 <= int(FieldData[FieldTypes.index("byr")]) and 2002 >= int(FieldData[FieldTypes.index("byr")]):
            if 2010 <= int(FieldData[FieldTypes.index("iyr")]) and 2020 >= int(FieldData[FieldTypes.index("iyr")]):
                if 2020 <= int(FieldData[FieldTypes.index("eyr")]) and 2030 >= int(FieldData[FieldTypes.index("eyr")]):
                    if FieldData[FieldTypes.index("hgt")][-2:] == "cm":
                        if 150 > int(FieldData[FieldTypes.index("hgt")][:-2]) or 193 < int(FieldData[FieldTypes.index("hgt")][:-2]):
                            return 0
                    elif FieldData[FieldTypes.index("hgt")][-2:] == "in":
                        if 59 > int(FieldData[FieldTypes.index("hgt")][:-2]) or 76 < int(FieldData[FieldTypes.index("hgt")][:-2]):
                            return 0
                    else:
                        return 0
                    if FieldData[FieldTypes.index("ecl")] in ["amb","blu","brn","gry","grn","hzl","oth"]:
                        try:
                            int(FieldData[FieldTypes.index("pid")])
                            if len(FieldData[FieldTypes.index("pid")]) == 9:
                                if FieldData[FieldTypes.index("hcl")][0] == "#" and (x in list(FieldData[FieldTypes.index("hcl")][1:]) for x in ["a","b","c","d","e","f","1","2","3","4","5","6","7","8","9"]) and len(FieldData[FieldTypes.index("hcl")][1:]) == 6:
                                    return 1
                        except:
                            return 0
    return 0

def Main():
    print(ReadFile("2020/Day4/main_input.txt"))

if __name__ == "__main__":
    Main()