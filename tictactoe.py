#Tic tac toe

import time


current_player="X"


board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

board2= [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

def displayboard(board):
  print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
  print(" ───┼───┼───")
  print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
  print(" ───┼───┼───")
  print(" ", board[2][0], "│", board[2][1], "│", board[2][2])


def check_win(board, current_player):
    won = False
    if board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player:
        won = True
    if board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player:
        won = True
    if board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player:
        won = True
    if board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player:
        won = True
    if board[0][1] ==current_player and board[1][1] == current_player and board[2][1] == current_player:
        won = True
    if board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player:
        won = True
    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        won = True
    if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        won = True
    elif board[0][0]!= "1" and board[0][1]!= "2" and board[0][2]!= "3" and board[1][0]!= "4" and board[1][1]!= "5" and board[1][2]!= "6" and board[2][0]!= "7" and board[2][1]!= "8" and board[2][2]!= "9":
      won = "greg"
    return won

def instructions():
  print("This is a 2 player game")
  time.sleep(0.5)
  print("Player 1 is crosses")
  time.sleep(0.5)
  print("Player 2 is noughts")
  time.sleep(0.5)
  print("The game is shown in this grid")
  time.sleep(0.5)
  print("To chose a position you select a number")
  time.sleep (0.5)
  print("")

def move(board,current_player):
    print(current_player,"s turn, where would you like to go?: ")
    choice=input("")
    choice=checkposition(choice,current_player)
    choice = overwrite(choice, current_player, board)
    print("")
    if choice == "1":
      board[0][0] = current_player
    elif choice == "2":
      board[0][1] = current_player
    elif choice == "3":
      board[0][2] = current_player
    elif choice == "4":
      board[1][0] = current_player
    elif choice == "5":
      board[1][1] = current_player
    elif choice == "6":
      board[1][2] = current_player
    elif choice == "7":
      board[2][0] = current_player
    elif choice == "8":
      board[2][1] = current_player
    elif choice == "9":
      board[2][2] = current_player
    return choice
      
def play(board):
  won = False
  current_player = "X"
  while won== False:
    move(board,current_player)
    won=check_win(board,current_player)
    displayboard(board)
    if won == True:
      winner=current_player
      print("The winner is ", winner)
    elif won == "greg":
      print("Draw!")
    if current_player=="X":
      current_player="O"
    else:
      current_player="X"
  return current_player
  return winner


def checkposition(choice, current_player):
  positions = ["1","2","3","4","5","6","7","8","9"]
  while choice not in positions:
    print("Invalid input")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go?: ")
    choice=input("")
    choice=overwrite(choice, current_player, board)
    
  return choice
  
def overwrite(choice, current_player, board):
  if board[0][0] != "1" and choice == "1":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[0][1] != "2" and choice == "2":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[0][2] != "3" and choice == "3":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[1][0] != "4" and choice == "4":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[1][1] != "5" and choice == "5":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[1][2] != "6" and choice == "6":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[2][0] != "7" and choice == "7":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[2][1] != "8" and choice == "8":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  elif board[2][2] != "9" and choice == "9":
    print("Slot already in use")
    print("")
    displayboard(board)
    print(current_player,"s turn, where would you like to go")
    choice=input("")
    choice=checkposition(choice,current_player)
  return choice
    
  



instructions() 
displayboard(board)
play(board)

print("Do you want to play again?")
again=input("").lower()
while again == "yes":
  board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
  displayboard(board)
  play(board)
  print("Do you want to play again?")
  again=input("")
