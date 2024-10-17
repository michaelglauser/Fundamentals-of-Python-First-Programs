#Python Programs Chapter 9 Project 2
#Take project 1 and place several Student objects into a list, and shuffle it. 
#Then run the sort method with this list and display all of the students' information.



import random

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
        """Returns self < other, with respect
        to names."""
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

    studentList = []
    for count in reversed(range(5)):
        s = studentClass("Name" + str(count + 1), 10)
        studentList.append(s)


    random.shuffle(studentList)

    for i in studentList:
        print(i)

    studentList.sort()

    for i in studentList:
        print(i)

if __name__ == "__main__":
    main()