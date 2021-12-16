def ReadFile(FileName):
    with open(FileName,"r") as SeatData:
        SeatList = []
        for line in SeatData:
            templine = []
            templine += line.strip()
            SeatList.append(templine)
    return SeatList

def ApplyRules(Seat,SeatList):
    

def Main():
    print(ReadFile("2020/Day11/test_input.txt"))

if __name__ == "__main__":
    Main()