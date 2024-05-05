import sqlite3
import datetime

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create expenses table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY, amount REAL, description TEXT, date TEXT)''')
conn.commit()

def add_expense(amount, description, date):
    """Add a new expense to the database."""
    c.execute("INSERT INTO expenses (amount, description, date) VALUES (?, ?, ?)", (amount, description, date))
    conn.commit()

def view_expenses():
    """View all expenses stored in the database."""
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    if expenses:
        for expense in expenses:
            print(expense)
    else:
        print("No expenses found.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            add_expense(amount, description, date)
            print("Expense added successfully.")

        elif choice == '2':
            print("\nAll Expenses:")
            view_expenses()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
