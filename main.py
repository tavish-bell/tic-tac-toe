from datetime import datetime


class Player:
    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name


class Move:
    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board:
    def __init__(self):
        self.moves = []
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def display(self):
        for line in self.board:
            print(f"{line[0]} {line[1]} {line[2]}")

    def add_move(self, move):
        row = move.position[0]
        column = move.position[1]
        self.board[row][column] = move.author.game_piece
        self.moves.append(move)


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.started_at = None
        self.finished_at = None


def play_game():
    print("Initializing Game!")
    player_one_name = input("What's player one's name? ")
    player_two_name = input("What's player two's name? ")

    player1 = Player("X", player_one_name)
    player2 = Player("O", player_two_name)
    print(f"{player1.name} is {player1.game_piece}")
    print(f"{player2.name} is {player2.game_piece}")

    players = [player1, player2]

    current_board = Board()

    current_game = Game(current_board, player1, player2)

    current_game.started_at = datetime.now()

    print("      Column 0  Column 1  Column 2")
    print("Row 0    -         -          -   ")
    print("Row 1    -         -          -   ")
    print("Row 2    -         -          -   ")

    win = False

    while not win:
        for player in players:
            if player == player1:
                number = "one"
            else:
                number = "two"
            row = int(
                input(f"What row does player {number} want to put their move in? ")
            )
            column = int(
                input(f"What row does player {number} want to put their move in? ")
            )
            player_move = Move(player, [row, column])
            current_board.add_move(player_move)
            current_board.display()
            check_for_winner(current_board.moves)
        break


def check_for_winner(moves):
    pass


play_game()
