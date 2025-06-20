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
            print("Adding a task...")
        elif choice == "2":
            print("Viewing tasks...")
        elif choice == "3":
            print("Deleting a task...")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()