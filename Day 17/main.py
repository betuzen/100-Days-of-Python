from data import question_data
from question_model import Question
from quiz_brain import Quiz

questionBank = []



def create_question_bank():
    for x in question_data:
        #print(x["text"] + " " + x["answer"])
        ques = x["text"]
        ans = x["answer"]
        question = Question(ques, ans)
        questionBank.append(question)


def main():
    flag = True
    create_question_bank()
    quizBrain = Quiz(questionBank)

    while (flag == True):
        quizBrain.askQuestion()
        flag = quizBrain.stillHasQuestion()

    quizBrain.printFinalScore()





main()
