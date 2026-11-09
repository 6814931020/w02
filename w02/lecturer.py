class Lecturer:
    def __init__(self, fullname):
        self.fullname = fullname

    def __str__(self):
        return f"Lecturer : {self.fullname}"