def display_board(board):
    # Display the game board.
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    # Check all possible winning lines.
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for line in winning_lines:
        if all(board[index] == player for index in line):
            return True

    return False


def play_game():
    # The numbers show the available choices.
    board = [str(number) for number in range(1, 10)]
    current_player = "X"

    print("Welcome to X/O!")
    print("Choose a number from 1 to 9 to place your mark.")

    while True:
        display_board(board)
        choice = input(f"Player {current_player}, choose a spot: ")

        # Make sure the input is a number from 1 to 9.
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1

        # Make sure the chosen spot is empty.
        if board[position] in ("X", "O"):
            print("That spot is already taken. Choose another one.")
            continue

        board[position] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(spot in ("X", "O") for spot in board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch to the other player.
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# Start the game.
play_game()
