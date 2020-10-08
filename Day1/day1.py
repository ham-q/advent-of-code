import math

def Fuel_Calculation(module): #input is float
    cost = 0
    total_cost=0 #used to total needed fuel (for module and fuel)
    cost = math.floor((module/3))-2
    while cost > 0:
        total_cost += cost
        cost = math.floor((cost/3))-2
    return total_cost

def Total_Fuel_Calculation(module_list):
    Fuel_Total = 0 #used to track total fuel cost
    for module in module_list:
        Fuel_Total += Fuel_Calculation(float(module))
    return Fuel_Total

def Read_File(filename):
    module_list = []
    with open(filename, "r") as module_file:
        for line in module_file:
            module_list.append(line.strip()) #formats string correctly
    return module_list

print("Total fuel consumption will be:", Total_Fuel_Calculation(Read_File("day1/input.txt")))