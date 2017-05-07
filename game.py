#create a game menu with 4 starting options
import sys
from random import randint

def innitialise_grid():
    board_array = []
    counter = 0
    while counter < 3:
        # blank_list[0]
        board_array.append([])
        new_counter = 0
        while new_counter < 3:
            board_array[counter].append(randint(0, 1))  # this is how rng function is made in this case between 0-1
            new_counter = new_counter + 1
        counter = counter + 1
    return board_array
def check_ship(board):
    y = int(input("x coordiante "))
    x = int(input("y coordinate "))
    if x > 2 or y > 2 or x < 0 or y < 0:
        print("invalid input")
    else:
        if board[x][y] == 1:
            print("ship found")
            board[x][y] = 0
        else:
            print("no ship found")
def quit_fn():
    print ("Exiting")
    # exiting through while condition makes this statement redundant
    sys.exit()
def save_fn():
    print("saved")
def new_fn():
    print("Starting new game")
    gameover = False
    board_array = innitialise_grid()

    for itemlist in board_array:
        print(itemlist[0], itemlist[1], itemlist[2])

    while gameover == False:
        check_ship(board_array)
        game_over_after_this_turn = True # we assume game is over, and then check if it is
        #if 1 in board_array[0] or 1 in board_array[1] or 1 in board_array[2]:
        for list in board_array:
            if 1 in list:
                game_over_after_this_turn = False


        if game_over_after_this_turn == True:
            print("you win!")
            gameover = True
        else:
            print("move again")

        # debug display grid.
        for ship in board_array:
            print(str(ship[0]) + " " + str(ship[1]) + " " + str(ship[2]))


def load_fn():
    print("loading...")
#wrap map in a function so it can be used multiple times by the meny

# Begin to conver the board into a hidden field where 1/0 are displayed as "?" and revealed as Xif ship was present and
# struck or 0 if no ship was present once that spot is selected

listmenu = []
listmenu.append("1 New game")
listmenu.append("2 Save game")
listmenu.append("3 Load game")
listmenu.append("4 Quit")


# print(menu["1"])
# print(menu["2"])
# print(menu["3"])
# print(menu["4"])
user_input = 0
while user_input != 4:
    for menu_option in listmenu:
        print(menu_option)
    user_input = int(input("what would you like to do next: "))
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


