def ReadFile(filename):
    """Used to read in input data and format it correctly
    Input: STR - directory for file to be used
    Outputs: 2x LIST (all STR elements) - lists with each direction as an element"""
    i = 0
    with open(filename, "r") as direction_file:
        for line in direction_file:
            if i == 0:
                wire1_directions = line.split(",")
            else:
                wire2_directions = line.split(",")
            i+=1
    return wire1_directions, wire2_directions

def RecordMovements(directions):
    """Used to build a list with all wire locations on grid
    Input: LIST (all STR elements) - list with directions which are iterated upon
    Outputs: LIST (all STR elements) - list with all locations visited in form x,y"""
    path_list = ["0,0"]
    for direction in directions:
        if direction[:1] == "U":
            for i in range(int(direction[1:])):
                temp_list = list(map(int, path_list[len(path_list)-1].split(",")))
                new_position = str(temp_list[0]) + "," + str(temp_list[1]+1)
                path_list.append(new_position)
        if direction[:1] == "D":
            for i in range(int(direction[1:])):
                temp_list = list(map(int, path_list[len(path_list)-1].split(",")))
                new_position = str(temp_list[0]) + "," + str(temp_list[1]-1)
                path_list.append(new_position)
        if direction[:1] == "L":
            for i in range(int(direction[1:])):
                temp_list = list(map(int, path_list[len(path_list)-1].split(",")))
                new_position = str(temp_list[0]-1) + "," + str(temp_list[1])
                path_list.append(new_position)
        if direction[:1] == "R":
            for i in range(int(direction[1:])):
                temp_list = list(map(int, path_list[len(path_list)-1].split(",")))
                new_position = str(temp_list[0]+1) + "," + str(temp_list[1])
                path_list.append(new_position)
    del path_list[0] #removes 0,0 since it won't be counted as intersection
    return path_list

def find_matching_indices(a, b):
    res = [] 
    i = 0
    while (i < len(a)): 
        if (b.count(a[i]) > 0): 
            res.append(i) 
        i += 1
        print(i, "/", len(a))
    return res

def CheckIntersection(wire1_dir_list, wire2_dir_list):
    """Used to check items in both lists and return where they intersect
    Input: 2xLIST (all STR elements) - list with all locations visited in form x,y for both wires
    Outputs: SET (all STR elements) - set of intersections"""
    wire_lengths = list(find_matching_indices(wire1_dir_list, wire2_dir_list))
    return set(wire1_dir_list).intersection(wire2_dir_list), wire_lengths

def GetIntersectionLengths(intersection_list, lengths):
    """Used to find minimum distance in Manhattan Distance, 
    Input: Set (all STR elements) - set of intersections
    Outputs: INT - the minimum distance of an intersection from centre"""
    length_list = []
    for position in intersection_list:
        temp_list = position.split(",")
        temp_list = map(abs,map(int, temp_list))
        length_list.append(sum(temp_list))
    return_string = str(min(length_list)), str(min(lengths))
    return return_string

def Main():
    wire1_directions, wire2_directions = ReadFile("Day3/input.txt")
    wire1_dir_list, wire2_dir_list = RecordMovements(wire1_directions), RecordMovements(wire2_directions)
    intersections, wirelength = CheckIntersection(wire1_dir_list, wire2_dir_list)
    print(GetIntersectionLengths(intersections, wirelength))


if __name__ == "__main__":
  Main()