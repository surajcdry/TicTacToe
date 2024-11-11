import os

play = True

# when the player wants to play
while play:
    # set the basics
    board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
    currentPlayer = "X"
    winner = None
    gameRunning = True

    def gameboard(board):
        print("Tic Tac Toe")
        print()
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

    while gameRunning:
        # print the board
        os.system('cls||clear')
        gameboard(board)
        print("Current Player: " + currentPlayer)
        print()

        # take user input & change value
        temp_logic = True
        move = None

        while temp_logic:
            move = input("Move (0-8): ")
            
            try:
                move = int(move)
                if (move >= 0) and (move < 9):
                    if (board[move] == "-"):
                        board[move] = currentPlayer
                        temp_logic = False
                    else:
                        print("Not allowed. Position already taken. Try again!")
                else:
                    print("Not allowed. Enter a value between 0-8!")
            except:
                print("Not a valid position. Try again! ")
        

        # check win or tie
        if ((board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") or 
        (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or 
        (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X")):
            winner = "X"
            gameRunning = False
        elif ((board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") or 
        (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O") or 
        (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O")):
            winner = "O"
            gameRunning = False

        if "-" not in board: # check for tie
            gameRunning = False

        # switch player
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"

    # print the winner
    os.system('cls||clear')
    gameboard(board)
    print()

    if (winner != None):
        print("Winner is " + winner)
    else:
        print("Tie!")

    print()

    # play again ?

    temp_logic2 = True
    while temp_logic2:
        play_again = input("Play again (y/n)? ")

        if play_again.lower() == 'y' or play_again.lower() == "yes":
            play = True
            temp_logic2 = False
        elif play_again.lower() == 'n' or play_again.lower() == "no":
            play = False
            temp_logic2 = False
            print("Thank you for playing!")

print()
