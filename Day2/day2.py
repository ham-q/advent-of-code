def ReadFile(filename): #used to read in input data for program only
    input_list = [] #initialising needed vars
    with open(filename, "r") as input_data:
        for line in input_data:
            input_list = line.split(",") #converts input into array to be dealt with easier
    for i in range(len(input_list)): #converts all items to ints to make them compatible for future operator functions
        input_list[i] = int(input_list[i])
    return input_list

def Setup(program_list, noun, verb): #setting program to correct state before iterating through
    program_list[1] = noun
    program_list[2] = verb
    print(program_list) #debugging
    return program_list

def debug_display(program_list, instr_marker, instruction): #used to see specific instrictions being executed
    if instruction == 1: #used to differentiate between commands
        print("+", program_list[instr_marker+1], program_list[instr_marker+2],program_list[instr_marker+3], "=", str(program_list[program_list[instr_marker+1]] + program_list[program_list[instr_marker+2]]))
    else:
            print("*", program_list[instr_marker+1], program_list[instr_marker+2],program_list[instr_marker+3], "=", str(program_list[program_list[instr_marker+1]] * program_list[program_list[instr_marker+2]]))

def ExecuteInstruction(program_list, instr_marker, instruction):
    debug_display(program_list, instr_marker, instruction) #shows line before execution (so before any overwriting)
    if instruction == 1:
        program_list[program_list[instr_marker+3]] = program_list[program_list[instr_marker+1]] + program_list[program_list[instr_marker+2]] #inside program_list[] is used to retrieve the location to read/write to and the outside one retrives value/writes to correct position
    elif instruction == 2: 
        program_list[program_list[instr_marker+3]] = program_list[program_list[instr_marker+1]] * program_list[program_list[instr_marker+2]]
    return program_list

def RunProgram(program_list):
    instruction = program_list[0]
    instr_marker = 0 #used to point to current opcode index
    while instruction != 99: #will run until halt code is executed
        program_list = ExecuteInstruction(program_list, instr_marker, instruction)
        instr_marker += 4
        instruction = program_list[instr_marker]
    return program_list

for noun in range(100):
    for verb in range(100):
        if RunProgram(Setup(ReadFile("Day2/input.txt"), noun, verb))[0] == 19690720:
            print((100*noun) + verb)
            quit()

#may optimise at a later date