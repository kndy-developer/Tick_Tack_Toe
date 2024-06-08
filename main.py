# Define the game board as a list
board = [' '] * 9

# Function to display the game board
def display_board():
  for i in range(3):
    print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')

# Function to check if a player has won
def check_win(player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
      return True
  return False

# Function to check if the board is full
def check_full():
  for space in board:
    if space == ' ':
      return False
  return True

# Function to get player input
def get_player_move(player):
  while True:
    try:
      move = int(input(f"Player {player}, enter your move (1-9): "))
      if move > 0 and move <= 9 and board[move - 1] == ' ':
        return move - 1
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
game_on = True
current_player = 'X'

while game_on:
  display_board()

  # Get player move
  move = get_player_move(current_player)

  # Update board
  board[move] = current_player

  # Check for win
  if check_win(current_player):
    display_board()
    print(f"Player {current_player} wins!")
    game_on = False
  
  # Check for tie
  elif check_full():
    display_board()
    print("It's a tie!")
    game_on = False

  # Switch turns
  current_player = 'O' if current_player == 'X' else 'X'

print("Thanks for playing!")
