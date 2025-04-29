class TodoApp:
    def __init__(self):
        self.todo = []

    def add_task(self):
        title = input("Enter Title\n")
        new_task = {"title": title, "done": False}
        self.todo.append(new_task)
        print("Todo added successfully\n")

    def del_task(self, task_index):
        if 0 <= task_index < len(self.todo):
            removed = self.todo.pop(task_index)
            print(f"'{removed['title']}' deleted successfully\n")
        else:
            print("Invalid index\n")

    def view_tasks(self):
        if self.todo:
            print("\nYour Todo List:")
            for i, task in enumerate(self.todo, 1):
                status = "Completed" if task["done"] else "Not Completed"
                print(f"{i}. {task['title']} - {status}")
        else:
            print("\nTodo list is empty\n")

    def mark_completed(self, index):
        if 0 <= index < len(self.todo):
            self.todo[index]["done"] = True
            print(f"'{self.todo[index]['title']}' marked as completed\n")
        else:
            print("Invalid index\n")

    def run(self):
        while True:
            try:
                option = int(input("\n1: Add todo\n2: View todo\n3: Delete todo\n4: Mark as Completed\n5: Exit\n"))
                if option == 1:
                    self.add_task()
                elif option == 2:
                    self.view_tasks()
                elif option == 3:
                    self.view_tasks()
                    index = int(input("Select todo number to delete\n")) - 1
                    self.del_task(index)
                elif option == 4:
                    self.view_tasks()
                    index = int(input("Select todo number to mark as completed\n")) - 1
                    self.mark_completed(index)
                elif option == 5:
                    print("Exiting....")
                    break
                else:
                    print("Select a valid option")
            except ValueError:
                print("Please enter a valid number.")


# Run the app
if __name__ == "__main__":
    app = TodoApp()
    app.run()
