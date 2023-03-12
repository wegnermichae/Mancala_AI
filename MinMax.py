def minimax_search(game, max_player, limit, heuristic):
    """
    Start of the minimax algorithm
    :param game: Instance of a game
    :param max_player: Who is currently the max player. This
    can either be 0 or 1
    :param limit: Depth limit
    :param heuristic: Heuristic to evaluate the board on
    :return: value and action that corresponds to the optimal move
    """
    value, action = max_value(game, 0, max_player, limit, heuristic)
    return value, action


def max_value(game, d, max_player, limit, heuristic):
    """
    Recursive function to find the max of possible successors
    to the game board.
    :param game: Instance of a game
    :param d: Maximum depth minimax can go
    :param max_player: Who is the player whose move we are trying
     to maximize. This can either be 0 or 1. Yes, this is the same player
     we pass into max_value
    :param limit: The given depth limit
    :param heuristic: The heuristic to evaluate the board on
    :return: value and action that corresponds to the optimal move
    """
    if game.terminal() or d >= limit:
        return game.eval(max_player, heuristic), None
    v = -100
    ply_player = (max_player + d) % 2
    for a in game.actions(ply_player):
        if game.is_bonus(a, ply_player):
            v2, a2 = max_value(game.execute(game, a, ply_player), d, max_player, limit, heuristic)
        else:
            v2, a2 = min_value(game.execute(game, a, ply_player), d + 1, max_player, limit, heuristic)
        if v2 > v:
            v, move = v2, a
    return v, move


def min_value(game, d, max_player, limit, heuristic):
    """
    Recursive function to find the min of possible successors
    to the game board.
    :param game: Instance of a game
    :param d: Maximum depth minimax can go
    :param max_player: Who is the player whose move we are trying
     to maximize. This can either be 0 or 1. Yes, this is the same player
     we pass into max_value
    :param limit: The given depth limit
    :param heuristic: The heuristic to evaluate the board on
    :return: value and action that corresponds to the optimal move
    """
    if game.terminal() or d >= limit:
        return game.eval(max_player, heuristic), None
    v = 100
    ply_player = (max_player + d) % 2
    for a in game.actions(ply_player):
        if game.is_bonus(a, ply_player):
            v2, a2 = min_value(game.execute(game, a, ply_player), d, max_player, limit, heuristic)
        else:
            v2, a2 = max_value(game.execute(game, a, ply_player), d + 1, max_player, limit, heuristic)
        if v2 < v:
            v, move = v2, a
    return v, move
