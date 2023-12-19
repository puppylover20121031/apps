from whatdo import whattodo
print("hello")
run = True
while run:
    cmd = input("what do want to do?\n")
    match cmd:
        case "what do i do":
            whattodo()
        case "":
            print("sorry you did not enter a command.")
