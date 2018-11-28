class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted[]

    def addStudents(self, stduent):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrade(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.allStudents:
            yield s

    def gradeReport(course):
        report = []
        for s in course.allStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report.append(str(s) + '\'s mean grade is' + str(average))
            except ZeroDivisionError:
                report.append(str(s) + 'has no grade')
        return '\n'.join(report)

#examples
ug1 = UG('Matt Damon', 2018)
ug2 = UG('Kathlyn Lewsinky', 2019)
g1 = Grad('Rucko Mattson')
g2 = Grad('Connery Havidson')

six00 = Grades()
six00.addStudents(g1)
six00.addStudents(ug2)
six00.addStudents(ug1)
six00.addStudents(g2)

six00.addGrade(g1, 100)
six00.addGrade(g2, 80)
six00.addGrade(ug1, 97)


print(gradeReport(six00))
