def ReadFile(FileName):
    Instructions = []
    with open(FileName,"r") as InstructionList:
        for line in InstructionList:
            templist = line.strip().split()
            templist[1] = int(templist[1])
            Instructions.append(templist)
    return Instructions

def RepeatUntilDoubleOrEnd(Instructions):
    pointer = 0
    visited = []
    accumulator = 0
    while True:
        if pointer in visited:
            return False, accumulator
        elif pointer >= len(Instructions):
            return True, accumulator
        visited.append(pointer)
        current_instruction = Instructions[pointer]
        if current_instruction[0] == "nop":
            pointer += 1
        elif current_instruction[0] == "jmp":
            pointer += current_instruction[1]
        elif current_instruction[0] == "acc":
            accumulator += current_instruction[1]
            pointer += 1

def FindFixedCode(Instructions):
    Passed = False
    JmpNopCount = 0
    while not Passed:
        count = 0
        changed = False
        ModifiedInstructions = []
        for item in Instructions:
            if item[0] in ["jmp","nop"] and count>=JmpNopCount and not changed:
                tempitem = item[:]
                if item[0] == "jmp":
                    tempitem[0] = "nop"
                elif item[0] ==  "nop":
                    tempitem[0] = "jmp"
                ModifiedInstructions.append(tempitem)
                changed = True
                JmpNopCount += 1
            elif item[0] in ["jmp","nop"] and not changed:
                ModifiedInstructions.append(item)
                count += 1
            else:
                ModifiedInstructions.append(item)
        Passed, accumulator = RepeatUntilDoubleOrEnd(ModifiedInstructions)
    return accumulator

def Main():
    print(FindFixedCode(ReadFile("2020/Day8/main_input.txt")))

if __name__ == "__main__":
    Main()