# Simple To-Do List Application

todo_list = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if len(todo_list) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == '3':
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
