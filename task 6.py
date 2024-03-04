import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def ask_question(question, options, correct_option):
    speak(question)
    for i, option in enumerate(options, start=1):
        speak(f"{i}. {option}")

    user_answer = int(input("Enter your choice (1, 2, 3, ...): "))
    if user_answer == correct_option:
        speak("Correct! Well done.")
        return True
    else:
        speak("Incorrect. Better luck next time.")
        return False

def play_quiz():
    speak("Welcome to the Quiz Game!")
    
    score = 0

    # Question 1
    question1 = "What is the capital of France?"
    options1 = ["Paris", "Berlin", "London"]
    correct_option1 = 1
    if ask_question(question1, options1, correct_option1):
        score += 1

    # Question 2
    question2 = "Which programming language is known for its readability?"
    options2 = ["Java", "Python", "C++"]
    correct_option2 = 2
    if ask_question(question2, options2, correct_option2):
        score += 1

    # Question 3
    question3 = "What is the largest planet in our solar system?"
    options3 = ["Earth", "Jupiter", "Mars"]
    correct_option3 = 2
    if ask_question(question3, options3, correct_option3):
        score += 1

    speak(f"Your final score is {score} out of 3. Thank you for playing!")

if __name__ == "__main__":
    play_quiz()
