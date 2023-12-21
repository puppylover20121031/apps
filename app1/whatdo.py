import random
import json
from TTS369 import TTS

def whattodo():

    with open('C:/Users/jaydenpuppy/Documents/GitHub/apps/app1/todolist.json', 'r+') as f1:
        todo_list = json.load(f1)
        num_tasks = len(todo_list['unfinished'])
        print(f"You have {num_tasks} tasks:")
        TTS(f"you have {num_tasks} tasks").say()
        for task_num, task_desc in todo_list['unfinished'].items():
            print(f"{task_num}: {task_desc}")
            TTS(f"{task_num}: {task_desc}").say()
        if num_tasks >= 10:
            print("That's a lot of tasks! Good luck!")
            TTS("That's a lot of tasks! Good luck!").say()
        if todo_list["unfinished"].items() != enumerate(todo_list["unfinished"], 1):
            print("oh no your number order is not correct i will fix it!")
            TTS("oh no your number order is not correct, i will fix it").say()
            fixed = sorted(todo_list["unfinished"].items())
            print(str(fixed).replace("[(", "{").replace(")]", "}"))
            f1.truncate(0)
            f1.write(str(fixed).replace("[(", "{").replace(")]", "}").replace("(", "{").replace(")", "}"))