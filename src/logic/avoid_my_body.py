from typing import Dict 
from typing import List

def avoid_my_body(my_body: dict, possible_moves: List[str]):
    my_head = my_body[0]
    for bodyComponent in my_body:
        if my_head["x"] == bodyComponent["x"] and my_head["y"] == bodyComponent["y"]:
            continue
        if "up" in possible_moves and my_head["y"] == bodyComponent["y"] + 1:
            possible_moves.remove("up")
        if "down" in possible_moves and my_head["y"] == bodyComponent["y"] - 1:
            possible_moves.remove("down")
        if "left" in possible_moves and my_head["x"] == bodyComponent["x"] + 1:
            possible_moves.remove("left")
        if "right" in possible_moves and my_head["x"] == bodyComponent["x"] - 1:
            possible_moves.remove("right")
    return possible_moves
