user_input: str = 'random'
# add data into a list
data = list()

# function displays the Main Menu
def menu_list():
    print("")
    print("Todo Application 1.0")
    print("=============================")
    print("")
    print("Main Menu:")
    print("      1. Add a new task")
    print("      2. List all the tasks")
    print("      3. Mark as done")
    print("      4. Quit")

# App starts by displaying the main menu
menu_list()

while (True):
# user inputs option from main menu
    user_input = input("Please enter your choice from the menu: ")
# if user selects 1, they add a new task
    if user_input == '1':
        task = input("Add new task: ")
        data.append(task)
        print("New task: ", task)
# if user selects 2, they print the entire to-do list
    elif user_input == '2':
        print("To-do list: ")
        for task in data:
            print(task)
# if user selects 3, they mark a previous task as done
    elif user_input == '3':
        task = input("Mark a task as done: ")
        if task in data:
            data.remove(task)
            print("Marked as done: ", task)
# If the task input by the user doesn't exist, the user is alerted
        else:
            print("No such task in the list!")
# If user inputs 4, they quit the app
    elif user_input == '4':
        exit()
# If user inputs an option not present in the main menu, they are alerted with the following message
    else:
        print("Only select options from the Main Menu!")
