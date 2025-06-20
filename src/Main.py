def main():
    from tasks import Task_Manager
    task_manager = Task_Manager()
    while True:
        print("Welcome to your personal task manager...")
        print("Before we begin, what is your name?")
        name = input("Enter your name: ")
        print(f"Hello, {name}! Please select an action...")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            task_manager.add_task(task)
            print(f'Task "{task}" added.')
        elif choice == "2":
            tasks = task_manager.view_tasks()
            if tasks:
                print("Current tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
            else:
                print("No tasks available.")
        elif choice == "3":
            task_id = int(input("Enter the task ID to delete: ")) - 1
            if task_manager.delete_task(task_id):
                print(f"Task {task_id + 1} deleted.")
            else:
                print("Invalid task ID.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main()