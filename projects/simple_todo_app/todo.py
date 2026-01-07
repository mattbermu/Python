# Load saved tasks from file

try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    tasks = []


def show_menu():
    print("\n==== To-Do List App ====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("You must enter a task name.")


def mark_done():
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark as done: "))
        if 0 < task_num <= len(tasks):
            task = tasks[task_num - 1]
            if task.endswith("✅"):
                print("That task is already marked as done.")
            else:
                tasks[task_num - 1] = task + " ✅"
                print(f"Marked as done: {task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")



# --- Main Program Loop ---
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        # Save tasks before exiting
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid option, try again.")
