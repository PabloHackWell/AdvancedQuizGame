""" # quiz game -- HINA 

print("Welcome to the Quiz Game!\n")
score = 0

# Question 1
print("Q1: What is the capital of France?")
print("A. Berlin")
print("B. Madrid")
print("C. Paris")
print("D. Rome")
ans1 = input("Enter your answer (A/B/C/D): ").upper()

if ans1 == "C":
    print("Correct!\n")
    score += 1
elif ans1 in ["A", "B", "D"]:
    print("Wrong! The correct answer was C\n")
else:
    print("Invalid choice! No points awarded.\n")

# Question 2
print("Q2: Which language is primarily used for AI?")
print("A. Python")
print("B. C++")
print("C. Java")
print("D. HTML")
ans2 = input("Enter your answer (A/B/C/D): ").upper()

if ans2 == "A":
    print("Correct!\n")
    score += 1
elif ans2 in ["B", "C", "D"]:
    print("Wrong! The correct answer was A\n")
else:
    print("Invalid choice! No points awarded.\n")

# Question 3
print("Q3: What is 5 + 7?")
print("A. 10")
print("B. 12")
print("C. 13")
print("D. 14")
ans3 = input("Enter your answer (A/B/C/D): ").upper()

if ans3 == "B":
    print("Correct!\n")
    score += 1
elif ans3 in ["A", "C", "D"]:
    print("Wrong! The correct answer was B\n")
else:
    print("Invalid choice! No points awarded.\n")

# Final Score
print("Quiz Over!")
print("Your final score is:", score, "out of 3") """

# QUIZ GAME -- ANUJ 

import random
import time

# -----------------------------
# Question Bank
# -----------------------------
questions = {
    "easy": [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        }
    ],
    "medium": [
        {
            "question": "Which data type is immutable?",
            "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            "answer": "D"
        },
        {
            "question": "What does OOP stand for?",
            "options": ["A. Object Oriented Programming", 
                        "B. Only Object Programming", 
                        "C. Object Oriented Process", 
                        "D. None"],
            "answer": "A"
        }
    ],
    "hard": [
        {
            "question": "Which method is used to add an element to a set?",
            "options": ["A. append()", "B. add()", "C. insert()", "D. push()"],
            "answer": "B"
        },
        {
            "question": "Which module is used for regular expressions?",
            "options": ["A. regex", "B. pyregex", "C. re", "D. pattern"],
            "answer": "C"
        }
    ]
}

# -----------------------------
# Quiz Function
# -----------------------------
def run_quiz():
    print("\n=== PYTHON QUIZ GAME ===")
    print("Select Difficulty: easy / medium / hard")
    
    level = input("Enter difficulty: ").lower()
    
    if level not in questions:
        print("Invalid difficulty! Defaulting to easy.")
        level = "easy"
    
    selected_questions = questions[level].copy()
    random.shuffle(selected_questions)  # Shuffle questions
    
    score = 0
    total_questions = len(selected_questions)
    
    for q in selected_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        start_time = time.time()
        answer = input("Your answer (A/B/C/D): ").upper()
        end_time = time.time()
        
        time_taken = end_time - start_time
        
        # Timer: 10 seconds limit
        if time_taken > 10:
            print("⏰ Time's up! You took too long.")
            continue
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! Correct answer:", q["answer"])
    
    print("\n=== Quiz Finished ===")
    print(f"Your Score: {score}/{total_questions}")
    print(f"Percentage: {(score/total_questions)*100:.2f}%")
    
    if score == total_questions:
        print("Excellent Performance!")
    elif score >= total_questions / 2:
        print("Good Job!")
    else:
        print("Keep Practicing!")

# -----------------------------
# Main Loop (Play Again Option)
# -----------------------------
while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break