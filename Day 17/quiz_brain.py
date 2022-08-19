class Quiz:
    def __init__(self, quiz_bank):
        self.bank = quiz_bank
        self.questionCount = 0
        self.totalScore = 0


    def askQuestion(self):
        question = self.bank[self.questionCount]
        self.questionCount += 1
        print("Q." + str(self.questionCount) + ": " + question.text + "True/False?")
        u_ans = input()
        self.checkAnswer(u_ans, question.answer)


    def stillHasQuestion(self):
        if self.questionCount >= len(self.bank):
            return False
        else:
            return True


    def checkAnswer(self, u_ans, q_ans):
        if u_ans.lower() == q_ans.lower():
            self.totalScore += 1
            print("Correct!")
            self.printScore()
        else:
            print("Incorrect!")
            self.printScore()

        print(f"Answer is: {q_ans}")

    def printScore(self):
        print(f"Score: {self.totalScore} / {self.questionCount}")

    def printFinalScore(self):
        print("Final Score: ")
        print(f"{self.totalScore} Correct")
        print(f"{len(self.bank) - self.totalScore} Incorrect")
