def ReadFile(filename):
    input_list = []
    with open(filename, "r") as input_data:
        for line in input_data:
            input_list = line.split(",")
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    return input_list

def debug_display(program_list, instr_marker, instruction, formatted_instr):
    if instruction == "01":
        print("+", formatted_instr[0], formatted_instr[1], "=", str(formatted_instr[0] + formatted_instr[1]))
    elif instruction == "02":
            print("*", formatted_instr[0], formatted_instr[1], "=", str(formatted_instr[0] * formatted_instr[1]))
    elif instruction == "3":
        print("INPUT")
    elif instruction == "4":
        print("OUTPUT")

def FormatInstruction(opcode, program_list, instr_marker):
    formatted_instr = []
    for i in range(1, len(opcode)):
        if opcode[-i] == "1":
            formatted_instr.append(program_list[instr_marker+i])
        elif opcode[-i] == "0":
            formatted_instr.append(program_list[program_list[instr_marker+i]])
        print("formatting...")
    return formatted_instr

def ExecuteInstruction(program_list, instr_marker, instruction):
    if len(instruction) > 1 :
        formatted_instr = FormatInstruction(
            str(program_list[instr_marker])[0:len(str(program_list[instr_marker-3]))],
            program_list,
            instr_marker)
        print(program_list[instr_marker],program_list[instr_marker+1],program_list[instr_marker+2],program_list[instr_marker+3])
    elif not (instruction in ["3","4"]):
        formatted_instr = [program_list[program_list[instr_marker+3]], program_list[program_list[instr_marker+1]], program_list[program_list[instr_marker+2]]]
        print(program_list[instr_marker],program_list[instr_marker+1],program_list[instr_marker+2],program_list[instr_marker+3])
    else:
        print(program_list[instr_marker],program_list[instr_marker+1])
    #debug_display(program_list, instr_marker, instruction, formatted_instr)
    print(str(program_list[instr_marker])[0:len(str(program_list[instr_marker-3]))])
    if instruction == "01":
        program_list[formatted_instr[2]] = formatted_instr[0] + formatted_instr[1]
    elif instruction == "02": 
        program_list[formatted_instr[2]] = formatted_instr[0] * formatted_instr[1]
    elif instruction == "3":
        program_list[program_list[instr_marker+1]] = int(input("enter input: "))
    elif instruction == "4":
        print(program_list[program_list[instr_marker+1]])
    return program_list

def RunProgram(program_list):
    instruction = str(program_list[0])[-2:]
    instr_marker = 0
    while instruction != 99:
        program_list = ExecuteInstruction(program_list, instr_marker, instruction)
        if instruction in ["3","4"]:
            instr_marker += 2
        else:
            instr_marker += 4
        instruction = str(program_list[instr_marker])[-2:]
    return program_list

def Main():
    RunProgram(ReadFile("Day5/input.txt"))

if __name__ == "__main__":
    Main()