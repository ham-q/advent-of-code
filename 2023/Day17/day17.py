from queue import PriorityQueue

def parse(filename):
    with open(filename, "r") as file:
        data = []
        for line in file:
            data += [list(map(int, list(line.strip())))]
    return data

def add_to_tuple(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])

def check_if_OOB(t1, graph):
    return t1[0] < 0 or t1[1] < 0 or t1[0] >= len(graph) or t1[1] >= len(graph[0])

def graph_value(t1, graph):
    return graph[t1[0]][t1[1]]

def set_max(x):
    return [1_000_000_000_000, 1_000_000_000_000, 1_000_000_000_000, 1_000_000_000_000]
        

def find_min_heat_loss(graph, end, smallest_step, largest_step):
    frontier = PriorityQueue()
    visited = [list(map(set_max, elem)) for elem in graph]

    to_add = 0
    for i in range(1,largest_step):
        new_tuple = add_to_tuple((0,i), (0,0))
        if check_if_OOB(new_tuple, graph):
            break
        to_add += graph_value(new_tuple, graph)
        if i >= smallest_step:
            frontier.put((to_add, (new_tuple, "R")))
    
    to_add = 0
    for i in range(1,largest_step):
        new_tuple = add_to_tuple((i,0), (0,0))
        if check_if_OOB(new_tuple, graph):
            break
        to_add += graph_value(new_tuple, graph)
        if i >= smallest_step:
            frontier.put((to_add, (new_tuple, "D")))

    min_end_found = 1_000_000_000_000

    direct_to_num = {
        "L": 0,
        "R": 1,
        "U": 2,
        "D": 3,
    }
    while not frontier.empty():
        current = frontier.get()
        position = current[1][0]
        current_val = current[0]
        direction = current[1][1]

        if current_val >= min_end_found:  # if this is triggered then all open paths are larger than found path so we stop
            break
        if position == end:
            min_end_found = min(min_end_found, current[0])
            continue
        if check_if_OOB(position, graph):  # triggered if OOB
            continue

        if current_val >= visited[position[0]][position[1]][direct_to_num[direction]]:  # we've found a shorter path to this node
            continue
        
        visited[position[0]][position[1]][direct_to_num[direction]] = current_val

        if direction == "U" or direction == "D":
            to_add = current_val
            for i in range(1,largest_step):
                new_tuple = add_to_tuple((0,-i), position)
                if check_if_OOB(new_tuple, graph):
                    break
                to_add += graph_value(new_tuple, graph)
                if i >= smallest_step:
                    frontier.put((to_add, (new_tuple, "L")))

        if direction == "U" or direction == "D":
            to_add = current_val
            for i in range(1,largest_step):
                new_tuple = add_to_tuple((0,i), position)
                if check_if_OOB(new_tuple, graph):
                    break
                to_add += graph_value(new_tuple, graph)
                if i >= smallest_step:
                    frontier.put((to_add, (new_tuple, "R")))

        if direction == "L" or direction == "R":
            to_add = current_val
            for i in range(1,largest_step):
                new_tuple = add_to_tuple((i,0), position)
                if check_if_OOB(new_tuple, graph):
                    break
                to_add += graph_value(new_tuple, graph)
                if i >= smallest_step:
                    frontier.put((to_add, (new_tuple, "D")))

        if direction == "L" or direction == "R":
            to_add = current_val
            for i in range(1,largest_step):
                new_tuple = add_to_tuple((-i,0), position)
                if check_if_OOB(new_tuple, graph):
                    break
                to_add += graph_value(new_tuple, graph)
                if i >= smallest_step:
                    frontier.put((to_add, (new_tuple, "U")))

    return min_end_found


def part_a(parsed_data):
    ans = find_min_heat_loss(parsed_data, (len(parsed_data)-1, len(parsed_data[0])-1), 1, 4)
    return ans

def part_b(parsed_data):
    ans = find_min_heat_loss(parsed_data, (len(parsed_data)-1, len(parsed_data[0])-1), 4, 11)
    return ans

def main(filename):
    parsed_data = parse(filename)
    a_sol = part_a(parsed_data)
    print(a_sol)
    b_sol = part_b(parsed_data)
    print(b_sol)

if __name__ == '__main__':
    main('2023/Day17/main_input.txt')