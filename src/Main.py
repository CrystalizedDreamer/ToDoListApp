def main():
    from tasks import Task_Manager
    task_manager = Task_Manager()
    import os
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print("Welcome to your personal task manager...")
    print("Before we begin, what is your name?")
    name = input("Enter your name: ")
    os.system('cls')
    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print(f"Hello, {name}! Let's proceed")
    
    while True:
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        print(f"\n{name} Please select an action...\n")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            task_manager.add_task(task)
            os.system('cls')
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            print(f'Task "{task}" added.')
        elif choice == "2":
            tasks = task_manager.view_tasks()
            if tasks:
                os.system('cls')
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                print("Current tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
            else:
                os.system('cls')
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                print("No tasks available.")
        elif choice == "3":
            task_id = int(input("Enter the task ID to delete: ")) - 1
            if task_manager.delete_task(task_id):
                os.system('cls')
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                print(f"Task {task_id + 1} deleted.")
            else:
                os.system('cls')
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
                print("Bestie... that is NOT a valid task ID, wanna try that again?.")
        elif choice == "4":
            os.system('cls')
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            print(f"Goodbye, {name}! Session Terminating.")
            break
        else:
            os.system('cls')
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
            print("I'm not certain what part of '1-4' you don't understand, but please try again.")


main()