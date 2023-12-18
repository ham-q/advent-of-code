from copy import deepcopy

class platform:
    platform = []

    def __init__(self, platform) -> None:
        self.platform = platform

    def _rot_clockwise(self, m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

    def hash(self):
        round_locs = []
        for i in range(0, len(self.platform)):
            for j in range(0, len(self.platform[0])):
                if self.platform[i][j] == "O":
                    round_locs += (i,j)
        return tuple(round_locs)

    def rollNorth(self):
        change = False
        new_platform = [self.platform[0]]
        for i in range (1, len(self.platform)):
            new_row = []
            for j in range(0, len(self.platform[0])):
                if self.platform[i][j] == "O":
                    if new_platform[i-1][j] == ".":
                        new_platform[i-1][j] = "O"
                        new_row += ["."]
                        change = True
                    else:
                        new_row += ["O"]
                else:
                    new_row += [self.platform[i][j]]
            new_platform += [new_row]
        self.platform = new_platform
        return change         

    def rollFarDirection(self, d):
        change = True
        if d == "S":
            self.platform = self._rot_clockwise(self._rot_clockwise(self.platform))
        elif d == "E":
            self.platform = self._rot_clockwise(self.platform)
        elif d == "W":
            self.platform = self._rot_clockwise(self._rot_clockwise(self._rot_clockwise(self.platform)))

        while change:
            change = self.rollNorth()

        if d == "S":
            self.platform = self._rot_clockwise(self._rot_clockwise(self.platform))
        elif d == "E":
            self.platform = self._rot_clockwise(self._rot_clockwise(self._rot_clockwise(self.platform)))
        elif d == "W":
            self.platform = self._rot_clockwise(self.platform)
        return

    def spinCycle(self):
        self.rollFarDirection("N")
        self.rollFarDirection("W")
        self.rollFarDirection("S")
        self.rollFarDirection("E")
        return

    def getLoad(self):
        load = 0
        for i in range(len(self.platform)):
            num_of_round = self.platform[i].count("O")
            load += (len(self.platform)-i)*num_of_round
        return load

    def show(self):
        for line in self.platform:
            print("".join(line))

def parse(filename):
    with open(filename, "r") as file:
        data = []
        for line in file:
            data += [list(line.strip())]
    return platform(data)

def part_a(parsed_data):
    parsed_data.rollFarDirection("N")
    ans = parsed_data.getLoad()
    return ans

def part_b(parsed_data):
    seen_grids = {}
    current = parsed_data.hash()
    last = 0
    while current not in seen_grids:
        seen_grids[current] = last
        parsed_data.spinCycle()
        current = parsed_data.hash()
        last += 1
    first = seen_grids[current]

    for i in range((1_000_000_000-first)%(last-first)):
        parsed_data.spinCycle()

    ans = parsed_data.getLoad()
    return ans

def main(filename):
    parsed_data = parse(filename)
    a_sol = part_a(deepcopy(parsed_data))
    print(a_sol)
    b_sol = part_b(parsed_data)
    print(b_sol)

if __name__ == '__main__':
    main('2023/Day14/main_input.txt')