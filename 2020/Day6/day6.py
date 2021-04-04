def ReadFile(FileName):
    GroupAnswers = []
    count = 0
    with open(FileName, "r") as SurveyData:
        for line in SurveyData:
            if line == "\n":
                count += CheckNoOfYes(GroupAnswers)
                GroupAnswers.clear()
            else:
                GroupAnswers.append(line.rstrip())
        count += CheckNoOfYes(GroupAnswers)
    return count

def CheckNoOfYes(GroupAnswers):
    LettersUsed = []
    for Survey in GroupAnswers:
        for Char in Survey:
            if not Char in LettersUsed:
                LettersUsed.append(Char)
    return len(LettersUsed)

def Main():
    print(ReadFile("2020/Day6/main_input.txt"))

if __name__ == "__main__":
    Main()