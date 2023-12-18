from time import time
from copy import deepcopy

class mirrors():
    grid = []
    energised = {}

    def __init__(self, g):
        self.grid = g
        self.energised = {}

    def shoot_laser(self, pos, step):
        (i_step, j_step) = step
        (start_i, start_j) = pos
        new_i = start_i + i_step
        new_j = start_j + j_step
        terminate = False
        while not terminate:

            if new_i < 0 or new_j < 0 or new_i >= len(self.grid) or new_j >= len(self.grid):  # case: offgrid
                #print("case offgrid")
                break

            if (new_i, new_j) in self.energised:  # case: traversed already
                if step in self.energised[(new_i, new_j)]:
                    #print("case traversed")
                    break
            
            if (new_i, new_j) in self.energised:  # energise square w direction for cycle detection later
                self.energised[(new_i, new_j)] += [step]
            else:
                self.energised[(new_i, new_j)] = [step]

            current_space = self.grid[new_i][new_j]

            if current_space == "." or (current_space == "-" and abs(j_step) == 1) or (current_space == "|" and abs(i_step) == 1):
                #print("case nextspace")
                new_i += i_step
                new_j += j_step
                continue

            if current_space == "/":
                if step == (1,0):
                    self.shoot_laser((new_i, new_j), (0,-1))
                elif step == (-1,0):
                    self.shoot_laser((new_i, new_j), (0,1))
                elif step == (0,1):
                    self.shoot_laser((new_i, new_j), (-1,0))
                elif step == (0,-1):
                    self.shoot_laser((new_i, new_j), (1,0))
                #print("new single thread")
                break

            if current_space == "\\":
                if step == (1,0):
                    self.shoot_laser((new_i, new_j), (0,1))
                elif step == (-1,0):
                    self.shoot_laser((new_i, new_j), (0,-1))
                elif step == (0,1):
                    self.shoot_laser((new_i, new_j), (1,0))
                elif step == (0,-1):
                    self.shoot_laser((new_i, new_j), (-1,0))
                #print("new single thread")
                break

            if current_space == "|":
                self.shoot_laser((new_i, new_j), (1,0))
                self.shoot_laser((new_i, new_j), (-1,0))
                break

            if current_space == "-":
                self.shoot_laser((new_i, new_j), (0,1))
                self.shoot_laser((new_i, new_j), (0,-1))
                break
        return

    def getEnergised(self):
        return len(self.energised)

def parse(filename) -> mirrors:
    with open(filename, "r") as file:
        data = []
        for line in file:
            data += [list(line.strip())]
    return data

def part_a(parsed_data, start, step):
    new = mirrors(deepcopy(parsed_data))
    new.shoot_laser(start, step)
    return new.getEnergised()

def part_b(parsed_data):
    max_seen = 0
    for i in range(len(parsed_data)):
        max_seen = max(max_seen, part_a(parsed_data, (i,-1),(0,1)))
        max_seen = max(max_seen, part_a(parsed_data, (i,len(parsed_data)),(0,-1)))
        max_seen = max(max_seen, part_a(parsed_data, (-1,i),(1,0)))
        max_seen = max(max_seen, part_a(parsed_data, (len(parsed_data),i),(-1,0)))
    return max_seen
        

def main(filename):
    parsed_data = parse(filename)
    start = time()
    a_sol = part_a(parsed_data, (0, -1), (0, 1))
    end = time()
    print((end-start), "s")
    print(a_sol)
    start = time()
    b_sol = part_b(parsed_data)
    end = time()
    print((end-start), "s")
    print(b_sol)

if __name__ == '__main__':
    main('2023/Day16/main_input.txt')