def ReadFile(FileName):
    TempData = []
    count = 0
    with open(FileName, "r") as PassportData:
        for line in PassportData:
            if line == "\n":
                if all(x in TempData for x in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]):
                    count += 1
                TempData.clear()
            else:
                TempData += line.split()
                for i in range(len(TempData)):
                    TempData[i] = TempData[i][0:3]
        if all(x in TempData for x in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]):
            count += 1
        return count

def Main():
    print(ReadFile("2020/Day4/main_input.txt"))

if __name__ == "__main__":
    Main()