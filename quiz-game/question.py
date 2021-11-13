class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


    def name_input(self):
        char = input("Enter your name >> ")
        self.answer = char


    def display_q(self):
        return f"Hello {self.answer}."
