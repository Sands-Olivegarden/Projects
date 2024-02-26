from accessories import player_one_color, player_two_color, bot_color

win_positions = [
        {"1a", "1b", "1c"},
        {"2a", "2b", "2c"},
        {"3a", "3b", "3c"},
        {"1a", "2a", "3a"},
        {"1b", "2b", "3b"},
        {"1c", "2c", "3c"},
        {"1a", "2b", "3c"},
        {"1c", "2b", "3a"},
    ]


def winning_position(play_history, player):
    win_positions = [
        {"1a", "1b", "1c"},
        {"2a", "2b", "2c"},
        {"3a", "3b", "3c"},
        {"1a", "2a", "3a"},
        {"1b", "2b", "3b"},
        {"1c", "2c", "3c"},
        {"1a", "2b", "3c"},
        {"1c", "2b", "3a"},
    ]
    winning_pos_list = []
    for plate in win_positions:
        for position in plate:
            for player_pos in play_history:
                if player_pos == position:
                    winning_pos_list.append("Yes")
        if len(winning_pos_list) == 3:
            if player == "P1":
                player_one_color("> Player 1 won!!!")
            elif player == "P2":
                player_two_color("> Player 2 won!!!")
            elif player == "Bot":
                bot_color("> Bot won!!!")
            return "end"
        winning_pos_list = []
    return None


def find_min(element):
    length_of_plate_list = {}
    for plate in element:
        length_of_plate_list[len(plate)] = plate
    smallest = 0
    for key, value in length_of_plate_list.items():
        if key == 2:
            smallest = key
    return length_of_plate_list.get(smallest)

def check_input_validility(move, positions):
    for position_list in positions:
        for position in position_list:
            if move in position:
                return True
    return False


