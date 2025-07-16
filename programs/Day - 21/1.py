import random

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for cell in board)

def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell not in ['X', 'O']]

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
    user_mark = 'X'
    computer_mark = 'O'

    print("Welcome to Tic Tac Toe!")
    print("You are 'X', Computer is 'O'")
    print_board(board)

    while True:
        # User's turn
        try:
            move = int(input(f"Your turn! Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            if board[move - 1] in ['X', 'O']:
                print("That spot is already taken. Try again.")
                continue
            board[move - 1] = user_mark
            print_board(board)

            if check_winner(board, user_mark):
                print("🎉 You win! 🎉")
                break

            if is_full(board):
                print("It's a draw!")
                break

            # Computer's turn
            print("Computer's turn...")
            available = get_available_moves(board)
            comp_move = random.choice(available)
            board[comp_move] = computer_mark
            print(f"Computer chose position {comp_move + 1}")
            print_board(board)

            if check_winner(board, computer_mark):
                print("💻 Computer wins! Better luck next time.")
                break

            if is_full(board):
                print("It's a draw!")
                break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Run the game
if __name__ == "__main__":
    play_game()
