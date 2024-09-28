# Import the Question class from the Question module
from Question import Question

# Define a list of question prompts with multiple-choice options
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",  # First question about apples
    "What color are bananas?\n(a) Green\n(b) Red\n(c) Yellow\n\n",        # Second question about bananas
    "What color are strawberries?\n(a) Blue\n(b) Red\n(c) Purple\n\n"     # Third question about strawberries
]

# Create instances of the Question class for each question, with the corresponding correct answer
questions = [
    Question(question_prompts[0], "a"),  # The correct answer for apples is "a" (Red/Green)
    Question(question_prompts[1], "c"),  # The correct answer for bananas is "c" (Yellow)
    Question(question_prompts[2], "b")   # The correct answer for strawberries is "b" (Red)
]

# Define a function that runs the quiz and checks answers
def run_test(questions):
    score = 0  # Initialize the score to 0
    # Loop through each question in the questions list
    for question in questions:
        # Show the question prompt to the user and get their input
        answer = input(question.prompt)
        # Check if the user's answer matches the correct answer
        if answer == question.answer:
            score += 1  # Increment score by 1 if the answer is correct
    # Display the total score at the end of the quiz
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

# Run the quiz using the list of questions
run_test(questions)