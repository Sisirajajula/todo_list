import functions

while True:
    user_action = input("Enter add, show, edit , complete or exit: ")
    # Strip the string of any white spaces using strip method.
    user_action = user_action.strip()
    # Checking if user_action is 'add'
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()
        # Appending new elements to copied file items.
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        """ Method 1: To remove extra "\n" while printing todos. Edit each element in todos
        list using for loop. 
        
        new_todos = []
        for item in todos:
            new_item = item.strip("\n")
            new_todos.append(new_item)
            
        Method 2: list comprehensation method to remove extra newline.
        new_todos = [item.strip("\n") for item in todos]"""

        # enumerate function with iterable object as input.
        for index, item in enumerate(todos):
            item = item.strip("\n")
            # F formatting
            row = f"{index + 1}--{item}"
            print(row)
    elif user_action.startswith("edit"):
        # type conversion from string to int using int() function
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the changed todo: ") + "\n"
            todos[index] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Command is invalid. enter edit and then a number.")
            continue
        except IndexError:
            print("No item with that index")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            # removal of element of a particular index using pop method.
            index = number - 1
            todos = functions.get_todos()

            remove_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {remove_todo} was removed from the list."
            print(message)
        except IndexError:
            print("No item with that index")
            continue
    elif user_action.startswith("exit"):
        break
    # default case where it executes when all other cases fail.
    else:
        print("Unexpected input entered.")
