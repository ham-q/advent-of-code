from copy import deepcopy
import dijkstra
from time import time

class universe:
    galaxy_locations = []
    universe_data = []
    expanded_rows = []
    expanded_cols = []
    expand_number = 1

    def _generate_galaxy_locations(self) -> None:
        self.galaxy_locations = []
        for row_num in range(len(self.universe_data)):
            for col_num in range(len(self.universe_data[row_num])):
                if self.universe_data[row_num][col_num] == "#":
                    self.galaxy_locations += [(row_num, col_num)]

    def get_all_galaxy_distances(self) -> list[int]:
        result = []
        graph = dijkstra.Graph()
        total_time = 0
        for row in range(len(self.universe_data)):
            for col in range(len(self.universe_data[row])):
                if row != len(self.universe_data)-1:
                    if row in self.expanded_rows:
                        graph.add_edge(str((row,col)), str((row+1, col)), self.expand_number)
                    else:
                        graph.add_edge(str((row,col)), str((row+1, col)), 1)
                if col != len(self.universe_data[row])-1:
                    if col in self.expanded_cols:
                        graph.add_edge(str((row,col)), str((row, col+1)), self.expand_number)
                    else:
                        graph.add_edge(str((row,col)), str((row, col+1)), 1)
                if row != 0:
                    if row in self.expanded_rows:
                        graph.add_edge(str((row,col)), str((row-1, col)), self.expand_number)
                    else:
                        graph.add_edge(str((row,col)), str((row-1, col)), 1)
                if col != 0:
                    if col in self.expanded_cols:
                        graph.add_edge(str((row,col)), str((row, col-1)), self.expand_number)
                    else:
                        graph.add_edge(str((row,col)), str((row, col-1)), 1)
        for i in range (len(self.galaxy_locations)):
            g1 = str(self.galaxy_locations[i])
            start = time()
            dijkstras = dijkstra.DijkstraSPF(graph, g1)
            end = time()
            total_time += (end-start)
            for j in range(i+1, len(self.galaxy_locations)):
                g2 = str(self.galaxy_locations[j])
                result += [dijkstras.get_distance(g2)]
        print("Cost to create dijkstras " + str(len(self.galaxy_locations)) + " times:" + str(total_time))
        return result

    def expand(self, num) -> None:
        self.expand_number = num
        for row_num in range(len(self.universe_data)):
            if all("." == x for x in self.universe_data[row_num]):
                self.expanded_rows += [row_num]
        for col_num in range(len(self.universe_data[0])):
            if all("." == x[col_num] for x in self.universe_data):
                self.expanded_cols += [col_num]

    def show(self) -> None:
        for row in self.universe_data:
            print("".join(row))
        print()

    def __init__(self, universe_data) -> None:
        self.universe_data = universe_data
        self._generate_galaxy_locations()

def parse(filename):
    with open(filename, "r") as file:
        uni_data = []
        for line in file:
            uni_data += [list(line.strip())]
        return universe(uni_data)

def part_a(universe):
    universe.expand(2)
    all_distances = universe.get_all_galaxy_distances()
    return sum(all_distances)

def part_b(universe):
    universe.expand(1_000_000)
    all_distances = universe.get_all_galaxy_distances()
    return sum(all_distances)

def main(filename):
    start = time()
    universe_info = parse(filename)
    end = time()
    print("Parse took: ", (end-start), "s")

    print("PART A")
    start = time()
    a_sol = part_a(universe_info)
    end = time()
    print(a_sol)
    print("Part A took: ", (end-start), "s")
    print()

    print("PART B")
    start = time()
    b_sol = part_b(universe_info)
    end = time()
    print(b_sol)
    print("Part B took: ", (end-start), "s")

if __name__ == '__main__':
    main("2023/Day11/main_input.txt")