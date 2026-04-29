'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/29/26
Group: 17
Description:
'''


from tasklist import Tasklist 
import check_input

def main_menu():
    print("\n-Tasklist")
    print("1. Display Current Task")
    print("2. Display all task")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")

    while True:
        choice = input("Enter choice:").strip()
        ### check input here

def get_date():
    print("Enter due date:")

    while True: 
        try:
            month = int(input("Enter month:"))
            day = int(input("Enter day:"))
            year = int(input("Enter year:"))

            ###check input
        except ValueError:
            print("Invalid input. Try again")


def get_time():
    print("Enter time:")

    while True:
        try:
            hour = int(input("Enter hour:"))
            minute = int(input("Enter minute:"))

            ##Check input

        except ValueError:
            print("Invalid input. Try again")

def main():
    filename = "tasklist.txt"
    tasklist = Tasklist(tasklist.txt)

    while True:
        print(f"\nTasks to complete: {len(tasklist)}")

        choice = main_menu()

        if choice == 1:
            task = tasklist.get_current_task()
            if task:
                print(task)
            else:
                print("All tasks are complete")

        elif choice == 2:
            if len(tasklist) == 0:
                print("No tasks to display")
            else:
                i = 1
                for task in tasklist:
                    print(f"{i}.{task}")
                    i += 1

        elif choice == 3:
            task = tasklist.mark_complete()
            if task:
                print("Completed:", task)
                new_task = tasklist.get_current_task()
                if new_task:
                    print("Next task:", new_task)
                else:
                    print("All tasks are completed")

        elif choice == 4:
            desc = input("Enter a task:").strip()
            date = get_date()
            time = get_time()
            tasklist.add_task(desc,date,time)

        elif choice == 5:
            date = get_date()
            found = False

            for task in tasklist: 
                if task.date == date:
                    print(task)
                    found = True
            
            if not found:
                print("No tasks found for that date")


        elif choice == 6:
            tasklist.save_file()
            print("Tasks saved. Goodbye")
            break

if __name__ == "__main__":
    main()
