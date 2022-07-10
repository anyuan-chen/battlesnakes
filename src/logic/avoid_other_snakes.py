from typing import List


def avoid_other_snakes(my_body: dict, possible_moves: List[str], other_snakes: List[dict]) -> List[str]:
    new_moves_delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    new_moves_name = ["up", "down", "right", "left"]
    my_head = my_body[0]

    for snake in other_snakes:
        for bodyComponent in snake["body"]:

            if len(possible_moves) == 0:
                return possible_moves

            for i in range(len(new_moves_delta)):
                move_name, dx, dy = new_moves_name[i], new_moves_delta[i][0], new_moves_delta[i][1]
                nx, ny = my_head["x"] + dx, my_head["y"] + dy
                if move_name in possible_moves and (bodyComponent["x"] == nx and bodyComponent["y"]):
                    possible_moves.remove(move_name)

    return possible_moves

