class QuizBrain:

    def __init__(self, choice1, second):
        self.choice1 = choice1
        self.second = second

    def check_input(self):
        if self.second == self.choice1:
            print("Your answer is right!")
            return True
        else:
            print("Your answer is wrong!")
            print(f"The correct answer is {self.second}.\n")