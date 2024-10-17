#Python Programs Chapter 9 Project 1
#Add three methods to the Student(s) class that compare two Student(s) objects. 
#One method should test for equality. A second method should test for less than. 
#The third method should test for greater than or equal to.


class studentClass(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))


    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __eq__(self, other):

        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name

def main():
    student = studentClass("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

if __name__ == "__main__":
    main()