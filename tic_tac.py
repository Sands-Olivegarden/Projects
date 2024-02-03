from tabulate import tabulate

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
def tic_tac():
    tic_code =[
    ["1a", "1b", "1c"],
    ["2a", "2b", "2c"],
    ["3a", "3b", "3c"]
    ]
    return tic_code
    

def print_tic_tac(tic_code):
    print(tabulate(tic_code, tablefmt="grid"))
   
   
def winning_position(p1_play_history, p2_play_history):
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
            for player_pos in p1_play_history:
                if player_pos == position:
                    winning_pos_list.append("Yes")
        if len(winning_pos_list) == 3:
            print("> Player 1 won.")
            return "end"
        winning_pos_list = []
    
    winning_pos_list = []
    for plate in win_positions:
        for position in plate:
            for player_pos in p2_play_history:
                if player_pos == position:
                    winning_pos_list.append("Yes")
        if len(winning_pos_list) == 3:
            print("> Player 2 won.")
            return "end"
        winning_pos_list = []
    return None
         
            
def multi_player_tracking(tic_code, p1_play_history, p2_play_history):
    user1 = input("> Player 1: ").strip().lower()
    while not check_input_validility(user1):
        print("Invalid Input, please eventer legal move")
        user1 = input("> Player 1: ").strip().lower()

    for plate in tic_code:
        for position in plate:
            if user1 == position:
                plate[plate.index(position)] = "X"
                p1_play_history.add(user1)
                print_tic_tac(tic_code)
                end = winning_position(p1_play_history, p2_play_history)
                if end:
                    return end

            
    user2 = input("> Player 2: ").strip().lower()
    while not check_input_validility(user2):
        print("Invalid Input, please eventer legal move")
        user2 = input("> Player 2: ").strip().lower()
        
    for plate in tic_code:
        for position in plate:
            if user2 == position:
                plate[plate.index(position)] = "O"
                p2_play_history.add(user2)
                print_tic_tac(tic_code)
                end = winning_position(p1_play_history, p2_play_history)
    return end
    
    
def single_player_tracking(tic_code, p1_play_history, smart_player_set, all_possible_moves):
    user1 = input("> Player 1: ").strip().lower()
    for plate in tic_code:
        for position in plate:
            if user1 == position:
                plate[plate.index(position)] = "X"
                p1_play_history.add(user1)
                print_tic_tac(tic_code)
                end = winning_position(p1_play_history, smart_player_set)
                if end:
                    return end
    
    smart_player(tic_code, p1_play_history, smart_player_set, all_possible_moves)
                
    

def find_min(element):
    if element == []:
        return -1
    else:
        if isinstance(element, list) and len(element) >= 2:
            if len(element[0]) > len(element[1]):
                element.pop(0)
                return find_min(element)
            elif len(element[0]) > len(element[1]):
                element.pop(1)
                return find_min(element)
            elif len(element[0]) == len(element[1]):
                element.pop(1)
                return find_min(element)
        else:
            return element[0]


def smart_player(tic_code, p1_play_history,  smart_player_set, all_possible_moves):
    
    played_algorithms = []
    # My loops are nested like this because I want to break out of only the plate loop.
    for plate in win_positions:
        for player_move in p1_play_history:
            for move in plate:
                if move == player_move:
                    played_algorithms.append(list(plate))
                    break
            
    for plate in played_algorithms:
        for move in plate:
            for player_move in p1_play_history:
                if move == player_move:
                    plate.remove(move)
                    
    if len(smart_player_set) > 0:
        for plate in played_algorithms:
            for move in plate:
                for player_move in smart_player_set:
                    if move == player_move:
                        plate.remove(move)
    for plate in played_algorithms:
        if len(plate) == 0:
            played_algorithms.remove(plate)
    
    shortest = find_min(played_algorithms)
    smart_move = shortest[0]

    if isinstance(all_possible_moves, list) and smart_move in all_possible_moves:
        all_possible_moves.remove(smart_move)
        print(f"Bot Played: {smart_move}")
        for plate in tic_code:
            for position in plate:
                if smart_move == position:
                    plate[plate.index(position)] = "O"
        print_tic_tac(tic_code)
        end = winning_position(p1_play_history, smart_player_set)
        smart_player_set.add(smart_move)
    
    elif len(shortest) == 2:
        smart_move = shortest[1]
        if smart_move in all_possible_moves:
            all_possible_moves.remove(smart_move)
            print(f"Bot Played: {smart_move}")
            for plate in tic_code:
                for position in plate:
                    if smart_move == position:
                        plate[plate.index(position)] = "O"
            print_tic_tac(tic_code)
            end = winning_position(p1_play_history, smart_player_set)
            smart_player_set.add(smart_move)
    else:
        pass
    return end
    
    
def setting():
    print("Welcome!!!")
    user_choice = input("> Y for single player\n> X for mutli player\n> :").strip().upper()
    while user_choice not in ["Y", "X"]:
        print("Sorry option not valid")
        user_choice = input("> Y for single player\n> X for mutli player\n> :").strip().upper()
    return user_choice


def check_input_validility(move):
    positions = tic_tac()
    for position_list in positions:
        for position in position_list:
            if move in position:
                return True
    return False


def main():
    end = None
    p1_play_history = set()
    p2_play_or_Bot_history = set()
    all_possible_moves = ["1a", "1b", "1c","2a", "2b", "2c", "3a", "3b", "3c"]
    user_choice = setting()
    tic_code = tic_tac()
    print_tic_tac(tic_code)
    if user_choice == "X":
        while not end:
            end = multi_player_tracking(tic_code, p1_play_history, p2_play_or_Bot_history)
    else:
        while not end:
            end = single_player_tracking(tic_code, p1_play_history, p2_play_or_Bot_history, all_possible_moves)


if __name__ == "__main__":
    main()   