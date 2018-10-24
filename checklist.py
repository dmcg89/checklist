# checklist

checklist = []

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# found color for python 2.7!!! doesnt work for python3
# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')
#
# print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
# print_red_on_cyan('Hello, World!')
# print_red_on_cyan('Hello, Universe!')


def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):

    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number?")
        item_index = int(item_index)
        print(checklist[item_index])
        read(item_index)

    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "U" or function_code == "u":
        input_item = user_input("Input item:")
        input_index = int(user_input("Index Number?"))
        update(input_index, input_item)

    elif function_code == "D" or function_code == "d":
        input_item = int(user_input("Index Number?"))
        destroy(input_item)

    elif function_code == "Q" or function_code == "q":
        return False

    else:
        print("Unknown Option")

    return True

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, D for delete, U to update, and Q to quit: ")
    running = select(selection)
