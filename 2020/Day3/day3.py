def ReadFile(FileName):
    MapList = []
    with open(FileName, "r") as MapData:
        for line in MapData:
            TempLine = list(line.rstrip())
            MapList.append(TempLine)
    return MapList

def GetHeightAndWidth(Map):
    return len(Map), len(Map[0])

def TracePath(Map,Right,Down):
    Height, Width = GetHeightAndWidth(Map)
    j = 0
    count = 0
    for i in range(0,Height,Down):
        while j >= Width:
            j -= Width
        if Map[i][j] == "#":
            count += 1
        j += Right
    return count

def MultiplyPathNums(Map):
    path1 = TracePath(Map, 1, 1)
    path2 = TracePath(Map, 3, 1)
    path3 = TracePath(Map, 5, 1)
    path4 = TracePath(Map, 7, 1)
    path5 = TracePath(Map, 1, 2)
    return path1 * path2 * path3 * path4 * path5


print(MultiplyPathNums(ReadFile("2020/Day3/main_input.txt")))