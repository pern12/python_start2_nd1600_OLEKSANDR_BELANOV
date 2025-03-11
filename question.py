# question.py
class Question():
    # variants, question, correctAnswer
    def __init__(self, question, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_ans1 = wrong_answer1
        self.wrong_ans2 = wrong_answer2
        self.wrong_ans3 = wrong_answer3
        self.correct_count = 0
        self.wrong_count = 0

    def variants(self):
        return [self.correct_answer, self.wrong_ans1, self.wrong_ans2, self.wrong_ans3]

    def check_answer(self, answer):
        correct =  answer == self.correct_answer
        if correct:
            self.correct_count += 1
        else: 
            self.wrong_count += 1
        return correct
    
questions = [
    Question("Яблуко", "apple", "car", "window", "carpet"),
    Question("Дерево", "tree", "three", "move", "good"),
    Question("Виноград", "grapes", "pineapple", "woodpecker", "light"),
    Question("Людина", "human", "hike", "zebra", "moonshine")
]