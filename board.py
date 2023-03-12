from copy import copy


class Board:
    """
    Mancala game board
    """
    def __init__(self, p1=0, p2=0, p1_side=None, p2_side=None):
        """
        Constructor for a Mancala game board
        :param p1: score for player 1
        :param p2: score for player 2
        :param p1_side: Player 1's pits
        :param p2_side: Player 2's pits
        """
        if p2_side is None:
            p2_side = [4 for i in range(6)]
        if p1_side is None:
            p1_side = [4 for i in range(6)]
        self._p1 = p1
        self._p2 = p2
        self._p1_side = p1_side
        self._p2_side = p2_side

    def p1(self):
        return self._p1

    def p2(self):
        return self._p2

    def p1_side(self):
        return self._p1_side

    def p2_side(self):
        return self._p2_side

    def print_board(self):
        """
        Prints the board
        :return: nothing
        """
        ret = ""
        ret += "         0     1     2     3     4     5         \n"
        ret += "+-----+-----+-----+-----+-----+-----+-----+-----+\n"
        ret += "|     |  "
        for j in range(len(self._p1_side)):
            if self._p1_side[j] < 10:
                ret += str(self._p1_side[j]) + "  |  "
            else:
                ret += str(self._p1_side[j]) + " |  "
        ret += "   |\n"
        if self._p2 < 10:
            ret += "|  "
        else:
            ret += "| "
        ret += str(self._p2)
        ret += "  |-----+-----+-----+-----+-----+-----|  "
        ret += str(self._p1)
        if self._p1 < 10:
            ret += "  |\n"
        else:
            ret += " |\n"
        ret += "|     |  "
        for j in range(len(self._p2_side)):
            if self._p2_side[len(self._p2_side) - 1 - j] < 10:
                ret += str(self._p2_side[len(self._p2_side) - 1 - j]) + "  |  "
            else:
                ret += str(self._p2_side[len(self._p2_side) - 1 - j]) + " |  "
        ret += "   |\n"
        ret += "+-----+-----+-----+-----+-----+-----+-----+-----+\n"
        ret += "         5     4     3     2     1     0         \n"
        print(ret)

    def copy(self):
        """
        Makes a copy of the board
        :return: copy of the board
        """
        new_p1 = copy(self._p1)
        new_p2 = copy(self._p2)
        new_p1_side = copy(self._p1_side)
        new_p2_side = copy(self._p2_side)
        new_board = Board(new_p1, new_p2, new_p1_side, new_p2_side)
        return new_board

    def terminal(self):
        """
        Returns true if the game is ended, false otherwise
        :return: if the game is done
        """
        if self.playerSum(0) == 0:
            self._p2 += self.playerSum(1)
            self._p2_side = [0 for i in range(6)]
            return True
        elif self.playerSum(1) == 0:
            self._p1 += self.playerSum(0)
            self._p1_side = [0 for i in range(6)]
            return True
        else:
            return False

    def winner(self):
        """
        Determines which player is the winner
        :return: 1 if player 1 is the winner, 2 if player 2 is the winner
        """
        if self._p1 > self._p2:
            return 1
        elif self._p1 < self._p2:
            return 2
        else:
            return 0

    def is_bonus(self, action, player):
        """
        Determines if a given action would result in a bonus move
        :param action: move
        :param player: player making the move
        :return: True if bonus move, false if not
        """
        test = self.copy()
        return test.move(action, player)

    def playerSum(self, player):
        """
        Returns the sum of the seeds on a given player's side
        :param player: the given player
        :return: sum of the seeds on player's side
        """
        sum = 0
        if player == 0:
            for x in self._p1_side:
                sum += x
        else:
            for x in self._p2_side:
                sum += x
        return sum

    def available(self, move, player):
        """
        Determines if a given move is available to make by the given player
        :param move: move being made
        :param player: player making the move
        :return: True if the move is available, false otherwise
        """
        if player == 0:
            if self._p1_side[move] != 0:
                return True
        elif player == 1:
            if self._p2_side[move] != 0:
                return True
        return False

    def actions(self, player):
        """
        Returns all available actions for a given player
        :param player: player making the action
        :return: list of available moves
        """
        return [i for i in range(len(self._p1_side)) if self.available(i, player)]


    def eval(self, max_player, heuristic):
        """
        Evaluation function
        :param max_player: player being maximized for
        :param heuristic: The heuristic the board is being evaluated on
        :return: evaluation of the board
        """
        if heuristic == 1:
            return self.h1(max_player)
        elif heuristic == 2:
            return self.h2(max_player)
        elif heuristic == 3:
            return self.h3(max_player)
        elif heuristic == 4:
            return self.h4(max_player)

    def h1(self, max_player):
        """
        Heuristic that evaluates based on how much the player is winning by
        :param max_player: player being maximized
        :return difference between players
        """
        if max_player == 0:
            # Returns value for Player 1
            return (self._p1 - self._p2)
        else:
            # Returns value for Player 2
            return (self._p2 - self._p1)

    def h2(self, max_player):
        """
        Heuristic that evaluates based on how close max_player is to winning
        :param max_player: player being maximized
        :return: how close the player is to winning
        """
        if max_player == 0:
            return self._p1 - 25
        else:
            return self._p2 - 25

    def h3(self, max_player):
        """
        Heuristic that evaluates based on how close the opponent is to winning
        :param max_player: player being maximized
        :return: how close the opponent is to winning
        """
        if max_player == 0:
            return 25 - self._p2
        else:
            return 25 - self._p1

    def h4(self, max_player):
        """
        Heuristic that evaluates based on how many seeds are on the player's side
        :param max_player: player being maximized
        :return: how many seeds are on max_player's side
        """
        if max_player == 0:
            return self.playerSum(0)
        else:
            return self.playerSum(1)

    def move(self, move, player):
        """
        Makes a move flor the player
        :param move: number between 0-5
        :param player: the player making the move
        :return: True if the move results in a bonus move, false otherwise
        """
        bonus = False
        steal = False
        if player == 0:
            marbles = self._p1_side[move] + 1
            self._p1_side[move] = 0
            for i in range(1, marbles):
                bonus = False
                steal = False
                if move + i - len(self._p1_side) == 7:
                    move = -i
                    self._p1_side[move + i] += 1
                    steal = True
                elif move + i - len(self._p1_side) == 0:
                    self._p1 += 1
                    bonus = True
                elif move + i - len(self._p1_side) > 0:
                    self._p2_side[move + i - len(self._p1_side) - 1] += 1
                else:
                    self._p1_side[move + i] += 1
                    steal = True
            if steal and self._p1_side[(move + marbles - 1) % 14] == 1 and self._p2_side[
                len(self._p2_side) - (move + marbles) % 14] != 0:
                self._p1 += self._p2_side[len(self._p1_side) - (move + marbles) % 14] + 1
                self._p2_side[len(self._p1_side) - (move + marbles) % 14] = 0
                self._p1_side[(move + marbles - 1) % 14] = 0
            self.terminal()

        else:
            marbles = self._p2_side[move] + 1
            self._p2_side[move] = 0
            for i in range(1, marbles):
                bonus = False
                steal = False
                if move + i - len(self._p2_side) == 7:
                    move = -i
                    self._p2_side[move + i] += 1
                    steal = True
                elif move + i - len(self._p2_side) == 0:
                    self._p2 += 1
                    bonus = True
                elif move + i - len(self._p2_side) > 0:
                    self._p1_side[move + i - len(self._p2_side) - 1] += 1
                else:
                    self._p2_side[move + i] += 1
                    steal = True
            if steal and self._p2_side[(move + marbles - 1) % 14] == 1 and self._p1_side[
                len(self._p1_side) - (move + marbles) % 14] != 0:
                self._p2 += self._p1_side[len(self._p1_side) - (move + marbles) % 14] + 1
                self._p1_side[len(self._p1_side) - (move + marbles) % 14] = 0
                self._p2_side[(move + marbles - 1) % 14] = 0
            self.terminal()
        return bonus

    def execute(self, game, action, player):
        """
        Copies a given game, then makes a move on that board
        :param game: game the move is being made on
        :param action: the move being made
        :param player: player making the move
        :return: new board where the move has been made
        """
        ret = game.copy()
        ret.move(action, player)
        return ret
