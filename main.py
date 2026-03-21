import json


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.__completed = completed

    def mark_done(self):
        self.__completed = True

    def is_completed(self):
        return self.__completed

    def show(self):
        status = "Done" if self.__completed else "Pending"
        return f"{self.title} [{status}]"


class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()   # NEW

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()   # NEW
        print(f"Task '{title}' added")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save_tasks()   # NEW
            print("Task marked as done")
        else:
            print("Invalid task number")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task.show()}")

    # NEW FUNCTION
    def save_tasks(self):
        data = []
        for task in self.tasks:
            data.append({
                "title": task.title,
                "completed": task.is_completed()
            })

        with open("tasks.json", "w") as f:
            json.dump(data, f)

    # NEW FUNCTION
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)

            for item in data:
                task = Task(item["title"], item["completed"])
                self.tasks.append(task)

        except:
            pass


if __name__ == "__main__":
    todo = TodoList()

    while True:
        print("\nTodo Menu")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            todo.add_task(title)

        elif choice == "2":
            todo.show_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter task number: "))
                todo.complete_task(index)
            except:
                print("Invalid input")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")