def ReadFile(FileName):
    number_list = []
    with open(FileName ,"r") as File:
        for line in File:
            number_list.append(int(line.strip()))
    return number_list

def CheckSummation(number_list):
    for num1 in number_list:
        for num2 in number_list:
            for num3 in number_list:
                if num1 + num2 + num3 == 2020:
                    return num1*num2*num3

print(CheckSummation(ReadFile("2020/Day1/main_input.txt")))