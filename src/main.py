import sys

file = open("todo-file.txt", "a+")


if len(sys.argv) == 1 or sys.argv[1] == "--help":
    print("Usage: todo [mode]\nModes: \t--fzf OR -f\t--view OR -v")
elif sys.argv[1] == "--add" or sys.argv[1] == "-h":
    if sys.argv[2] != "":
        file.write(str(sys.argv[2]) + "\n")
        file.close()
    else:
        print("No todos to be added")
elif sys.argv[1] == "--view":
    with open("todo-file.txt", "r")as todoFile:
        for lines in todoFile:
            sys.stdout.write(lines)
