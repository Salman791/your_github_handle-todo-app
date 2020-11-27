import sys

def print_usage():
    print("")
    print("$ todo")
    print("")
    print("Command Line Todo application")
    print("=============================")
    print("")
    print("Command line arguments:")
    print("      -l   Lists all the tasks")
    print("      -a   Adds a new task")
    print("      -r   Removes a task")
    print("      -c   Completes a task")

def list_tasks():
    print("")
    print("List All Elements")

def add_task(task):
    print("add " + task + " to the list")

print(sys.argv)

if len(sys.argv) == 1:
    print_usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    add_task(sys.argv[2])
