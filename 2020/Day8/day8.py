def ReadFile(FileName):
    Instructions = []
    with open(FileName,"r") as InstructionList:
        for line in InstructionList:
            templist = line.strip().split()
            templist[1] = int(templist[1])
            Instructions.append(templist)
    return Instructions

def RepeatUntilDouble(Instructions):
    pointer = 0
    visited = []
    accumulator = 0
    while True:
        if pointer in visited:
            return accumulator
        visited.append(pointer)
        current_instruction = Instructions[pointer]
        if current_instruction[0] == "nop":
            pointer += 1
        elif current_instruction[0] == "jmp":
            pointer += current_instruction[1]
        elif current_instruction[0] == "acc":
            accumulator += current_instruction[1]
            pointer += 1


def Main():
    print(RepeatUntilDouble(ReadFile("2020/Day8/main_input.txt")))

if __name__ == "__main__":
    Main()