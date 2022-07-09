import random
from re import M
from typing import List, Dict
import avoid_my_neck
from logic.avoid_my_body import avoid_my_body
from logic.avoid_other_snakes import avoid_other_snakes
from logic.avoid_walls import avoid_walls

def get_info() -> dict:
    return {
        "apiversion": "1",
        "author": "Andrew and James",  
        "color": "#ff3r44",  # TODO: Personalize
        "head": "default",  # TODO: Personalize
        "tail": "default",  # TODO: Personalize
    }


def choose_move(data: dict) -> str:
    """
    https://docs.battlesnake.com/references/api/sample-move-request
    return: A String, the single move to make. One of "up", "down", "left" or "right".
    """
    my_snake = data["you"]      # A dictionary describing your snake's position on the board
    my_head = my_snake["head"]  # A dictionary of coordinates like {"x": 0, "y": 0}
    my_body = my_snake["body"]  # A list of coordinate dictionaries like [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}]

    # Uncomment the lines below to see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnake this turn is: {my_snake}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    # Step 0: Don't allow your Battlesnake to move back on it's own neck.
    possible_moves = avoid_my_neck(my_body, possible_moves)
    possible_moves = avoid_other_snakes(my_body, data["board"]["snakes"])
    possible_moves = avoid_walls(my_head, possible_moves, data["board"])
    possivle_moves = avoid_my_body(my_body, possible_moves)
    
    # TODO: Step 4 - Find food.
    # Use information in `data` to seek out and find food.
    # food = data['board']['food']

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    move = random.choice(possible_moves)
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move






