from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

count = 0
question_no = 0
for question in question_data:
    first = question["text"]
    second = question["answer"]
    question_no += 1
    ques = Question(first, question_no)
    choice1 = ques.concate_ques()
    quiz = QuizBrain(choice1, second)
    r = quiz.check_input()
    if r==True:
        count += 1
    print(f"Your Score is {count}/{question_no}\n")


