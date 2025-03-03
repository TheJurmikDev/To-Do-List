import time
import os

def data_get():
    with open('list.txt', 'r') as file:
        data = file.read()
    return data

def data_write(data):
    with open('list.txt', 'a') as file:
        file.write(f'{data}\n')

def data_remove(line_index_to_delete):
    with open('list.txt', 'r') as file:
        data = file.readlines()

    if 0 <= line_index_to_delete < len(data):
        del data[line_index_to_delete]

    with open('list.txt', 'w') as file:
        file.writelines(data)

def menu_main():
    os.system('cls')
    choice = input('''

    To Do List with memory :D
---------------------------------
|                               |
|     1. Add something          |
|     2. Remove something       | 
|     3. See whats inside       |
|                               |
---------------------------------''')

    if choice == '1':
        time.sleep(1)
        menu_add()
    elif choice == '2':
        time.sleep(1)
        menu_remove()
    elif choice == '3':
        time.sleep(1)
        menu_see()
    else:
        print('''

>> Wrong CHoice !!!''')
        time.sleep(1)
        menu_main()

def menu_remove():
    os.system('cls')
    print('#Note, the first line is 0')
    line_to_delete = input('What line do you want to remove? ')
    line_to_delete = int(line_to_delete)
    data_remove(line_to_delete)
    choice = input('ToDo list has been removed, press enter to continue')
    if choice:
        time.sleep(1)
        menu_main()
    else:
        time.sleep(1)
        menu_main()


def menu_add():
    os.system('cls')
    data = input('What do you want to add? ')
    data_write(data)
    choice = input('ToDo list has been added, press enter to continue')
    if choice:
        time.sleep(1)
        menu_main()
    else:
        time.sleep(1)
        menu_main()


def menu_see():
    os.system('cls')
    data = data_get()
    choice = input(f'''

------------------------------------------------------------------
{data}
------------------------------------------------------------------
                Press enter to continue..''')
    if choice:
        time.sleep(1)
        menu_main()
    else:
        time.sleep(1)
        menu_main()

menu_main()