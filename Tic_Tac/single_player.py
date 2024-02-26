from helpers import win_positions, find_min, winning_position
from accessories import print_tic_tac, colored_input, bot_color

def single_player_tracking(tic_code, p1_play_history, smart_player_set, all_possible_moves):
    user1 = colored_input("> Player 1: ", "GREEN").strip().lower()
    for plate in tic_code:
        if user1 in plate:
            plate[plate.index(user1)] = "X"
            p1_play_history.add(user1)
            print_tic_tac(tic_code)
            end = winning_position(p1_play_history, "P1")
            if end:
                return all_possible_moves, end, p1_play_history, smart_player_set

    return smart_player(tic_code, p1_play_history, smart_player_set, all_possible_moves)


def smart_player(tic_code, p1_play_history, smart_player_set, all_possible_moves):
    played_algorithms = []
    end = None
    
    for plate in win_positions:
        for player_move in p1_play_history:
            if player_move in plate:
                played_algorithms.append(list(plate))
                break

    for plate in win_positions:
        for smart_play in smart_player_set:
            if smart_play in plate and list(plate) in played_algorithms:
                played_algorithms.append(list(plate))
                break

    for plate in played_algorithms:
        for move in plate[:]:
            if move in p1_play_history or move in smart_player_set:
                plate.remove(move)

    if len(smart_player_set) > 0:
        for plate in played_algorithms:
            for move in plate[:]:
                if move in smart_player_set:
                    plate.remove(move)

    played_algorithms = [plate for plate in played_algorithms if plate]

    shortest = find_min(played_algorithms)
    smart_move = shortest[0]

    if smart_move in all_possible_moves:
        all_possible_moves.remove(smart_move)
        bot_played = f"Bot Played: {smart_move}"
        bot_color(bot_played)

        for plate in tic_code:
            if smart_move in plate:
                plate[plate.index(smart_move)] = "O"

        print_tic_tac(tic_code)
        end = winning_position(smart_player_set, "Bot")
        smart_player_set.add(smart_move)

    return all_possible_moves, end, p1_play_history, smart_player_set
