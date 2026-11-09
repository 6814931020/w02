class Subject:
    def __init__(self, subjectCode, subjectName, subjectUnit):
        self.subjectCode = subjectCode
        self.subjectName = subjectName
        self.subjectUnit = subjectUnit

    def __str__(self):
        return f"{self.subjectCode}, {self.subjectName}, {self.subjectUnit} หน่วยกิต"