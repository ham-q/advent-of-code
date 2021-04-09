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
    Bags = [Bag]
    while Bags:
        CurrentBag = Bags.pop(0)
        if "shiny gold bag" in CurrentBag:
            return 1
        if not BagRules.get(CurrentBag)[0] in ["no other bags.","no other bags"]:
            for bag in BagRules.get(CurrentBag):
                Bags.append(ReturnBagOnly(bag))
    return 0

def ReturnBagOnly(bag):
    Numbers = ["1","2","3","4","5","6","7","8","9"]
    if bag[-1:] == "s":
        bag = bag[:-1]
    if any(x in bag for x in Numbers):
        return bag[2:].strip()
    else:
        return bag.strip()


def NoOfBagsInShinyGold(BagRules):
    Paths = CollectAllPaths("shiny gold bag",BagRules)
    return Paths
    count = 0
    for path in Paths:
        temp = 1
        for bag in path:
            temp = temp*bag

def CollectAllPaths(Bag,BagRules):
    Numbers = ["1","2","3","4","5","6","7","8","9"]
    paths = []
    currentpath = [Bag]
    while currentpath:
        print("current path is", currentpath)
        CurrentBag = currentpath[-1]
        if BagRules.get(CurrentBag)[0] in ["no other bags.","no other bags"]:
            while BagRules.get(CurrentBag)[0] in ["no other bags.","no other bags"]:
                pathtoadd = []
                for pathbag in currentpath:
                    if not (BagRules.get(CurrentBag)[0] in ["no other bags.","no other bags"] or currentpath.index(pathbag) == len(currentpath)):
                        pathtoadd.append(pathbag)
                paths.append(currentpath)
                currentpath.pop()
                CurrentBag = currentpath[-1]
            fully_searched = True
            while fully_searched:
                print("fully search list (currentpath)", currentpath)
                input()
                for child in BagRules.get(currentpath[-1]):
                    print(ReturnBagOnly(child))
                    temppath = currentpath
                    temppath.append(ReturnBagOnly(child))
                    print("temppath is",temppath, "list of paths is",paths)
                    if not any(set(temppath) <= set(x) for x in paths):
                        fully_searched = False
                if fully_searched:
                    print("before pop is", currentpath)
                    currentpath.pop()
                    print("reached condition, currentpath is", currentpath)
        else:
            print("else condition reached")
            for bag in BagRules.get(CurrentBag):
                currentpath.append(ReturnBagOnly(bag))
    return paths

def Main():
    print(NoOfBagsInShinyGold(ReadFile("2020/Day7/test_input.txt")))

if __name__ == "__main__":
    Main()