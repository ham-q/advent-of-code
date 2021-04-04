import math

def ReadFile(FileName):
    Tickets = []
    with open(FileName,"r") as TicketData:
        for line in TicketData:
            Tickets.append(line.rstrip())
    return Tickets

def CalculateMaxID(Tickets):
    MaxID = 0
    for Ticket in Tickets:
        NewTicketID = CalculateID(Ticket)
        print(NewTicketID)
        if NewTicketID > MaxID:
            MaxID = NewTicketID
        #input()
    return MaxID

def CalculateEmptySeat(Tickets):
    ListOfIDs = list(range(8,1016))
    for Ticket in Tickets:
        ListOfIDs.remove(int(CalculateID(Ticket)))
    return ListOfIDs

def CalculateID(Ticket):
    MinNum = 0
    MaxNum = 127
    MinNum8 = 0
    MaxNum8 = 7
    for Char in Ticket:
        if Char == "B":
            MinNum = (MinNum+MaxNum)//2 + 1
        elif Char == "F":
            MaxNum = (MinNum+MaxNum)//2
        elif Char == "R":
            MinNum8 = (MinNum8+MaxNum8)//2 + 1
        elif Char == "L":
            MaxNum8 = (MinNum8+MaxNum8)//2
        print("Char is", Char)
        print("Min is", MinNum)
        print("Max is", MaxNum)
    return (MinNum*8) + MaxNum8

def Main():
    print("Empty seats are", CalculateEmptySeat(ReadFile("2020/Day5/main_input.txt")))

if __name__ == "__main__":
    Main()