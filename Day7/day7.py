def ReadFile(filename):
    """Reads in text file and splits it into a list
    Input: filename(STR) - name of file in directory
    Output: input_list(LIST - all INT elements) - list containing program data"""
    input_list = []
    with open(filename, "r") as input_data:
        for line in input_data:
            input_list = line.split(",")
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    return input_list

def Setup(program_list, noun, verb):
    program_list[1] = noun
    program_list[2] = verb
    return program_list

def debug_display(instruction):
    """Used to show what instruction is being executed 
    (and to show when an incorrect instruction is executed)
    Input: instruction(STR) - the current instruction executed"""
    if instruction in ["1","01"]:
        print("ADD")
    elif instruction in ["2","02"]:
        print("MULTIPLY")
    elif instruction in ["3","03"]:
        print("INPUT")
    elif instruction in ["4","04"]:
        print("OUTPUT")
    elif instruction in ["5","05"]:
        print("JUMP IF TRUE")
    elif instruction in ["6","06"]:
        print("JUMP IF FALSE")
    elif instruction in ["7","07"]:
        print("LESS THAN")
    elif instruction in ["8","08"]:
        print("EQUAL TO")
    else:
        print("WHAT", instruction)
    
def ProgramStepper(program_list):
    """Simply shows the state of the entire program
    and allows for step by step execution - to better understand what's happening
    Input: program_list(LIST - all INT elements) - the entire program"""
    print(program_list)
    input()

def FormatInstruction(opcode, program_list, instr_marker, instruction):
    """Used to get the correct values for the command execution (direct or immediate addressal)
    To note, the loops assign all but the final parameter which is defined at the bottom of function
    (as the last is always direct)
    Inputs: opcode(STR) - the second half of an instruction (minus the 0x at the end)
        program_list(LIST - all INT elements) - the entire program
        instr_marker(INT) - the location of the currently executed opcode
        instruction(STR) - the instruction part of the entire opcode (0x)
    Outputs: formatted_instr(LIST - all INT elements) - the parameters needed for the operation, in their correct state"""
    formatted_instr = []
    i = 0
    if instruction in ["02","01","07","08"]:
        for i in range(1,3):
            try:
                if opcode[-i] == "1":
                    formatted_instr.append(program_list[instr_marker+i])
                elif opcode[-i] == "0":
                    formatted_instr.append(program_list[program_list[instr_marker+i]])
            except IndexError:
                formatted_instr.append(program_list[program_list[instr_marker+i]])
    if instruction in ["05","06"]:
        for i in range(1,3):
            try:
                if opcode[-i] == "1":
                    formatted_instr.append(program_list[instr_marker+i])
                elif opcode[-i] == "0":
                    formatted_instr.append(program_list[program_list[instr_marker+i]])
            except IndexError:
                formatted_instr.append(program_list[program_list[instr_marker+i]])
    if instruction in ["04"]:
        if opcode[-1] == "1":
            formatted_instr.append(program_list[instr_marker+1])
        elif opcode[-1] == "0":
            formatted_instr.append(program_list[program_list[instr_marker+1]])
    i+=1
    if not instruction in ["04","05","06"]:
        formatted_instr.append(program_list[instr_marker+i])
    return formatted_instr

