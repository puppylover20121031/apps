import random
import json

def whattodo():

    with open('C:/Users/jaydenpuppy/Documents/GitHub/apps/app1/todolist.json', 'r') as f:
        todo_list = json.load(f)

        num_tasks = len(todo_list['unfinished'])

        print(f"You have {num_tasks} tasks:")
        for task_num, task_desc in todo_list['unfinished'].items():
            print(f"{task_num}: {task_desc}")

        if num_tasks >= 10:
            print("That's a lot of tasks! Good luck!")


whattodo()