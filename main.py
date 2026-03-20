class Task:
    def __init__(self, title):
        self.title = title
        self.__completed = False   # encapsulation

    def mark_done(self):
        self.__completed = True

    def show(self):
        status = "Done" if self.__completed else "Pending"
        return f"{self.title} [{status}]"
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print("Task marked as done")
        else:
            print("Invalid task number")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task.show()}")


if __name__ == "__main__":
    todo = TodoList()

    todo.add_task("Study Python OOP")
    todo.add_task("Go to gym")

    todo.show_tasks()

    todo.complete_task(0)

    todo.show_tasks()

    