print("Here, you need to answer 5 questions answer and you have 3 lifes\nif you will be answered all the questions then you will win otherwise you loss")
username = input("\nplease enter your username or go with guest:")
life = 3
True_ = ["T", "t"]
False_ = ["F", "f"]
answers = True_ + False_

print(f"Welcome {username} you have {life} life and for True please answer in {True_} and for False answer in {False_}")

# (question_text, is_true_answer)
questions = [
    ("Python is a high-level programming language", "T"),
    ("In Python, the value of 5 > 3 is True", "T"),
    ("The boolean values in Python are written as true and false", "F"),
    ("The expression 10 == 5 evaluates to True in Python", "F"),
    ("In Python, comparison operators can be used to produce True/False results", "T")
]

while life >0:
    correct = 0
    for question, answer in questions:
        while True:
            print(question)
            ans = input("Your Answer:")
            if ans in answers:
                if ans.upper() == answer:
                    correct += 1
                break
            else:
                print("print answer in T/t or f/f")
    if correct == len(questions):
        print(f"Congrats to you {username} your score is {correct} out of {len(questions)}")
    elif life > 1:
        life -=1
    else:
        print("Game over")
        break