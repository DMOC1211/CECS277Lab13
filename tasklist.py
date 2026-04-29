'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/29/26
Group: 17
Description: Iterator. Creates the tasklist class and fills it with tasks from the provided text
file. Creates methods for adding/removing tasks, return the current task, saving the file,
and iteration through the file via __next__. 
'''

from task import Task

class Tasklist:
    def __init__(self,tasklist):
        '''Initializer for the task list. Iterates through the given text file
        (named tasklist) and saves that as well as an iteration counter and the list as 
        extracted from the test file. Each line in the text file is used to create a new task for
        the program.'''

        # Reads the list of tasks from the file and stores them by opening the file
        self.tasklist = []
        self.filename = Task
        self.list = tasklist
        self.n = 0 

        try:
            #Opens the file provided
            with open(self.list, "r") as file:
                for line in file:
                    line = line.strip()
                    #Creation of data for the task by removing all separation between data bits.
                    if line:
                        desc, date, time = line.split(', ')
                        self.tasklist.append(Task(desc, date, time))
            #Self call to order list
            self.tasklist.sort()
        except FileNotFoundError:
            pass
    
    def add_task(self,desc,date,time):
        #Creates a new task using the parameters, adds it to the tasklist and sorts the list
        new_task = Task(desc,date,time)
        self.tasklist.append(new_task)
        self.tasklist.sort()

    def get_current_task(self):
        #Returns the task that is at the beginning of the list
        if len(self.tasklist) == 0:
            return None
        return self.tasklist[0]
    
    def mark_complete(self):
        #Removes and returns the current task from the list
        if len(self.tasklist) == 0:
            return None
        return self.tasklist.pop(0)
    
    def save_file(self):
        # Writes hte content of the tasklist back to the file using the repr method
        with open(self.list, 'w') as file:
            for task in self.tasklist:
                file.write(repr(task)+ '\n')

    def __len__(self):
        # Returns the number of items in the tasklist
        return len(self.tasklist)
    
    def __iter__(self):
        # Initializes the iterator attribute 'n' and returns itself
        self.n = 0 
        return self
    
    def __next__(self):
        # Iterate the iterator at each position.  Raises a StopIteration when the iterator reaches 
        # the end of the tasklist, if not, returns the Task object at the iterator's current positon
        if self.n >= len(self.tasklist):
            raise StopIteration
        task = self.tasklist[self.n]
        self.n += 1
        return task 
