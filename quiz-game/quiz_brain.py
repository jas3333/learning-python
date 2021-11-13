class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def more_questions(self):
        return self.question_number < len(self.question_list)
        
         
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number} {current_question.text} -- [Score: {self.score}/{len(self.question_list)}] -- (true/false?) ")
        self.check_answer(user, current_question.answer)


    def check_answer(self, user, current_answer):
        if user.lower() == current_answer.lower():
            print("\nThat is correct!")
            self.score += 1
        else:
            print("\nThat is incorrect!")
        print(f"\nThe answer was: {current_answer}.")
