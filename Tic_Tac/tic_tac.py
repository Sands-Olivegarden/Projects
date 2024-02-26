from single_player import single_player_tracking
from multi_player import multi_player_tracking
from accessories import welcome_print, print_tic_tac, tic_tac, exit_print, colored_input
import questionary
import sys


def setting():
    welcome = "Welcome!!!"
    welcome_print(welcome)
    user_choice = users_choice()
    return user_choice


def users_choice():    
    prompt = questionary.select("",
            choices= ["> Single player",
            "> Mutli player",
            "> EXIT"]).ask()
    
    
    if prompt == "> Single player": 
        colored_input("You have chosen Single Player mode.", "RED")
        colored_input("The 1st move is yours.", "GREEN")
        colored_input("Your are X.", "GREEN")
        return "O"
    elif prompt == "> Mutli player":
        colored_input("You have chosen Multi Player mode.", "BLUE")
        colored_input("Player 1 is X", "GREEN")
        colored_input("Player 2 is 0.", "YELLOW")
        return "X"
    elif prompt == "> EXIT":
        exit_print("Thank You For Playing.")
        sys.exit()
    return None


def game_continaution():
    print("\nPlay some more?")
    prompt = questionary.select("",
            choices= ["> Yes",
            "> No, thank you"]).ask()
    
    if prompt == "Yes":
        return main()
    else:
        exit_print("Thank You For Playing.")
    return None
    

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
            all_possible_moves, end, p1_play_history, p2_play_or_Bot_history = single_player_tracking(tic_code,
            p1_play_history, p2_play_or_Bot_history, all_possible_moves)
    return game_continaution()
    
    


if __name__ == "__main__":
    main()