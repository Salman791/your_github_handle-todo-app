import sys

print(sys.argv)

if len(sys.argv) == 1:
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
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    print("")
    print("List All Elements")
