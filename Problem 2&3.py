class PartTimeStudent:
    count = 0  

    def __init__(self, name, student_id):
        self.name = name 
        self.student_id = student_id  
        PartTimeStudent.count += 1  

    @staticmethod
    def get_count():
        return PartTimeStudent.count  


class SchoolSystem:
    def __init__(self): 
        self.students = []
        self.lecturers = []
        self.projects = []

    def add_student(self, student):
        if len(self.students) < 10:  
            self.students.append(student)  

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:  
            self.lecturers.append(lecturer)

    def add_project(self, project):
        if len(self.projects) < 10: 
            self.projects.append(project)


if __name__ == "__main__":
    
    s1 = PartTimeStudent("Alice", "PTS001")
    s2 = PartTimeStudent("Bob", "PTS002")
    s3 = PartTimeStudent("Charlie", "PTS003")

    system = SchoolSystem()
    system.add_student(s1)  
    system.add_student(s2)  

    print("Số lượng sinh viên bán thời gian đã tạo:", PartTimeStudent.get_count())

