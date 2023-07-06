class Person:
    	def __init__(self, firstName, lastName, idNumber):
		        self.firstName = firstName
		        self.lastName = lastName
		        self.idNumber = idNumber
	    def printPerson(self):
		    print("Name:", self.lastName + ",", self.firstName)
		    print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, n_first, l_last, id_num, score):
    #   Parameters:
        self.first = n_first
        self.last = l_last 
        self.Id = id_num 
        self.score = score 
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    
    # Write your constructor here
    def printPerson(self):
        person = f"{self.last}, {self.first}"
        Id_ = f"{self.Id}"
        print(f"Name: {person}"+"\n"+ f"ID: {Id_}")
        
    #   Function Name: calculate
    def calculate(self):
        grades = self.score
        sum = 0
        for i in grades:
            sum += i 
        marks = sum / len(grades)
    #   Return: A character denoting the grade.
        if marks >= 90 and marks <= 100:
            letter = "O"
            return letter
        elif marks >= 80 and marks < 90:
            letter = "E"
            return letter
        elif marks >= 70 and marks < 80:
            letter = "A"
            return letter
        elif marks >= 50 and marks < 70:
            letter = "P"
            return letter
        elif marks >= 40 and marks < 55:
            letter = "D"
            return letter
        else:
            letter = "T"
            return letter
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())