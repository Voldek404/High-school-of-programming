current_string = ""
undo_stack = [current_string]
redo_stack = []
last_action = 0

def Add(string_command):
    global current_string, undo_stack, redo_stack, last_action
    if last_action in (4, 5):
        undo_stack = [current_string]
        redo_stack = []
    current_string += string_command[2:]
    undo_stack.append(current_string)
    last_action = 12
    return current_string

def Delete(string_command):
    global current_string, undo_stack, redo_stack, last_action
    if last_action in (4, 5):
        undo_stack = [current_string]
        redo_stack = []
    delete_count = int(string_command[2:])
    current_string = current_string[:-delete_count] if delete_count <= len(current_string) else ''
    undo_stack.append(current_string)
    last_action = 12
    return current_string

def Print_index(string_command):
    index = int(string_command[2:])
    return current_string[index] if 0 <= index < len(current_string) else ''

def Undo():
    global current_string, undo_stack, redo_stack, last_action
    if len(undo_stack) > 1:
        redo_stack.append(current_string)
        undo_stack.pop()
        current_string = undo_stack[-1]
    last_action = 4
    return current_string

def Redo():
    global current_string, undo_stack, redo_stack, last_action
    if redo_stack:
        current_string = redo_stack.pop()
        undo_stack.append(current_string)
    last_action = 5
    return current_string

def BastShoe(string_command) -> str:
    if string_command.startswith('1'):
        return Add(string_command)
    elif string_command.startswith('2'):
        return Delete(string_command)
    elif string_command.startswith('3'):
        return Print_index(string_command)
    elif string_command.startswith('4'):
        return Undo()
    elif string_command.startswith('5'):
        return Redo()
    else:
        return current_string
