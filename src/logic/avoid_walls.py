from typing import Dict
from typing import List


def avoid_walls(my_body: Dict, possible_moves: List[str], board: Dict) -> List[str]:
    my_head = my_body[0]
    new_moves_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    new_moves_name = ["up", "down", "right", "left"]

    for i in range(len(new_moves_delta)):
        move_name, dx, dy = new_moves_name[i], new_moves_delta[i][0], new_moves_delta[i][1]
        nx, ny = my_head["x"] + dx, my_head["y"] + dy
        if move_name in possible_moves and (nx < 0 or nx > board["width"] or ny < 0 or ny > board["height"]):
            possible_moves.remove(move_name)

    return possible_moves
