import os


class InvalidMove(Exception):
    pass


# noinspection PyPep8Naming
class TicTacToe:
    def __init__(self):
        self.board = {1: '1', 2: '2', 3: '3',
                      4: '4', 5: '5', 6: '6',
                      7: '7', 8: '8', 9: '9'}
        input("X plays first. \nPRESS ANY KEY TO START GAME")
        self.player1 = 'X'
        self.player2 = 'O'
        self.playerMoves()
        input("Press any key to exit.")
        # self.cpu = 'O'

    def isBoardFull(self):
        return not any(map(lambda x: x in "123456789", self.board.values()))

    def isPositionEmpty(self, position):
        return self.board[position] in "123456789"

    def insertAtPosition(self, position, playerID):
        if self.isPositionEmpty(position):
            self.board[position] = playerID
        else:
            raise InvalidMove("That square is already occupied. Please enter valid input.")

    def playerWon(self, playerID):
        return ((self.board[1] == playerID and self.board[2] == playerID and self.board[3] == playerID) or
                (self.board[4] == playerID and self.board[5] == playerID and self.board[6] == playerID) or
                (self.board[7] == playerID and self.board[8] == playerID and self.board[9] == playerID) or
                (self.board[1] == playerID and self.board[4] == playerID and self.board[7] == playerID) or
                (self.board[2] == playerID and self.board[5] == playerID and self.board[8] == playerID) or
                (self.board[3] == playerID and self.board[6] == playerID and self.board[9] == playerID) or
                (self.board[1] == playerID and self.board[5] == playerID and self.board[9] == playerID) or
                (self.board[3] == playerID and self.board[5] == playerID and self.board[7] == playerID))

    def printBoard(self):
        print('  ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print("  +---+---+")
        print('  ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print("  +---+---+")
        print('  ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print("\n")

    def player1Move(self):
        while True:
            os.system("clear") if os.name == "posix" else os.system("cls")
            self.printBoard()
            position = input(f"Enter Move for {self.player1} (1-9): ")
            try:
                position = int(position)
            except ValueError:
                print("Please enter an Integer.")
                continue
            if position < 1 or position > 9:
                print("Integer must be within range 1-9.")
                continue
            else:
                self.insertAtPosition(position, self.player1)
                break

    def player2Move(self):
        while True:
            os.system("clear") if os.name == "posix" else os.system("cls")
            self.printBoard()
            position = input(f"Enter Move for {self.player2} (1-9): ")
            try:
                position = int(position)
            except ValueError:
                print("Please enter an Integer.")
                continue
            if position < 1 or position > 9:
                print("Integer must be within range 1-9.")
                continue
            else:
                self.insertAtPosition(position, self.player2)
                break

    def playerMoves(self):
        while True:
            if self.isBoardFull():
                print("DRAW!")
                break
            self.player1Move()
            if self.playerWon(self.player1):
                print(f"\n\nPlayer 1 ({self.player1}) won. Congrats.")
                break
            if self.isBoardFull():
                print("\n\nDRAW!")
                break
            self.player2Move()
            if self.playerWon(self.player2):
                print(f"\n\nPlayer 2 ({self.player2}) won. Congrats.")
                break


if __name__ == '__main__':
    TicTacToe()
