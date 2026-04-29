'''
Name: Jacob Miranda & Daniel Puerto
Date: 4/29/26
Group: 17
Description:
'''


class Task:
    def _init_(self, desc, date, time):
        self.description = desc
        self.date = date #MM/DD/YYYY
        self.time = time #HH:MM

    def __str__(self):
        return f"{self.description} (Due: {self.date} at {self.time})"
    
    def __repr__(self):
        return f"{self.description}, {self.date}, {self.time}"
    
    def __lt__(self,other):
        m1, d1, y1 = map(int, self.date.split)
