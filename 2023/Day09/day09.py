def parse(filename):
    with open(filename,"r") as file:
        return list(map(lambda x: list(map(lambda y: int(y), x.split())), map(lambda x: x.strip(), file.readlines())))

def differentiate(l):
    result = []
    for i in range(len(l)-1):
        result += [l[i+1]-l[i]]
    return result

def next_value(l):
    if all(elem == 0 for elem in l):
        return 0
    else:
        return l[-1] + next_value(differentiate(l))

def prev_value(l):
    if all(elem == 0 for elem in l):
        return 0
    else:
        return l[0] - prev_value(differentiate(l))    

def sum_next_values(sequences):
    result = []
    for sequence in sequences:
        result += [prev_value(sequence)]
    return sum(result)

def main(filename):
    sequences = parse(filename)
    print(sum_next_values(sequences))

if __name__ == '__main__':
    main("2023/Day09/main_input.txt")