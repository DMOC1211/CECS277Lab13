'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/29/26
Group: 17
Description: A tasklist mantained by the user. Uses the Tasklist file in order to keep a 
record of all current tasks, and allows the user choices in order to modify said list. This includes
"completing" a task and adding a new one, but the user can look at their next task, view all, or 
search by date for a specific one. Includes functions for the main menu and date/time data collection
'''

from tasklist import Tasklist 
import check_input

def main_menu():
    '''The main menu for the task list. Displays all 6 options that the user can 
    choose, then returns the choice as long as it is valid.'''

    print("\n-Tasklist")
    print("1. Display Current Task")
    print("2. Display all task")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")

    #Asks user for the choice between 1 and 6. Will reject all other inputs.
    choice = check_input.get_int_range("Enter choice: ", 1, 6)
    return choice

def get_date():
    '''Function for retrieving the date of either a new or existing task from the user. Requires
    input of a month from 1-12, day from 1-31, and a year from 2000-2100. Formats all inputs as strings for use
    with Task object creation. If an input is single digit, the program will automatically add a 0 in
    front for formatting/searching purposes'''

    print("Enter due date:")
    #Month input
    month = check_input.get_int_range("Enter month: ", 1, 12)
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    #Day input
    day = check_input.get_int_range("Enter day: ", 1, 31)
    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)
    
    #Year input. Format check not required.
    year = str(check_input.get_int_range("Enter year: ", 2000, 2100))

    #Returns data in traditional calander format
    return month + "/" + day + "/" + year


def get_time():
    '''Function for retrieving the time of either a new or existing task from the user. Requires
    input of a hour from 1-12 and a minute from 0-59. Formats all inputs as strings for use
    with Task object creation. If an input is single digit, the program will automatically add a 0 
    in front for formatting/searching purposes'''

    print("Enter time:")

    #Hour input
    hour = check_input.get_int_range("Enter hour: ", 1, 12)
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)

    #Minute input
    minute = check_input.get_int_range("Enter minute: ", 0, 59)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    #Returns the combined time in standard digital formatting
    return hour + ":" + minute

def main():
    '''Main function for the user's task list. Creates a tasklist based on the text file and 
    prompts the user for a choice of action. From options 1-6, this will Display the next task, 
    Display all tasks, Complete a task and remove it, Allow for a new task to be added, Search 
    for a task based on it's date, or save the list and quit out respectivly.'''
    filename = "tasklist.txt"
    tasklist = Tasklist(filename)

    while True:
        
        #Starting page with the task amount and menu displayed
        print(f"\nTasks to complete: {len(tasklist)}")

        choice = main_menu()

        #Call to task list to get the next task
        if choice == 1:
            task = tasklist.get_current_task()
            if task:
                print(task)
            else:
                print("All tasks are complete")
        
        #Iterates through tasklist to print all task (if any)
        elif choice == 2:
            if len(tasklist) == 0:
                print("No tasks to display")
            else:
                i = 1
                for task in tasklist:
                    print(f"{i}.{task}")
                    i += 1

        #Call to Tasklist object to mark task complete. Tells the user as such
        elif choice == 3:
            task = tasklist.mark_complete()
            if task:
                print("Completed: ", task)
                new_task = tasklist.get_current_task()
                if new_task:
                    print("Next task: ", new_task)
                else:
                    print("All tasks are completed")

        #Gains data to add a new task via Tasklist
        elif choice == 4:
            desc = input("Enter a task: ").strip()
            date = get_date()
            time = get_time()
            tasklist.add_task(desc,date,time)

        #Gains data for the requested date, then searches Tasklist for the same date.
        elif choice == 5:
            date = get_date()
            found = False

            for task in tasklist: 
                if task.date == date:
                    print(task)
                    found = True
            
            if not found:
                print("No tasks found for that date")

        #Calls Tasklist to write down the current state, then ends program
        elif choice == 6:
            tasklist.save_file()
            print("Tasks saved. Goodbye")
            break

if __name__ == "__main__":
    main()

