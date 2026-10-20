import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['description']}")
    print()

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if task_num < 1 or task_num > len(tasks):
            print("Error: No task with that number exists.")
            return
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        if task_num < 1 or task_num > len(tasks):
            print("Error: No task with that number exists.")
            return
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()