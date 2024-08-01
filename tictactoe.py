import numpy as np
import random

def display_welcome():
    """
    Displays a welcome message to the user
    """
    print('Welcome to Tic-Tac-Toe')
    print("You are the 'X' and the computer is the 'O'.")
    print('The first player to get three of their marks in a row, column, or diagonal wins.')
    print("If all squares are filled and no player has three in a row, the game ends in a draw.")
    print("Let's begin!")
def get_user_move(board):
    """
    Asks the user for their move, checks its validity, and updates the board.
    Ensures the chosen square is empty and within range.
    Returns a tuple (row, col) representing the user's move.
    """
    print()
    print('Choose your move by entering a row and column')
    while True:
        try:
            user_move_row = int(input('Enter the row (1-3) you would like to select: ')) - 1
            user_move_col = int(input('Enter the column (1-3) you would like to select: ')) - 1

            if user_move_row not in range(3) or user_move_col not in range(3):
                print()
                print('That is an invalid move. Please enter a number that is between 1 and 3')
            elif board[user_move_row][user_move_col] != ' ':
                print()
                print('That space is taken. Please choose another')
            else:
                board[user_move_row][user_move_col] = 'X'
                return user_move_row, user_move_col
        except ValueError:
            print()
            print("Invalid input. Please enter a number.")

def get_comp_move(board):
    """
     Determines the computer's move based on a strategy to block the user.
     Finds an empty square and places the computer's move ('O').
     Returns a tuple (row, col) representing the computer's move.
     """
    print()
    print('It is my turn!')
    open_moves = []
    block_move = find_blocking_move(board)
    if block_move:
        row, col = block_move
        board[row][col] = 'O'
        show_board(board)
        return block_move

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                open_moves.append((row, col))
    if open_moves:
        move = random.choice(open_moves)
        board[move[0]][move[1]] = 'O'
        show_board(board)
        return move
    return None


def find_blocking_move(board):
    """
    Checks the board to find a blocking move to prevent the user from winning.
    Returns a tuple (row, col) representing the blocking move or None if no block is available.
    """
    for i in range(3):
        counter = 0
        empty_spot = None
        for j in range(3):
            if board[i][j] == 'X':
                counter += 1
            elif board[i][j] == ' ':
                empty_spot = (i, j)
        if counter == 2 and empty_spot:
            return empty_spot

    # Check columns for blocking move
    for i in range(3):
        counter = 0
        empty_spot = None
        for j in range(3):
            if board[j][i] == 'X':
                counter += 1
            elif board[j][i] == ' ':
                empty_spot = (j, i)
        if counter == 2 and empty_spot:
            return empty_spot

    # Check top-left to bottom-right diagonal
    counter = 0
    empty_spot = None
    for i in range(3):
        if board[i][i] == 'X':
            counter += 1
        elif board[i][i] == ' ':
            empty_spot = (i, i)
    if counter == 2 and empty_spot:
        return empty_spot

    # Check top-right to bottom-left diagonal
    counter = 0
    empty_spot = None
    for i in range(3):
        if board[i][2 - i] == 'X':
            counter += 1
        elif board[i][2 - i] == ' ':
            empty_spot = (i, 2 - i)
    if counter == 2 and empty_spot:
        return empty_spot

    return None



def is_full(board):
    """
    Checks if all the squares on the board are filled
    Returns True if the board is full, otherwise False.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def play_again():
    """
    Asks the user if they would like to play again
    Returns True if the user wants to play again, False otherwise.
    """
    while True:
        response = input("Do you want to play again? (y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print()
            print("Invalid input. Please enter 'y' or 'n'.")

def get_first_player():
    """
    Asks the user if they want to go first and returns the first player.
    Returns 'user' if the user wants to go first, otherwise 'computer'.
    """
    print()
    choice = input('Would you like to go first? Type (y/n): ').lower()

    while choice not in ['y', 'n']:
        print()
        print("That is not an option. Please type 'y' or 'n'.")
        choice = input('Would you like to go first? Type (y/n): ').lower()
    if choice == 'y':
        return 'user'
    elif choice == 'n':
        return 'computer'

def get_winner(board):
    """
    Checks if there is a winner by looking for three marks in a row, column, or diagonal.
    Returns 'X' if the user wins, 'O' if the computer wins, or None if there is no winner.
    """

    # check row for winner
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # check column for winner
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return board[0][column]

    # check for diagonal winner
    if (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[0][2] == board[1][1] == board[2][0] != ' '):
        return board[1][1]
    return None

def show_board(board):
    """
    Displays the current state of the board to the user.
    """
    for row in board:
        print(f"[{' '.join(row)}]")
    print()


def main():
    """
    Main function to run the Tic-Tac-Toe game.
    Manages the game loop, player turns, and checks for win or draw conditions.
    """

    display_welcome()

    play_game = True

    while play_game:
        board = np.array([[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']])
        first_player = get_first_player()
        winner = None

        if first_player == 'user':
            while not winner and not is_full(board):
                get_user_move(board)
                show_board(board)
                winner = get_winner(board)
                if winner or is_full(board):
                    break
                get_comp_move(board)
                winner = get_winner(board)
        else:
            while not winner and not is_full(board):
                get_comp_move(board)
                winner = get_winner(board)
                if winner or is_full(board):
                    break
                get_user_move(board)
                winner = get_winner(board)

        show_board(board)

        if winner:
            if winner == 'X':
                print("Good job! You win!")
            else:
                print()
                print("I win. Better luck next time!")
        else:
            print()
            print("It's a draw!")

        play_game = play_again()
    print()
    print("Thanks for playing with me!")

if __name__ == '__main__':
    main()