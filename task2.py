import csv
import os

# File path for the CSV
CSV_FILE_PATH = 'budget_data.csv'


def initialize_csv():
    try:
        with open(CSV_FILE_PATH, 'r') as file:
            pass  # File exists, do nothing
    except FileNotFoundError:
        with open(CSV_FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['type', 'category', 'amount', 'remaining_budget'])




def add_income_to_csv(amount, remaining_budget):
    with open(CSV_FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['income', '', str(amount), 'remaining_budget', str(remaining_budget)])


def add_expense_to_csv(category, amount, remaining_budget):
    with open(CSV_FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['expense', category, str(amount), 'remaining_budget', str(remaining_budget)])

     

def load_data_from_csv():
    try:
        with open(CSV_FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            data = {'income': 0, 'expenses': [], 'remaining_budget': 0}
            for row in reader:
                if 'type' in row and row['type'] == 'income':
                    data['income'] += float(row['amount'])
                    if 'remaining_budget' in row:
                        data['remaining_budget'] = float(row['remaining_budget'])
                elif 'type' in row and row['type'] == 'expense':
                    data['expenses'].append({
                        'category': row['category'],
                        'amount': float(row['amount']),
                        'remaining_budget': float(row['remaining_budget']) if 'remaining_budget' in row else 0
                    })
            return data
    except FileNotFoundError:
        return {'income': 0, 'expenses': [], 'remaining_budget': 0}        

def show_menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. Exit")
 
def add_income(data):
    amount = float(input("Enter income amount: "))
    data['income'] += amount

    # Calculate remaining budget
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses

    add_income_to_csv(amount, remaining_budget)
    print(f"Income of ${amount} added successfully!")
       

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})

    # Calculate remaining budget
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses

    add_expense_to_csv(category, amount, remaining_budget)
    print(f"Expense of ${amount} in the category {category} added successfully!")

    

def view_budget(data):
    print("\n----- Budget Overview -----")
    print(f"Total Income: ${data['income']}")
    
    if not data['expenses']:
        print("No expenses recorded.")
    else:
        print("\n----- Expenses -----")
        for expense in data['expenses']:
            print(f"{expense['category']}: ${expense['amount']}")

        total_expenses = sum(expense['amount'] for expense in data['expenses'])
        remaining_budget = data['income'] - total_expenses

        print("\n----- Budget Summary -----")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Remaining Budget: ${remaining_budget}")

def main():
    data = load_data_from_csv()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            print(data)  # Debugging line to print data dictionary
            view_budget(data)
        elif choice == '4':
            print("Exiting Budget Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    initialize_csv()
    main()
