# PERSONAL FINANCE MANAGER
#### Description:

This is my Final Project for CS50's Introduction to Programming with Python. My project is a simple yet effective command-line tool called "Personal Finance Manager".

The primary goal of this application is to help users track their daily expenses and incomes in a structured way. In today's world, managing finances is crucial, and I wanted to create a tool that is lightweight and easy to use without the need for a complex GUI.

#### Project Structure:
The project consists of several key components:

1. **project.py**: This is the main script that runs the application. It contains the `main` function which handles the user interface and input loop. It also contains three main helper functions:
    - `add_transaction`: This function validates user input and adds a new record to the data list.
    - `calculate_balance`: This function iterates through all recorded transactions to provide a real-time total.
    - `format_currency`: This ensures that the output is always displayed in a professional monetary format ($X,XXX.XX).

2. **test_project.py**: To ensure the reliability of the core functions, I implemented a suite of tests using the `pytest` framework. Each function in the main script is tested against various edge cases, such as invalid numeric inputs or empty lists.

3. **requirements.txt**: This file lists any external dependencies. For this basic version, I focused on using Python's robust standard library, but the project is designed to be easily extensible with libraries like `pandas` or `tabulate` in the future.

#### How it works:
When the user starts the program, they are greeted with a simple prompt. They can choose to:
- **Add**: Input a description of an item and its cost (positive for income, negative for expense).
- **Show**: View the current calculated balance formatted as currency.
- **Exit**: Close the program safely.

#### Challenges and Learning:
During the development of this project, I faced challenges regarding input validation. I had to ensure that if a user entered a string instead of a number for the amount, the program wouldn't crash. This allowed me to practice exception handling (`try-except` blocks) in a real-world scenario. I also learned the importance of separating logic from the user interface, which made writing the unit tests much easier.

In the future, I plan to add a feature to save these records into a CSV file automatically so that the data persists even after the program is closed.
