# Smart Expense Tracker (Python + MySQL)

A simple console-based Expense Tracker application built using Python and MySQL. This project helps users manage their monthly income and expenses, view summaries, and avoid duplicate entries using proper database constraints.

## Features
- Add Monthly Income (Month + Year based)
- Prevent Duplicate Income for the Same Month & Year
- Update Existing Income
- Add Expenses
- Store Data Securely in MySQL
- Show Summary of Income vs Expenses
- Input Validation (Number checks, range checks)

## Technologies Used
- Python 3
- MySQL
- PyMySQL (Database Connector)

## Database Structure

income_table:
id (INT, Primary Key)
month_number (INT)
year (INT)
income_amount (INT)
Unique Constraint: (month_number, year)

expenses_table:
id (INT, Primary Key)
month_number (INT)
year (INT)
amount (INT)
category (VARCHAR(50))

## How to Run the Project

1. Clone the repository:
git clone https://github.com/your-username/smart-expense-tracker.git

2. Install dependency:
pip install pymysql

3. Create database in MySQL:
CREATE DATABASE expenses_tracker;

4. Create tables as per above structure.

5. Run the application:
python main.py

## Project Purpose
This project is designed for learning Python-MySQL integration, understanding CRUD operations, practicing database constraints, and building a real-world mini project.

## Future Improvements
- Delete Income & Expenses
- Category-wise Expense Summary
- Monthly & Yearly Reports
- Graphical Interface (GUI)
- Export Data to Excel/PDF

## Author
Manoj Kumar k 
MCA Student & Aspiring Software Developer

If you like this project, give one star