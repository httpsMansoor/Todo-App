todo = []

def add_task():
    title = input("Enter Title\n")
    new_task = {"title": title, "done": False}
    todo.append(new_task)
    print("Todo added successfully\n")

def del_todo(task_index):
    if 0 <= task_index < len(todo):
        removed = todo.pop(task_index)
        print(f"'{removed['title']}' deleted successfully\n")
    else:
        print("Invalid index\n")

def view_todo():
    if todo:
        print("\nYour Todo List:")
        for i, task in enumerate(todo, 1):
            status = "Completed" if task["done"] else "Not Completed"
            print(f"{i}. {task['title']} - {status}")
    else:
        print("\nTodo list is empty\n")

def mark_completed(index):
    if 0 <= index < len(todo):
        todo[index]["done"] = True
        print(f"'{todo[index]['title']}' marked as completed\n")
    else:
        print("Invalid index\n")

# Main loop
while True:
    option = int(input("\n1: Add todo\n2: View todo\n3: Delete todo\n4: Mark as Completed\n5: Exit\n"))

    if option == 1:
        add_task()
    elif option == 2:
        view_todo()
    elif option == 3:
        view_todo()
        todo_del = int(input("Select todo number to delete\n")) - 1
        del_todo(todo_del)
    elif option == 4:
        view_todo()
        idx = int(input("Select todo number to mark as completed\n")) - 1
        mark_completed(idx)
    elif option == 5:
        print("Exiting....")
        break
    else:
        print("Select a valid option")
