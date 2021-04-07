def ReadFile(FileName):
    BagRules = {}
    with open(FileName, "r") as BagData:
        for line in BagData:
            split = line.split("s contain ")
            split[1] = split[1].strip(" .\n").split(",")
            BagRules[split[0]] = split[1]
    return BagRules

def CountNoOfBags(BagRules):
    BagNumber = 1
    count = 0
    for Bag, Rules in BagRules.items():
        print(BagNumber)
        count += IfBagContainsShinyGold(Bag, BagRules)
        BagNumber += 1
    return count

def IfBagContainsShinyGold(Bag, BagRules):
    Numbers = ["1","2","3","4","5","6","7","8","9"]
    Bags = [Bag]
    while Bags:
        CurrentBag = Bags.pop(0)
        if "shiny gold bag" in CurrentBag:
            return 1
        if not BagRules.get(CurrentBag)[0] in ["no other bags.","no other bags"]:
            for bag in BagRules.get(CurrentBag):
                if bag[-1:] == "s":
                    bag = bag[:-1]
                if any(x in bag for x in Numbers):
                    Bags.append(bag[2:].strip())
                else:
                    Bags.append(bag).strip()
    return 0

def Main():
    print(CountNoOfBags(ReadFile("2020/Day7/main_input.txt")))

if __name__ == "__main__":
    Main()