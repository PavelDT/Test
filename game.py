#create a game menu with 4 starting options
import sys

def quit_fn():
    print ("Exiting")
    # exiting through while condition makes this statement redundant
    sys.exit()
def save_fn():
    print("saved")
def new_fn():
    print("what would you like to play")
    board_array = ([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    for itemlist in board_array:
        print(itemlist[0], itemlist[1], itemlist[2])
def load_fn():
    print ("loading...")
#wrap map in a function so it can be used multiple times by the meny

# menu = {}
# menu["1"] = "New game"
# menu["2"] = "Save game"
# menu["3"] = "Load game"
# menu["4"] = "Quit"
# for menu_option in menu:
#     print(menu_option+ " " + menu[menu_option])

listmenu = []
listmenu.append("1 New game")
listmenu.append("2 Save game")
listmenu.append("3 Load game")
listmenu.append("4 Quit")
for menu_option in listmenu:
    print(menu_option)

# print(menu["1"])
# print(menu["2"])
# print(menu["3"])
# print(menu["4"])
user_input = 0
while user_input != 4:
    print("what would you like to do")
    user_input = int(input("what would you like to do next"))
    if user_input == 1:
        new_fn()
    elif user_input == 2:
        save_fn()
    elif user_input == 3:
        load_fn()
    elif user_input == 4:
        quit_fn()
    else:
        print ("invalid input")


