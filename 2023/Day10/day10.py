from functools import reduce

class graph:
    graph = [[]]

    def __init__(self, graph) -> None:
        self.graph = graph
    
    def get(self, x, y):
        return self.graph[x][y]
    
    def set(self, value, x, y):
        self.graph[x][y] = value
    
    def iter(self):
        return [(i,j) for i in range(len(graph)) for j in range(len(graph[0]))]

def parse(filename):
    with open(filename, "r") as file:
        result = []
        i = 0
        for line in file:
            line = list(line.strip())
            if "S" in line:
                x = line.index("S")
                s_location = (i, x)
            result += [line]
            i += 1
        return (s_location, graph(result))


def up(location):
    (x, y) = location
    return (x-1, y)

def down(location):
    (x, y) = location
    return (x+1, y)

def left(location):
    (x, y) = location
    return (x, y-1)

def right(location):
    (x, y) = location
    return (x, y+1)

def move_to(come_from, current, graph):
    symbol = graph.get(*current)
    if symbol == "7":
        return ("up", down(current)) if come_from == "left" else ("right", left(current))
    if symbol == "J":
        return ("down", up(current)) if come_from == "left" else ("right", left(current))
    if symbol == "F":
        return ("up", down(current)) if come_from == "right" else ("left", right(current))
    if symbol == "L":
        return ("down", up(current)) if come_from == "right" else ("left", right(current))
    if symbol == "-":
        return ("left", right(current)) if come_from == "left" else ("right", left(current))
    if symbol == "|":
        return ("up", down(current)) if come_from == "up" else ("down", up(current))
    else:
        raise ValueError("Expected recognised symbol, got:", symbol)

def find_s_cycle(s_location, graph):
    cycle = [s_location]
    if graph.get(*up(s_location)) in ["7","F","|"]:
        current = up(s_location)
        come_from = "down"
    elif graph.get(*right(s_location)) in ["7","J","-"]:
        current = right(s_location)
        come_from = "left"
    elif graph.get(*left(s_location)) in ["F","L","-"]:
        current = left(s_location)
        come_from = "right"
    while graph.get(*current) != "S":
        cycle += [current]
        (come_from, current) = move_to(come_from, current, graph)
    return cycle


def furthest_in_loop(cycle):
    return len(cycle)/2

def part_a(s_location, graph):
    print(s_location)
    cycle = find_s_cycle(s_location, graph)
    print(cycle)
    result = furthest_in_loop(cycle)
    return result

def fill_cycle_case(p, cycle, graph, come_from):
    if p not in cycle:
        flood_fill(p, cycle, graph)
    else:
        # note: unfinished
        pass

def flood_fill(point, cycle, graph):
    graph.set("O", *point)
    i = 0
    i_to_come_from = {
        0: "right",
        1: "left",
        2: "down",
        3: "up"
    }
    for p in [left(point), right(point), up(point), down(point)]:
        if p != "O":
            if p not in cycle:
                flood_fill(p, cycle, graph)
            else:
                come_from = i_to_come_from[i]
                fill_cycle_case(p, cycle, graph, come_from)
        i += 1

def find_enclosed(cycle, graph):
    enclosed = []
    flood_fill((0,0), cycle, graph)
    for tile in graph.iter:
        if graph.get(*tile) != "O" and tile not in cycle:
            enclosed += [tile]
    return enclosed

def part_b(s_location, graph):
    cycle = find_s_cycle(s_location, graph)
    enclosed_tiles = find_enclosed(cycle, graph)
    return len(enclosed_tiles)

from PIL import Image
def visualise(graph):
    graph_contents = graph.graph
    total_height = 3*len(graph_contents)
    total_width = 3*len(graph_contents[0])
    new_im = Image.new("RGBA", (total_width, total_height))
    elem_to_image = {
        ".": Image.open("2023/Day10/images/dot.png"),
        "|": Image.open("2023/Day10/images/pipe.png"),
        "-": Image.open("2023/Day10/images/dash.png"),
        "7": Image.open("2023/Day10/images/7.png"),
        "F": Image.open("2023/Day10/images/F.png"),
        "J": Image.open("2023/Day10/images/J.png"),
        "L": Image.open("2023/Day10/images/L.png"),
        "S": Image.open("2023/Day10/images/S.png"),
    }
    for row_num in range(len(graph_contents)):
        for col_num in range(len(graph_contents[0])):
            curr_img = elem_to_image[graph_contents[col_num][row_num]]
            new_im.paste(curr_img, (3*row_num, 3* col_num))
    new_im.show()
    new_im.save("2023/Day10/images/result.png")


def main(filename):
    (s_location, graph) = parse(filename)
    print(graph.graph)
    sol_a = part_a(s_location, graph)
    print(sol_a)
    visualise(graph)
    # sol_b = part_b(s_location, graph)
    # print(sol_b)

if __name__ == '__main__':
    main("2023/Day10/main_input.txt")