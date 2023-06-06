def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j != len(board[0]) - 1:
              print(board[i][j],"|", end = " ") 
        if i != len(board) - 1:
          print("\n~~~~~~~~~")
          

# takes player number, prints a prompt, takes input, extracts x and y, and returns them          
def takeMove(playerNo):
  move = input("Player",  playerNo, "move: ")
  x = int(move.split(" ")[0])
  y = int(move.split(" ")[1])
  return x, y
 
def moveIsValid(board, x, y, symb):
  # given coord must be in the board 
  # yazligi yerde karakter olmamalidi empty*
  if 0 <= x < len(board) and 0 <= y < len(board[0]):
    if board[x][y] == ' ':
        return True 
  else:
    return False


def play(b):
  print("\nPlayer 1: x, player 2: o\n")
  # 1. ask p1
  # 2. take coordinates '1 2' 
  # 3. put x to input coordinates of board if empty
  # 4. print board 
  x1, y1 = takeMove("1") 
  while not moveIsValid(b, x1, y1, 'x'):
      print("INVALID INPUT.")
      x1, y1 = take_move("1")
  board[x][y] = 'x'
  printBoard(board)
  # check if game ends 
  # 
    
  x2, y2 = takeMove("2")
   

def main():
  board = [[' ' for i in range(3)] for i in range(3)]
  play(board)
  

if __name__ == "__main__": main()
