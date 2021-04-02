found = False
number_list = []
with open("2020/Day1/main_input.txt","r") as File:
    for line in File:
        number_list.append(int(line.strip()))

for num1 in number_list:
    for num2 in number_list:
        for num3 in number_list:
            if num1 + num2 + num3 == 2020:
                print(num1*num2*num3)
                found = True
        if found:
            break