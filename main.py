import time
from board import Board
from MinMax import minimax_search
from random import randint
from alphaBeta import alpha_beta
import tracemalloc

"""
Loop to run a game against a passed in set of players, limits and heuristics
"""
def game_loop(game, player, test, limits, heuristic=None):
    if heuristic is None:
        heuristic = [1, 1]
    player_id = 0
    game_over = False
    while not game_over:
        if not test:
            print("-------START TURN------")
            print("Board:")
            game.print_board()
            print("Current player: " + str(player_id + 1))

        if player[player_id] == "human":
            action = int(input("Enter a move (0-5): "))
        elif player[player_id] == "minimax":
            [value, action] = minimax_search(game.copy(), player_id, limits[player_id], heuristic[player_id])
        elif player[player_id] == "random":
            avail = game.actions(player_id)
            action = avail[randint(0, len(avail) - 1)]
        elif player[player_id] == "alphabeta":
            [value, action] = alpha_beta(game.copy(), player_id, limits[player_id], heuristic[player_id])

        if not test:
            print("Action: "+str(action))
        temp = game.actions(player_id)
        if action in temp:
            if game.is_bonus(action, player_id):
                game = game.execute(game, action, player_id)
                temp = game.terminal()
                if temp:
                    game_over = True
                if not test:
                    print("BONUS TURN!")
            else:
                game = game.execute(game, action, player_id)
                temp = game.terminal()
                if temp:
                    game_over = True
                else:
                    player_id = 1 if player_id == 0 else 0
        else:
            print("Invalid move.")

    if not test:
        print("The Winner is Player " + str(game.winner()))
    if game.winner() == 1:
        if not test:
            print("With a score of " + str(game.p1()))
    elif game.winner() == 2:
        if not test:
            print("With a score of " + str(game.p2()))
    if not test:
        game.print_board()
    return game.winner()

"""
Sets the players if a player is playing
"""
def set_players(players):
    """
    Allows you to set player 0 and 1 to either a human, random move, or minimax move
    :param players:
    :return:
    """
    for i in range(len(players)):
        prompt = "Set Player " + str(i+1) + ":" + "\n\t1:Human" + "\n\t2:Random\n" + "\t3:Minimax\n" + "\t4:AlphaBeta\n"
        option = int(input(prompt))
        if option == 1:
            players[i] = "human"
        elif option == 2:
            players[i] = "random"
        elif option == 3:
            players[i] = "minimax"
        elif option == 4:
            players[i] = "alphabeta"

    print("")
"""
Loop to continuously play games
"""
def function_loop():
    player = ["human", "alphabeta"]
    limits = [6, 6]
    heuristic = [1,1]
    run_program = True

    print("Welcome to Mancala.")
    print("Would you like to play a game?")
    print("------------------------------\n")

    while run_program:
        print("Current players:")
        print("\tPlayer1:" + player[0] + "\n\tPlayer2:" + player[1] + "\n")
        prompt = "Options:" + "\n\t1.Set Players" + "\n\t2.Play Game\n"
        # try:
        option = int(input(prompt))
        if option == 0:
            run_program = False
        elif option == 1:
            set_players(player)
        elif option == 2:
            game_loop(Board(), player, False, limits, heuristic)
    run_program = True

    while run_program:
        print("Would you like to play a game?")
        print("------------------------------")
        prompt = "Options:" + "\n\t1.Don't Play Game" + "\n\t2.Play Game\n"
        option = int(input(prompt))
        if option == 2:
            game_loop(Board(4), player, False)
        else:
            run_program = False

"""
Tests choice against opponnent 100 times, 50 starting first and 50 starting second
"""
def test_loop(choice, opponent):
    limits = [4, 4]
    heuristic = [1, 1]
    tracemalloc.start()
    print(tracemalloc.get_traced_memory())
    player = [opponent, choice]
    sum = 0
    start = time.time()
    for i in range(50):
        result = game_loop(Board(4), player, True, limits, heuristic)
        if result == 2:
            sum += 1

    print(player[1] + " won a total of " + str(sum*2) + "% of games starting second")
    player = [choice, opponent]
    heuristic = [2, 1]
    new_sum = 0
    for i in range(50):
        result = game_loop(Board(4), player, True, limits, heuristic)
        if result == 1:
            new_sum += 1
    end = time.time()
    print(tracemalloc.get_traced_memory())
    print(player[0] + " won a total of " + str(new_sum*2) + "% of games starting first")
    print(str(end-start))

if __name__ == '__main__':
    #test_loop("alphabeta", "alphabeta")
    function_loop()