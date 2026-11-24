def create_board():
    # Create a 4-by-4 board filled with zeros.
    return [[0 for column in range(4)] for row in range(4)]


def display_board(board):
    # Display empty cells as dots.
    for row in board:
        print(" | ".join(str(number) if number != 0 else "." for number in row))
        print("-" * 21)


# Test the functions.
board = create_board()
display_board(board)
