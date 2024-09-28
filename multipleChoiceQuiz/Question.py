# Define the Question class to represent each question in the quiz
class Question:
    # The constructor (__init__) initializes the question prompt and the correct answer
    def __init__(self, prompt, answer):
        self.prompt = prompt  # Stores the question text or prompt
        self.answer = answer  # Stores the correct answer to the question


