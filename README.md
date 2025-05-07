# Tic-Tac-Toe AI with Minimax and Alpha-Beta Pruning

This project implements an AI-powered Tic-Tac-Toe game in Python using the **Minimax algorithm** and its optimized version with **Alpha-Beta Pruning**. The goal is to create a game-playing agent that plays optimally and efficiently.

## 🎯 Objectives

- Develop core logic for a playable Tic-Tac-Toe game.
- Implement the Minimax algorithm to enable optimal decision-making for the AI.
- Optimize Minimax with Alpha-Beta Pruning to improve computational efficiency.
- Compare performance between standard Minimax and Alpha-Beta Pruning.

## 🧠 Algorithms Used

### Minimax
A recursive decision-making algorithm used in game theory to determine the best move for a player, assuming the opponent also plays optimally.

### Alpha-Beta Pruning
An optimization to Minimax that skips evaluating branches that won’t affect the final decision, significantly reducing computation time.

## 📁 Structure

- `TicTacToe`: Handles game state and logic
  - `print_board()`
  - `available_moves()`
  - `make_move()`
  - `winner()`, etc.
- `minimax()`: Standard Minimax recursive logic.
- `minimax_ab()`: Minimax with Alpha-Beta Pruning.
- `get_best_move()`: AI move decision based on selected algorithm.

## 🕹️ How to Play

```bash
# Run the game (example entry point)
python Min_Max.py
