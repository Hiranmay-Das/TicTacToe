import os
import math


# Custom Exception to handle wrong input
class InvalidMove(Exception):
    pass


class TicTacToe:
    # Default constructor
    def __init__(self):
        # The playing board in a Dictionary Form
        self.board = {1: '1', 2: '2', 3: '3',
                      4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9'}
        self.player1 = 'X'  # Symbol of First Player
        self.player2 = 'O'  # Symbol of Second Player
        input("X plays first. \nPRESS ANY KEY TO START GAME\n")
        os.system("clear") if os.name == "posix" else os.system("cls")
        self.gameTime()  # Start the Game
        input("Press any key to exit.")
        # self.cpu = 'O'

    # Function Name - isBoardFull
    # Parameters - None
    # Return Type - Boolean
    # Function - Returns True if there are no more moves to play, else Returns False.
    def isBoardFull(self):
        return not any(map(lambda x: x in "123456789", self.board.values()))

    # Function Name - isPositionEmpty
    # Parameters - position (Integer, holds a value within 1-9 representing a position on the board)
    # Return Type - Boolean
    # Function - Returns True if passed position is empty, else Returns False.
    def isPositionEmpty(self, position):
        return self.board[position] in "123456789"

    # Function Name - insertAtPosition
    # Parameters - position (Integer, holds a value within 1-9 representing a position on the board)
    #              playerID (Character, holds the character of the current player)
    # Return Type - None
    # Function - Inserts the player symbol to the given position, if possible.
    #            Otherwise, raises InvalidMove exception.
    def insertAtPosition(self, position, playerID):
        if self.isPositionEmpty(position):
            self.board[position] = playerID
        else:
            raise InvalidMove("That square is already occupied. Please enter valid input.")

    # Function Name - playerWon
    # Parameters - PlayerID (Character, holds the symbol of the current player)
    # Return Type - Boolean
    # Function - Checks if current player has won the game. Returns True if yes, else False.
    def playerWon(self, playerID):
        return ((self.board[1] == playerID and self.board[2] == playerID and self.board[3] == playerID) or
                (self.board[4] == playerID and self.board[5] == playerID and self.board[6] == playerID) or
                (self.board[7] == playerID and self.board[8] == playerID and self.board[9] == playerID) or
                (self.board[1] == playerID and self.board[4] == playerID and self.board[7] == playerID) or
                (self.board[2] == playerID and self.board[5] == playerID and self.board[8] == playerID) or
                (self.board[3] == playerID and self.board[6] == playerID and self.board[9] == playerID) or
                (self.board[1] == playerID and self.board[5] == playerID and self.board[9] == playerID) or
                (self.board[3] == playerID and self.board[5] == playerID and self.board[7] == playerID))

    # Function Name - printBoard
    # Parameters - None
    # Return Type - None
    # Function - Prints the current state of the playing board
    def printBoard(self):
        print('  ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print("  +---+---+")
        print('  ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print("  +---+---+")
        print('  ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print("\n")

    # Function Name - playerMove
    # Parameters - PlayerID (Character, holds the symbol of the current player)
    # Return Type - None
    # Function - Accepts input from Current player and inserts their symbol at desired location, if possible.
    #            handles exceptions where the user entered Illegal Character, entered out of bounds or
    #            enters and InvalidMove.
    def playerMove(self, playerID):
        while True:
            self.printBoard()
            position = input(f"Enter Move for {playerID} (1-9): ")
            os.system("clear") if os.name == "posix" else os.system("cls")
            try:
                position = int(position)
            except ValueError:
                print("\nPlease enter an Integer.\n")
                continue
            if position < 1 or position > 9:
                print("\nInteger must be within range 1-9.\n")
                continue
            else:
                try:
                    self.insertAtPosition(position, playerID)
                except InvalidMove:
                    print("\nThat square is already occupied. Please enter valid input.")
                    continue
                break

    # Function Name - gameTime
    # Parameters - None
    # Return Type - None
    # Function - Initiates the game and proceeds till their is a clear winner or
    #            there are no more moves to make (i.e. a tie) and declares the result
    def gameTime(self):
        while True:
            if self.isBoardFull():
                print("\n\nDRAW!")
                break
            self.playerMove(self.player1)
            if self.playerWon(self.player1):
                print(f"\n\nPlayer 1 ({self.player1}) won. Congrats.")
                break
            if self.isBoardFull():
                print("\n\nDRAW!")
                break
            self.playerMove(self.player2)
            if self.playerWon(self.player2):
                print(f"\n\nPlayer 2 ({self.player2}) won. Congrats.")
                break


# Base Function to call the TicTacToe class
if __name__ == '__main__':
    TicTacToe()
