

def showBoard():
    print("Current board state:")
    print(f" {board[0]} | {board[1]} | {board[2]}\n---+---+---\n {board[3]} | {board[4]} | {board[5]}\n---+---+---\n {board[6]} | {board[7]} | {board[8]}")

def addPiece(currentPlayer):
    coord = int(input("Where do you want to put your next peice? "))
    if board[coord] == " ":
        if currentPlayer == player1:
            board[coord] = "X"
        elif currentPlayer == player2:
            board[coord] = "O"
    else:
        print("You can't put your piece there, this space has already been used.")
        addPiece(currentPlayer)

def help():
    print("#-------Guide-------#")
    print("Use these numbers as coordinates for where you want to put your peice:")
    print(f" 0 | 1 | 2\n---+---+---\n 3 | 4 | 5\n---+---+---\n 6 | 7 | 8")

def playerTicker():
    global currentPlayer
    if currentPlayer == player1:
        currentPlayer = player2
    elif currentPlayer == player2:
        currentPlayer = player1

def winCondition():
    if currentPlayer == player1:
        currentPiece = "X"
    elif currentPlayer == player2:
        currentPiece = "O"
    if board[0] == currentPiece and board[1] == currentPiece and board[2] == currentPiece:
        return (currentPlayer, True)
    elif board[3] == currentPiece and board[4] == currentPiece and board[5] == currentPiece:
        return (currentPlayer, True)
    elif board[6] == currentPiece and board[7] == currentPiece and board[8] == currentPiece:
        return (currentPlayer, True)
    elif board[0] == currentPiece and board[3] == currentPiece and board[6] == currentPiece:
        return (currentPlayer, True)
    elif board[1] == currentPiece and board[4] == currentPiece and board[7] == currentPiece:
        return (currentPlayer, True)
    elif board[2] == currentPiece and board[5] == currentPiece and board[8] == currentPiece:
        return (currentPlayer, True)
    elif board[0] == currentPiece and board[4] == currentPiece and board[8] == currentPiece:
        return (currentPlayer, True)
    elif board[2] == currentPiece and board[4] == currentPiece and board[6] == currentPiece:
        return (currentPlayer, True)
    else:
        return ("", False)

print("#-------New Game-------#")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1 = str(input("Name of player 1: "))
player2 = str(input("Name of player 2: "))
currentPlayer = player2
turn = 1
help()
while winCondition()[1] == False:
    playerTicker()
    print(f"#-------{currentPlayer}'s turn-------#")
    showBoard()
    addPiece(currentPlayer)
    if winCondition()[1] == False:
        continue
    else:
        print(f"{winCondition()[0]} won the game!")
        showBoard()
        break