def ExecuteInstruction(program_list, instr_marker, instruction, input1, input2, first_input):
    """Used to execute a single instruction
    First selector filters through different types of instructions (single x or 1010x ones) where the non if statements catergorise x ones
    They format the instruction parameters correctly for second selector
    This is used to execute the specific instruction (printing an error message if instruction isn't valid)
    Inputs: program_list(LIST - all INT elements) - the entire program
        instr_marker(INT) - the location of the currently executed opcode
        instruction(STR) - the instruction part of the entire opcode (0x)
    Outputs: program_list(LIST - all INT elements) - the entire program after being updated
    instr_marker(INT) - the new location of instr_marker, for the next instruction"""
    debug_display(instruction)
    output = 0
    if len(str(program_list[instr_marker])) > 1:
        formatted_instr = FormatInstruction(
            str(program_list[instr_marker])[0:len(str(program_list[instr_marker]))-2],
            program_list,
            instr_marker, 
            instruction)
    elif not (instruction in ["3","4","5","6"]):
        formatted_instr = [program_list[program_list[instr_marker+1]], program_list[program_list[instr_marker+2]], program_list[instr_marker+3]]
    elif instruction in  ["5","6"]:
        formatted_instr = [program_list[program_list[instr_marker+1]], program_list[program_list[instr_marker+2]]]
    else:
        formatted_instr = [program_list[program_list[instr_marker+1]]]

    if instruction in ["1","01"]:
        program_list[formatted_instr[2]] = formatted_instr[0] + formatted_instr[1]
        instr_marker += 4
    elif instruction in ["2","02"]: 
        program_list[formatted_instr[2]] = formatted_instr[0] * formatted_instr[1]
        instr_marker += 4
    elif instruction in ["3","03"]:
        if first_input:
            program_list[program_list[instr_marker+1]] = input1
            first_input = False
        else: 
            program_list[program_list[instr_marker+1]] = input2
        instr_marker += 2
    elif instruction in ["4","04"]:
        print(formatted_instr[0])
        output = formatted_instr[0]
        instr_marker += 2
    elif instruction in ["5","05"]:
        print(formatted_instr)
        if formatted_instr[0] != 0:
            instr_marker = formatted_instr[1]
        else:
            instr_marker += 3
    elif instruction in ["6","06"]:
        print(formatted_instr)
        if formatted_instr[0] == 0:
            instr_marker = formatted_instr[1]
        else:
            instr_marker += 3
    elif instruction in ["7","07"]:
        if formatted_instr[0] < formatted_instr[1]:
            program_list[formatted_instr[2]] = 1
        else:
            program_list[formatted_instr[2]] = 0
        instr_marker += 4
    elif instruction in ["8","08"]:
        if formatted_instr[0] == formatted_instr[1]:
            program_list[formatted_instr[2]] = 1
        else:
            program_list[formatted_instr[2]] = 0
        instr_marker += 4
    else:
        instr_marker += 2
    #ProgramStepper(program_list)
    return program_list, instr_marker, output, first_input

def RunProgram(program_list, input2, input1):
    """Runs through program until a 99 instruction is encountered
    Inputs: program_list(LIST - all INT elements) - the entire program"""
    instruction = str(program_list[0])[-2:]
    instr_marker = 0
    first_input = True
    while instruction != "99":
        program_list, instr_marker, output, first_input = ExecuteInstruction(program_list, instr_marker, instruction, input1, input2, first_input)
        instruction = str(program_list[instr_marker])[-2:]
    return output

def Main():
    outputs = []
    i = 0
    #outputted = RunProgram(ReadFile("Day7/test_input1.txt"), 0, 3)
    #outputted = RunProgram(ReadFile("Day7/test_input1.txt"), outputted, 1)
    #outputted = RunProgram(ReadFile("Day7/test_input1.txt"), outputted, 1)
    #outputted = RunProgram(ReadFile("Day7/test_input1.txt"), outputted, 3)
    #outputted = RunProgram(ReadFile("Day7/test_input1.txt"), outputted, 2)
    input()
    for A in range(5):
        for B in range(5):
            for C in range(5):
                for D in range(5):
                    for E in range(5):
                        outputted = RunProgram(ReadFile("Day7/test_input2.txt"), 0, A)
                        outputted = RunProgram(ReadFile("Day7/test_input2.txt"), outputted, B)
                        outputted = RunProgram(ReadFile("Day7/test_input2.txt"), outputted, C)
                        outputted = RunProgram(ReadFile("Day7/test_input2.txt"), outputted, D)
                        outputted = RunProgram(ReadFile("Day7/test_input2.txt"), outputted, E)
                        outputs.append(outputted)
                        i+=1
                        print(i)
    print(outputs)
    print(max(outputs))

if __name__ == "__main__":
    Main()