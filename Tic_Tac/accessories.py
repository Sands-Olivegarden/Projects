from art import *
from tabulate import tabulate
from termcolor import colored
from tabulate import tabulate


def welcome_print(prompt):
    tprint(f"{prompt:^100}")
    return None
    
def player_one_color(prompt):
    print(colored(prompt, "green"))
    return None
    
def player_two_color(prompt):
    print(colored(prompt, "yellow"))
    return None
    
def bot_color(prompt):
    print(colored(prompt, "red"))
    return None

def exit_print(prompt):
    tprint(f"{prompt:^50}")
    return None

def print_tic_tac(tic_code):
    print(tabulate(tic_code, tablefmt="grid"))
    return None
    
 

def tic_tac():
    tic_code =[
    ["1a", "1b", "1c"],
    ["2a", "2b", "2c"],
    ["3a", "3b", "3c"]
    ]
    return tic_code


def colored_input(prompt, color):
    if color == 'BLUE':
        color = '\033[94m'
    elif color == "RED":
        color = '\033[91m'
    elif color == "GREEN":
        color = '\033[92m'
    elif color == "YELLOW":
        color = '\033[93m'
    END = '\033[0m'
    return input(color + prompt + END)



