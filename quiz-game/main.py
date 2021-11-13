from question import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


for index in question_data:
    question_text = index["text"]
    question_answer = index["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


while quiz.more_questions():
    quiz.next_question()


print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")
