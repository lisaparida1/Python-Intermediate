from data import question_data


class Question:

    def __init__(self, first, question_no):
        self.first = first
        self.question_no = question_no

    def concate_ques(self):
        choice = input(f"Q{self.question_no}. {self.first} (True/False): ")
        return choice

