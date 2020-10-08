import math

def Fuel_Calculation(module): #input is float
    return math.floor((module/3))-2

def Total_Fuel_Calculation(module_list):
    for i in range(len(module_list)):
        