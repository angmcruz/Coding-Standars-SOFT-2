class student:
    def __init__(s, id, name):
        s.id = str(id)
        s.name = str(name)
        s.gradez = []
        s.isPassed = True
        s.honor = False

    def addGrades(self, g):
        if not str(g).isdigit():
            print("Grade must be a number")
        else:
            grade = int(g)
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100")
            else:
                self.gradez.append(grade)

    def calcAvg(self):
        total = 0
        letra = ""
        for grade in self.gradez:
            total += grade
        if len(self.gradez) == 0:
            avg = 0
        else:   
            avg = total / len(self.gradez)

        if avg >= 90:
            letra = "A"
        elif avg >= 80:
            letra = "B"
        elif avg >= 70:
            letra = "C"
        elif avg >= 60:
            letra = "D"
        else:
            letra = "F"
            self.isPassed = False

        return avg, letra

    def checkHonor(self):
        if self.calcAvg()[0] > 90:
            self.honor = True

    def deleteGrade(self, index):
        if index < 0 or index >= len(self.gradez):
            print("Failed to delete grade, out of range")
        else:
            del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + str(self.calcAvg()[0]))
        if self.isPassed:
            print("Student has passed")
        else:
            print("Student has not passed")


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcAvg()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


if __name__ == "__main__":
    startrun()
