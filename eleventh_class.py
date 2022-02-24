# class Student():
#     instructor = "Desmond"

#     def __init__(self, name, grade, stu_num):
#         self.name = name
#         self.grade = grade
#         self.stu_num = stu_num


#     def get_grade(self):
#         return self.grade




# student = Student(name="Thimzy", grade="C", stu_num="3911XYZ")
# student1 = Student(name="Zara", grade="A", stu_num="3915XYZ")

# print(student.name)
# print(student1.name)





# class Square():
    

#     def __init__(self, side_len):
#         self.types = side_len
#         self.area = side_len**2
#         self.perimeter = side_len*4


#     def get_area(self):
#         return self.area       




# square = Square(side_len=5)
# square1 = Square(side_len=12)

# print(square.side_len)
# print(square.area)
# print(square.perimeter)

# print(square1.side_len)
# print(square1.area)
# print(square1.perimeter)


# class Employee():

#     def __init__(self, name, salary, years):
#         self.name = name
#         self.salary = salary
#         self.years = years

#     @property
#     def bonus(self):
#         if self.years >= 5:
#             return self.salary*0.1
#         return 0


# class Supervisor(Employee):
#     def __init__(self, name, salary, years, branch):
#         self.branch = branch
#         super().__init__(name, salary, years)


# emp1 = Employee("Chidu", 250, 2)
# emp1 = Employee("Adeola", 500, 5)
# sup1 = Supervisor("Charles", 2500, 15, "Yaba")

# print(sup1.years, sup1.branch)



class Questions:
    def __init__(self, useranswer, correctanswer):
        self.useranswer = useranswer
        self.correctanswer = correctanswer

questions_ = [
    "What form of Buddhist mysticism and meditation is practiced in Japan?\n(a) Zen\n(b) Ben\n(c) Ken\n(d) Ven\n",
    "Which blood group does one have to accept the blood of any of the four groups?\n(a) A\n(b) B\n(c) AB\n(d) O\n",
    "What is the name of the criminal act relating to computer?\n(a) Fraud\n(b) Cybercrime\n(c) Yahoo Yahoo\n(d) 419\n",
    "The last letter of the Greek alphabet is?\n(a) Alpha\n(b) Omega\n(c) Beginner\n(d) End\n",
    "After Paris, which is the worlds largest primarily French-speaking city?\n(a) London\n (b) Istanbul\n(c) Kinshasa\n(d) Montreal\n",
]

questions = [
    Questions(questions_[0], "a"),
    Questions(questions_[1], "c"),
    Questions(questions_[2], "b"),
    Questions(questions_[3], "a"),
    Questions(questions_[4], "a"),
]

def quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.useranswer)
        if answer == question.correctanswer:
            score += 1
        print("You get " + str(score) + '/' + str(len(questions)) + "correct")

quiz(questions)


class QuizQuestion():
    num_questions = 0
    num_correct = 0
    question = ""
    correct_answer = ""

    def __init__(self, quest, options:list, answer):
        QuizQuestion.question = quest
        for ans in options:
            QuizQuestion.question+=f"\n{ans}"


        QuizQuestion.correct_answer = answer.upper()

    def __ask(self):

        while True:
            print(self.question)
            answer = input(">").upper()
            if answer in ["A","B", "C","D", "E"]:
                return answer
            print("\nInvalid answer. Please enter A, B, C, D, or E.\n")

    def check(self):
        QuizQuestion.num_questions+=1
        ans = self.__ask()
        if QuizQuestion.correct_answer == ans:
            QuizQuestion.num_correct+=1
            print("Correct")
        else:
            print("Incorrect")


    def result(self):
        print(f"{QuizQuestion.num_correct} correct our of {QuizQuestion.num_questions} question(s)")


q1 = QuizQuestion("What year was java created?", 
                  [
                    "A. 1982", 
                    "B. 1996",
                    "C. 1991",
                    "D. 1891",
                    "E. 1981",
],
                  "B")
q1.check()

q2 = QuizQuestion("Who invented Java?", 
                  [
                    "A. James Gosling", 
                    "B. Dennis Ritchie",
                    "C. Raj Reddy",
                    "D. Guido van Ross",
                    "E. Bill Joy"
],
                  "A")
q2.check()


q2.result()