import uuid

class Question:
    def __init__(self, text):
        self.question_id = str(uuid.uuid4())
        self.text = text
        self.answers = []

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, value):
        self._question_id = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, value):
        self._answers = value

    def add_answer(self, answer):
        # TODO: Validate that only one is correct
        self.answers.append(answer)

    def validate(self):
        # TODO: Add validation logic
        pass
