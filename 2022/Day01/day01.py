def Parse(FileName: str) -> list[int]:
    output: list[int] = []
    curr_elf: int = 0
    with open(FileName ,"r") as File:
            for line in File:
                if line != "\n":
                    curr_elf += int(line)
                else:
                    output.append(curr_elf)
                    curr_elf = 0
    return output

def TopThree(CalList: list[int]) -> int:
    SortedList: list[int] = sorted(CalList)
    total: int = 0
    for i in range(3):
        total += SortedList.pop()
    return total

print(TopThree(Parse("2022/Day01/main_input.txt")))