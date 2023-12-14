from copy import deepcopy

class TwoDimensionalList:
    data = []

    def __init__(self, x) -> None:
        self.data = x

    def _transposed(self, l):
        return [list(x) for x in zip(*l)]

    def _find_reflect(self, l, ignore = -1):
        seen = []
        for i in range(len(l)):
            if l[i] == seen:
                perfect_reflection = True
                for j in range(1,i):
                    if i+j < len(l):
                        if l[i+j] != l[i-j-1]:
                            perfect_reflection = False
                if perfect_reflection and i != ignore:
                    return i
            seen = l[i]
        return -1

    def reflect(self, ignore=False):
        rows = self._find_reflect(self.data)
        if ignore != False:
            if ignore[0] == "r":
                rows = self._find_reflect(self.data, ignore[1])
        if rows != -1:
            return ("r", rows)
        columns = self._find_reflect(self._transposed(self.data))
        if ignore != False:
            if ignore[0] == "c":
                columns = self._find_reflect(self._transposed(self.data), ignore[1])
        if columns != -1:
            return ("c", columns)
        return None
    
    def show(self):
        for line in self.data:
            print(line)
        print()

def parse(filename):
    result = []
    with open(filename, "r") as file:
        data = []
        for line in file:
            if line.strip() == "":
                result += [TwoDimensionalList(data)]
                data = []
            else:
                data += [list(line.strip())]
        result += [TwoDimensionalList(data)]
    return result

def part_a(parsed_data):
    result = 0
    for testcase in parsed_data:
        reflection = testcase.reflect()
        if reflection == None:
            raise ValueError
        if reflection[0] == "r":
            result += reflection[1]*100
        else:
            result += reflection[1]
    return result

def part_b(parsed_data):
    result = 0
    for testcase in parsed_data:
        reflection = testcase.reflect()
        found_new = False
        for i in range(len(testcase.data)):
            for j in range(len(testcase.data[0])):
                if found_new:
                    continue
                data_copy = deepcopy(testcase.data)
                if data_copy[i][j] == "#":
                    data_copy[i][j] = "."
                else:
                    data_copy[i][j] = "#"
                newList = TwoDimensionalList(data_copy)
                new_reflection = newList.reflect(reflection)
                if new_reflection == None:
                    continue
                if new_reflection == reflection:
                    continue
                if new_reflection[0] == "r":
                    result += new_reflection[1]*100
                else:
                    result += new_reflection[1]
                found_new = True
        if not found_new:
            print("NONE")
    return result

def test():
    testdata = [
        ['#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.'],
        ['.', '#', '.', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '#', '#'],
        ['.', '#', '.', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '#', '#'],
        ['#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.'],
        ['#', '#', '#', '.', '.', '#', '#', '.', '#', '.', '#', '.', '.', '#', '.'],
        ['#', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '.', '.', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '#', '#', '#', '#', '.', '.', '.', '.', '#']
    ]
    newList = TwoDimensionalList(testdata)
    print(newList.reflect(('r',2)))

def main(filename):
    parsed_data = parse(filename)
    a_sol = part_a(parsed_data)
    #test()
    #input()
    print(a_sol)
    b_sol = part_b(parsed_data)
    print(b_sol)

if __name__ == '__main__':
    main('2023/Day13/main_input.txt')