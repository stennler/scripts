import os
import readline


def h(max_history=0):
    """Prints the history up to a certain max (max is optional)"""
    history_length = readline.get_current_history_length()
    end = history_length
    start = 0
    if max_history > 0:
        start = history_length - min(max_history, history_length)
    num_items = end-start
    for i in range(num_items):
        actual = num_items-i
        offset = " "
        if actual < 100:
            offset = "  "
        if actual < 10:
            offset = "   "
        print("%d:%s%s" % (actual, offset, readline.get_history_item(start + i + 1)))  # nopep8
