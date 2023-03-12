# Mancala

Mancala game with MiniMax/AlphaBeta algorithms

## Basics of Mancala

- Each player starts with 4 “seeds” in each of their 6 pits, with “stores” at the end of the pits
- The player can only move seeds on their side of the board, placing 1 seed in each pit as they move counterclockwise
- If the player ends in their store, they get a bonus turn
- If the player lands in an empty space on their side, they can “steal” the opposing player’s seeds on the opposite side
- The game ends when one player has no seeds in their pits
- Or when a player has no chance of winning with remaining moves
- The goal is to end the game with the most seeds

## Functionality

- Two functions that can be run from main
- function_loop(), This allows the user to visually see the games being played, also letting them play against random, MiniMax, AlphaBeta or another player
- test_loop(choice, opponent), This will run 100 games of the "choice" algorithm vs the "opponent" algorithm, the depth limits and evaluation heuristics can be manually changed within the method. test_loop will also get the elapsed time for the tests along with peak and ending memory usage

## Authors
- Carson Meredith
- Hamza Zuberi
- Michael Wegner
