import uuid

class Answer:
    def __init__(self, text, is_correct):
        self.answer_id = str(uuid.uuid4())
        self.text = text
        self.is_correct = is_correct

    @property
    def answer_id(self):
        return self._answer_id

    @answer_id.setter
    def answer_id(self, value):
        self._answer_id = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def is_correct(self):
        return self._is_correct

    @is_correct.setter
    def is_correct(self, value):
        self._is_correct = value