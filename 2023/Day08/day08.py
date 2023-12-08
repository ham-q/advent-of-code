from dataclasses import dataclass
from functools import reduce
from math import lcm

@dataclass
class node:
    value: str
    left: 'node'
    right: 'node'

def parse_graph(filename):
    with open(filename,"r") as file:
        file_data = list(map(lambda x: x.strip(),file.readlines()))
        rule = list(file_data[0])
        node_data = {}
        for node in file_data[2:]:
            line_data = node.split()
            node_data[line_data[0]] = [line_data[2][1:-1],line_data[3][:-1]]
        return (rule, node_data)

def part_a_condition(currentnode, steps):
    return currentnode != "ZZZ"

def part_b_condition(currentnode, steps):
    return steps != 1

def steps_with_rule(move_rule, graph, start_node, part_b= False):
    steps = 0
    current_node = start_node
    if not part_b:
        condition = part_a_condition
    else:
        condition = part_b_condition
    while condition(current_node, steps):
        selected_move = move_rule[steps%len(move_rule)]
        if selected_move == "L":
            current_node = graph[current_node][0]
        elif selected_move == "R":
            current_node = graph[current_node][1]
        else:
            raise ValueError("Move Ruleset contains characters that aren't 'L' or 'R'.")
        steps += 1
    return (steps, current_node)

def find_cycle(move_rule, graph, start_node):
    visited = {}
    current_node = start_node
    steps = 0
    while (current_node, steps%len(move_rule)) not in visited:
        selected_move = move_rule[steps%len(move_rule)]
        visited[(current_node, steps%len(move_rule))] = steps
        current_node = graph[current_node][0] if selected_move == "L" else graph[current_node][1]
        steps += 1
    return(current_node, visited[(current_node, steps%len(move_rule))], steps)

def total_steps(move_rule, graph):
    start_nodes = []
    for key in graph.keys():
        if key[2] == "A":
            start_nodes += [key]
    steps = 0
    print(start_nodes)
    while not all(node[2]=="Z" for node in start_nodes):
        selected_move = move_rule[steps%len(move_rule)]
        for i in range(len(start_nodes)):
            next_node = graph[start_nodes[i]][0] if selected_move == "L" else graph[start_nodes[i]][1]
            start_nodes[i] = next_node
        steps += 1
        if steps%1_000_000 == 0:
            print(steps)
    return steps

def total_steps_redux(move_rule, graph):
    start_nodes = []
    for key in graph.keys():
        if key[2] == "A":
            start_nodes += [key]
    cycles = []
    for node in start_nodes:
        cycles += [find_cycle(move_rule,graph,node)]
    print(cycles)
    z_locations = []
    for i in range(len(start_nodes)):
        z = []
        cycle_info = cycles[i]
        current_node = cycle_info[0]
        for steps in range(cycle_info[1],cycle_info[2]):
            if current_node[2] == "Z":
                z += [steps]
            selected_move = move_rule[steps%len(move_rule)]
            current_node = graph[current_node][0] if selected_move == "L" else graph[current_node][1]
        assert current_node == cycle_info[0]
        z_locations += z
    print(z_locations)
    return lcm(*tuple(z_locations))


def main(filename):
    (move_rule, graph) = parse_graph(filename)
    # (part_a_steps, final) = steps_with_rule(move_rule, graph,"AAA")
    # print(part_a_steps)
    part_b_steps = total_steps_redux(move_rule, graph)
    print(part_b_steps)

if __name__ == '__main__':
    main("2023/Day08/main_input.txt")