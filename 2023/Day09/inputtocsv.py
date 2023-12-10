def main():
    filename = "2023/Day09/main_input.txt"
    outputfile = "2023/Day09/main_input.csv"
    data = []
    with open(filename,"r") as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    with open(outputfile, "w") as file:
        for line in data:
            line = line.replace(" ", ",") + "," + "\n"
            file.write(line)
    return


if __name__ == '__main__':
    main()