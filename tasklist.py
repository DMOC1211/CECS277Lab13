'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/29/26
Group: 17
Description: Creates the tasklist class, assigns the attributes, and creates methods. 
'''


from task import Task

class Tasklist:
    def __init__(self,tasklist):
        self.tasklist = []
        self.filename = Task
        self.list = tasklist
        self.n = 0 

        try:
            with open(tasklist, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        desc, date, time = line.split(',')
                        self.tasklist.append(Task(desc, date, time))
            self.tasklist.sort()
        except FileNotFoundError:
            pass
    
    def add_task(self,desc,date,time):
        new_task = Task(desc,date,time)
        self.tasklist.append(new_task)
        self.tasklist.sort()

    def get_current_task(self):
        if len(self.tasklist) == 0:
            return None
        return self.tasklist[0]
    
    def mark_complete(self):
        if len(self.tasklist) == 0:
            return None
        return self.tasklist.pop(0)
    
    def save_file(self):
        with open(self.list, 'w') as file:
            for task in self.tasklist:
                file.write(repr(task)+ '\n')

    def __len__(self):
        return len(self.tasklist)
    
    def __iter__(self):
        self.n = 0 
        return self
    
    def __next__(self):
        if self.n >= len(self.tasklist):
            raise StopIteration
        task = self.tasklist[self.n]
        self.n += 1
        return task 
