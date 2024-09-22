import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from models.question import Question
from models.quiz_result import QuizResult
from database import SessionLocal, init_db

def main_menu():
    while True:
        print("\n1. Create User")
        print("2. Create Question")
        print("3. Take Quiz")
        print("4. View Results")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            create_question()
        elif choice == '3':
            take_quiz()
        elif choice == '4':
            view_results()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_user():
    session = SessionLocal()
    username = input("Enter username: ")
    user = User(username=username)
    session.add(user)
    session.commit()
    print(f"User {username} created!")
    session.close()

def create_question():
    session = SessionLocal()
    question_text = input("Enter the question: ")
    correct_answer = input("Enter the correct answer: ")
    options = input("Enter the answer options (comma-separated): ")
    question = Question(question_text=question_text, correct_answer=correct_answer, options=options)
    session.add(question)
    session.commit()
    print(f"Question '{question_text}' created!")
    session.close()

def take_quiz():
    session = SessionLocal()
    user_id = int(input("Enter your user ID: "))
    questions = session.query(Question).all()
    score = 0

    for question in questions:
        print(f"\n{question.question_text}")
        print(f"Options: {question.options}")
        answer = input("Your answer: ")

        if answer == question.correct_answer:
            score += 1

    result = QuizResult(user_id=user_id, score=score)
    session.add(result)
    session.commit()
    print(f"You scored {score}/{len(questions)}!")
    session.close()

def view_results():
    session = SessionLocal()
    results = session.query(QuizResult).all()
    # for result in results:
    #     print(f"User {result.user.username} scored {result.score} on {result.date_taken}")
    # session.close()
    for result in results:
        print(view_results)  # Print the result object to see if user is None
    if result.user:
        print(f"User {result.user.username} scored {result.score} on {result.date_taken}")
    else:
        print(f"Anonymous user scored {result.score} on {result.date_taken}")

def delete_user():
    session = SessionLocal()
    user_id = int(input("Enter user ID to delete: "))
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user.username} deleted!")
    else:
        print(f"User with ID {user_id} not found.")
    session.close()

if __name__ == "__main__":
    init_db()
    main_menu()
