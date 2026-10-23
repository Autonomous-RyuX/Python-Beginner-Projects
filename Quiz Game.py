questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kerala"],
        "answer": "b"
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "c"
    },
    {
        "question": "3. How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "c"
    },
    {
        "question": "4. Which language is used for Python programming?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "a"
    },
    {
        "question": "5. What is 10 * 5?",
        "options": ["A. 15", "B. 50", "C. 100", "D. 25"],
        "answer": "b"
    }
]

Marks = 0
print("====== WELCOME TO MY QUIZ GAME ======".center(50));
for A in questions:
    print( "\n" + A["question"])
    for B in A["options"]:
        print(B);
    
    User_Answer = input("Enter your answer (A/B/C/D): ").strip().lower()

    if User_Answer == A["answer"]:
        print("Correct Answer");
        Marks += 1
    else:
        print("Wrong Answer");

print("======= QUIZ COMPLETED ======".center(50));
print(f"Your Marks: {Marks}/{len(questions)}");
if Marks == len(questions):
    print("Excellent!! Keep Going");
elif Marks >= 3:
    print("Good, Keep Learning");
else:
    print("Work Harder");
