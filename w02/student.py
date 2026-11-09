class Student:
    def __init__(self,sid,fullname):
        self.sid = sid
        self.fullname = fullname
        
    def __str__(self):
        return f"{self.sid} {self.fullname}"
    