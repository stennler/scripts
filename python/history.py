import readline
# Prints the history up to a certain max (max is optional)
def h(max_history=0):
    history_length = readline.get_current_history_length()
    max_length = history_length if max_history==0 else min(max_history, history_length)
    for i in range(max_length):
        print readline.get_history_item(i + 1)
