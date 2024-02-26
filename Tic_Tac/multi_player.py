from helpers import check_input_validility, winning_position
from accessories import print_tic_tac, colored_input

def multi_player_tracking(tic_code, p1_play_history, p2_play_history):
    player_1_input = "> Player 1: "
    user1 =colored_input(player_1_input, "GREEN").strip().lower()
    while not check_input_validility(user1, tic_code):
        print("Invalid Input, please eventer legal move")
        user1 = colored_input(player_1_input, "GREEN").strip().lower()

    for plate in tic_code:
        for position in plate:
            if user1 == position:
                plate[plate.index(position)] = "X"
                p1_play_history.add(user1)
                print_tic_tac(tic_code)
                end = winning_position(p1_play_history, "P1")
                if end:
                    return end

    player_2_input = "> Player 2: " 
    user2 = colored_input(player_2_input, "YELLOW").strip().lower()
    while not check_input_validility(user2, tic_code):
        print("Invalid Input, please eventer legal move")
        user2 = colored_input(player_2_input, "YELLOW").strip().lower()
        
    for plate in tic_code:
        for position in plate:
            if user2 == position:
                plate[plate.index(position)] = "O"
                p2_play_history.add(user2)
                print_tic_tac(tic_code)
                end = winning_position(p2_play_history, "P2")
    return end