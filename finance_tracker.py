# welcomes the user to the personal finance tracker
def welcome_user():
    print("Welcome to the Personal Finance Tracker!")


# adds an expense to a given dictionary of expenses
def add_expense(expenses):
    
    # prompts user to enter an expense description
    description = input("Enter expense description: ")

    # ensures the description entered is not empty, reprompts user until the input is a valid description
    while not description:
        description = input("Description cannot be blank. Please enter a description: ")
    
    # prompts user to enter an expense category
    category = input("Enter category: ")
    
    # ensures the category entered is not empty, reprompts user until the input is a valid category
    while not category:
        category = input("Category cannot be blank. Please enter a category: ")
    
    # loops until the user enters a positive numerical expense amount
    while True:
        try: 
            # prompts user to enter an expense amount
            amount = float(input("Enter amount: "))

            # ensures the amount entered is not blank
            if not amount:
                print("Amount cannot be blank.")
                continue
            
            # checks to make sure the amount is positive
            if amount <= 0:
                print("Amount must be greater than $0.")
                continue
                
            break

        except ValueError:
            print("Invalid value. Please enter a numerical amount")

    # creates a tuple with the expense description and amount
    expense = (description, amount)

    # if the category does not already exist in the dictionary, create the key and set its value to an empty list
    if category not in expenses:
        expenses[category] = []
    
    # append the tuple to the list of expenses value) for the given category (key) in the expenses dictionary
    expenses[category].append(expense)

    # informs that the expense was added or not
    print("Expense added successfully!")


# prints all categories and their expenses
def view_expenses(data):

    # prints a message and returns if there are no expenses
    if not data:
        print("No expenses have been recorded yet.")
        return

    # iterates through the dict to display each expense's category, description, and amount
    for category, expense in data.items():
        print(f"Category: {category}")
        for description, amount in expense:
            print(f"    - {description}: ${amount:.2f}")


# shows the total amount per category
def view_summary(data):

    # prints a message and returns if there are no expenses
    if not data:
        print("No expenses have been recorded yet.")
        return
    
    print("Summary:")
    # iterates through each expense, totals up the amount in each category, and prints it
    for category, expenses in data.items():
        category_total = 0
        for _, amount in expenses:
            category_total += amount
        
        print(f"{category}: ${category_total:.2f}")


# uses a menu-driven approach to allow users to choose what they'd like to do
def menu_logic():
    print("What would you like to do? 1. Add Expense 2. View All Expenses 3. View Summary 4. Exit")
    
    # prompts users to enter an option until their input is valid
    while True:
        try: 
            # prompts users to enter an option
            option = int(input("Choose an option: "))

            # checks to see if the option is 1, 2, 3, or 4
            if option in [1, 2, 3, 4]:
                return option
            
            # option is not 1, 2, 3, or 4, so it is invalid
            else:
                print("Invalid option. Please enter a number 1-4.")
        
        # catches ValueErrors for non-int inputs
        except ValueError:
            print("Invalid value. Please enter a number 1-4.")


# main function to combine all the logic and call the functions above accordingly
def main():
    welcome_user()
    expenses = {}

    # loops until user exits the personal finance tracker
    while True:
        option = menu_logic()
        if option == 1:
            add_expense(expenses)
        elif option == 2:
            view_expenses(expenses)
        elif option == 3:
            view_summary(expenses)
        elif option == 4:
            print("Goodbye!")
            break


# ensures main() runs when this script is executed
if __name__ == "__main__":
    main()