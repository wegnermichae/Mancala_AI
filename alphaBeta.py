def alpha_beta(game, maximizing_player, limit, heuristic):
    """
    Start of the alphabeta algorithm
    :param game: Instance of a game
    :param maximizing_player: Who is currently the max player. This
    can either be 0 or 1
    :param limit: Depth limit
    :param heuristic: Heuristic to evaluate the board on
    :return: value and action that corresponds to the optimal move
    """
    value, action = ab_max_value(game, 0, maximizing_player, -1000, 1000, limit, heuristic)
    return value, action


def ab_max_value(game, d, max_player, alpha, beta, limit, heuristic):
    """
    Recursive function to find the max of possible successors
    to the game board with alpha beta pruning
    :param game: Instance of a game
    :param d: Maximum depth minimax can go
    :param max_player: Who is the player whose move we are trying
     to maximize. This can either be 0 or 1
    :param alpha: the current alpha value
    :param beta: the current beta value
    :param limit: The given depth limit
    :param heuristic: The heuristic the board is being evaluated on
    :return: value and action that corresponds to the optimal move
    """
    if game.terminal() or d >= limit:
        return game.eval(max_player, heuristic), None
    v = -100
    ply_player = (max_player + d) % 2
    for a in game.actions(ply_player):
        if game.is_bonus(a, ply_player):
            v2, a2 = ab_max_value(game.execute(game, a, ply_player), d, max_player, alpha, beta, limit, heuristic)
        else:
            v2, a2 = ab_min_value(game.execute(game, a, ply_player), d + 1, max_player, alpha, beta, limit, heuristic)
        if v2 > v:
            v, move = v2, a
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v, move


def ab_min_value(game, d, max_player, alpha, beta, limit, heuristic):
    """
    Recursive function to find the min of possible successors
    to the game board with alpha beta pruning
    :param game: Instance of a game
    :param d: Maximum depth minimax can go
    :param max_player: Who is the player whose move we are trying
     to maximize. This can either be 0 or 1
    :param alpha: the current alpha value
    :param beta: the current beta value
    :param limit: The given depth limit
    :param heuristic: The heuristic the board is being evaluated on
    :return: value and action that corresponds to the optimal move
    """
    if game.terminal() or d >= limit:
        return game.eval(max_player, heuristic), None
    v = 100
    ply_player = (max_player + d) % 2
    for a in game.actions(ply_player):
        if game.is_bonus(a, ply_player):
            v2, a2 = ab_min_value(game.execute(game, a, ply_player), d, max_player, alpha, beta, limit, heuristic)
        else:
            v2, a2 = ab_max_value(game.execute(game, a, ply_player), d + 1, max_player, alpha, beta, limit, heuristic)
        if v2 < v:
            v, move = v2, a
        beta = min(v, beta)
        if beta <= alpha:
            break
    return v, move
