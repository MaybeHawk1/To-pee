import json
import os
import sys


class JsonDB:
    def __init__(self, todo: str, title: str, debug: bool, fileName: str) -> None:
        self.debug = debug
        self.todo = todo
        self.title = title
        self.file = fileName

    def initJson(self):
        for i in os.listdir(os.getcwd()):
            if i == "todo.json":
                exist = True
            else:
                with open(self.file, "w") as todoList:
                    if self.debug:
                        todoList.readlines()
                        sys.exit(0)

    def addTodos(self):
        # Im praying to God this works
        todo = {
            "title": self.title,
            "todo": self.todo
        }

        with open(self.file ,"r+")as todoJson:
            json.dump(todo, todoJson, indent=4)
        # Update: 2024-11-5, 14:34: What the fuck bro
        # Update: 2024-11-5, 18:49: Go fuck youserlf
        # Update: 2024-11-5, 19:00: WOOOOO FUCK YEAH BABY IT WORKS

    def viewTodos(self):
        # Dumb stuff i dont think they will work
        for i in self.file:
            print(json.dumps(self.file, indent=4))


try:
    DB = JsonDB(sys.argv[2], sys.argv[3], False, "todo.json")

    # What ze fuck bro
    # This happens when there is either no args or argv[1] is equal to --help
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print("Usage: todo [mode]\nModes: \t--fzf OR -f\t--view OR -v")
    # This checks what the user actually wants to (will user a better way later on)
    elif sys.argv[1] == "--add" or sys.argv[1] == "-a":
    # What happens if argv[2] is empy
        if sys.argv[2] == "" or sys.argv[2] is None:
            print("Nothing to add to todo list")
        # What happens if argv[2] is NOT empty
        else:
            DB.initJson()
            DB.addTodos()
            print("Todo Added")
# Error catching bullshit stuff
except IndexError:
    print("Usage: todo [mode]\nModes: \t--fzf OR -f\t--view OR -v")
