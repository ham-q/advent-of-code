def parse_cards(filename):
    result = {}
    with open(filename, "r") as file:
        for line in file:
            temp = line.strip().split(": ")
            key = int(temp[0].split()[1])
            temp = list(map(lambda x: list(map(lambda x: int(x) ,x.split())), temp[1].split(" | ")))
            result[key] = (temp[0],temp[1])
    return result

def get_num_of_matching(list1, list2):
    matching_num = 0
    for i in range(len(list1)):
        current_num = list1.pop()
        if current_num in list2:
            matching_num += 1
            list2.remove(current_num)
    return matching_num

def get_cards_points(game_cards):
    result = []
    for (winning_nums, actual_nums) in game_cards.values():
        matching_num = get_num_of_matching(winning_nums, actual_nums)
        result += [int(pow(2, matching_num-1))]
    return result

def get_num_of_scratchcards(game_cards):
    num_of_scratchcards = [1]*len(game_cards)
    for i in range(len(num_of_scratchcards)):
        (winning_nums, actual_nums) = game_cards[i+1]
        matching_num = get_num_of_matching(winning_nums, actual_nums)
        for j in range(matching_num):
            num_of_scratchcards[i+j+1] += num_of_scratchcards[i]
    return num_of_scratchcards

def main(filename):
    game_cards = parse_cards(filename)
    total_scratchcards = get_num_of_scratchcards(game_cards)
    print(sum(total_scratchcards))

if __name__ == "__main__":
    main("2023/Day04/main_input.txt")