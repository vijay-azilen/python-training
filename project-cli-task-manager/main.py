from task_manager import TaskManager


manager = TaskManager()


while True:
    print ("\nTask Manager")
    print ("1. Add Task")
    print ("2. View Tasks")
    print ("3. Exit")
    
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        manager.add_task(title, description)
        print("Task added successfully!")
    elif choice == '2':
        tasks = manager.view_tasks()
        if tasks:
            for task in tasks:
                print(f"Title: {task['title']}, Description: {task['description']}")
        else:
            print("No tasks available.")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")  