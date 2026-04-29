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
        h1, min1 = map(int, self.time.split(':'))

        m2, d2, y2, = map(int, other.date.split('/'))
        h2, min2 = map(int, other.time.split(':'))

        if y1 != y2:
            return y1 < y2
        if m1 != m2:
            return m1 < m2 
        if d1 != d2:
            return d1 < d2 
        if h1 != h2:
            return h1 < h2
        if min1 != min2:
            return min1 < min2
        
        return self.description < other.description
