from whatdo import whattodo
from TTS369 import TTS
print("hello")
TTS("hello").say()
run = True
attempts = 0
while run:
    if attempts >= 1:
        TTS("what next").say()
    else:
        TTS("what do you want to do").say()
    attempts += 1
    cmd = input("what do you want to do?\n")
    match cmd:
        case "what do i do":
            whattodo()
        case "play":
            print("why do you want to play human i am a fucker.")
            TTS("why do you want to play human i am a fucker.").say()
        case "":
            print("sorry you did not enter a command.")
            TTS("sorry you did not enter a command.").say()
