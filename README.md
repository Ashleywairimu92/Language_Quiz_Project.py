# Language Learning Quiz App

## Overview

The **Language Learning Quiz App** is a command-line interface (CLI) application designed to help users improve their language skills by taking quizzes. Users can create profiles, answer questions, and track their progress over time. The app uses a SQLite database with SQLAlchemy ORM to manage users, questions, and quiz results.

## Features

- **User Management**: Create and delete user profiles.
- **Quiz Management**: Add new quiz questions with multiple answer options and correct answers.
- **Take Quizzes**: Users can take quizzes and their results are stored in the database.
- **View Results**: Users can view their quiz results and scores.
- **Command-Line Interface**: Navigate through the application using a CLI with interactive menus.
- **Input Validation**: Ensures valid user input and provides informative error messages.

## Project Structure

language_quiz/
│
├── models/
│   ├── user.py  # SQLAlchemy User model
│   ├── question.py  # SQLAlchemy Question model
│   └── quiz_result.py  # SQLAlchemy QuizResult model
│
├── cli/
│   └── quiz_cli.py  # Main CLI for quiz interaction
│
├── migrations/
│   └── ...  # Alembic migrations for the database
│
├── database.py  # SQLAlchemy database setup
├── Pipfile  # Pipenv for virtual environment and dependencies
└── README.md  # Project documentation
## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pipenv for managing the virtual environment
- SQLite (automatically installed with SQLAlchemy)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/language-quiz-app.git
   cd language-quiz-app
Install dependencies using Pipenv:

pipenv install
Activate the virtual environment:

pipenv shell
Set up the database: Initialize the database schema using Alembic:

alembic upgrade head


Usage

Run the CLI application by executing the following command:

python cli/quiz_cli.py


Main Menu Options:
  Create User: Add a new user to the quiz system.
  Create Question: Add a new quiz question with multiple options and a correct answer.
  Take Quiz: Take a quiz based on the stored questions. Your score will be saved.
  View Results: Display quiz results for all users.
  Delete User: Remove a user from the system.
  Exit: Exit the CLI application.

Example Workflow

 Create a User:
   Enter a username.
   The user will be created and stored in the database.
 Create a Quiz Question:
   Enter a question, correct answer, and options.
   The question will be stored for future quizzes.
 Take a Quiz:
   Select a user and take a quiz.
   Answer the questions, and your score will be recorded.
 View Quiz Results:
   View the scores for all users who have taken quizzes.
 Delete a User:
   Enter a user ID to remove a user from the system.

Database Schema

 The app uses three main tables:

  Users: Stores user profiles (username).
  Questions: Stores quiz questions, options, and correct answers.
  Quiz Results: Tracks users' quiz scores and the date when the quiz was taken.

Future Improvements

 Support for multiple-choice questions with randomization of answer order.
 Option to view individual user scores.
 User authentication and progress tracking.
 Add more complex validation for input and better error handling.

Contributing

 Fork the repository.
 Create your feature branch (git checkout -b feature/new-feature).
 Commit your changes (git commit -m 'Add new feature').
 Push to the branch (git push origin feature/new-feature).
 Open a pull request.

License

 This project is licensed under the MIT License


### Key Points in the README:
- **Overview**: Briefly describes the purpose of the app.
- **Features**: Highlights key features like user management, quizzes, and result viewing.
- **Project Structure**: Lists and explains important project files.
- **Getting Started**: Instructions to clone the repository, install dependencies, and set up the database.
- **Usage**: Explains how to run the CLI and the options available.
- **Database Schema**: Provides an overview of the tables used in the database.
- **Future Improvements**: Lists potential future features for the app.

This README can be modified as you progress through your project and add more features.