current_string = ""
undo_stack = []
redo_stack = []

def Add(string_command):
    global current_string, undo_stack, redo_stack
    string_command = string_command[1:].lstrip()
    undo_stack.append(current_string)
    current_string += string_command.rstrip
    redo_stack.clear()
    return current_string

def Delete(string_command):
    global current_string, undo_stack, redo_stack
    N = int(string_command[1:])
    undo_stack.append(current_string)
    if N > len(current_string):
        current_string = ""
    else:
        current_string = current_string[:-N]
    redo_stack.clear()
    return current_string

def Print_index(string_command):
    global current_string
    N = int(string_command[1:])
    if 0 <= N < len(current_string):
        return current_string[N]
    else:
        return ""

def Undo():
    global current_string, undo_stack, redo_stack
    if undo_stack:
        redo_stack.append(current_string)
        current_string = undo_stack.pop()
    return current_string

def Redo():
    global current_string, undo_stack, redo_stack
    if redo_stack:
        undo_stack.append(current_string)
        current_string = redo_stack.pop()
    return current_string

def BastShoe(string_command) -> str:
    command_num = int(string_command[0])
    if command_num == 1:
        return  Add(string_command)
    elif command_num == 2:
        return Delete(string_command)
    elif command_num == 3:
        return Print_index(string_command)
    elif command_num == 4:
        return Undo()
    elif command_num == 5:
        return Redo()
    else:
        return current_string
