import sys
tasks = []

class TaskManager:
    def add (self, tasks):
        task = input("Please enter the task you'd like to add: ")
        if task in tasks:
            exceptAdd = input("Task is already added. Would you like to add anyway?").lower()
            if exceptAdd == "yes":
                tasks.append(task)
        else:
            tasks.append(task)
            print("Task successfully added.")


    def list(self, tasks):
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks to show.")
        prompt = ("Would you like to return to the main menu? (Y/N): ")
        if "y" in prompt:
            return
        if "n" in prompt:
            print("Thank you!")
            sys.exit()

    def delete(self, tasks):
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                delete_index = int(input("Which task would you like to delete? "))
                delete_index -=1
                if 0 <= delete_index < len(tasks):
                    tasks.pop(delete_index)
                    print("Task deleted.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid index.")
        else:
            print("No tasks to delete.")

def main():
    manager = TaskManager()
    while True:
        print("\n Welcome to Task Manager. What would you like to do today?")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")

        try:
            option = int(input("Choose an option: "))
            if option == 1:
                manager.add(tasks)
            elif option == 2:
                manager.list(tasks)
            elif option == 3:
                manager.delete(tasks)
            elif option == 4:
                sys.exit()
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid option.")

if __name__ == "__main__":
    main()
