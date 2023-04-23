# tic_tak_toe
This is a Python program that uses the tkinter library to create a graphical user interface (GUI) for a tic-tac-toe game.
The game has two modes: single player and two player. 

The game starts by creating a Tkinter window and setting its title to "TIC TAK TOC". 
The game board is represented using nine Tkinter buttons, arranged in a 3x3 grid. 
The game board is a 3x3 grid of buttons that players click to make their moves.

The game is played between two players. 
The first player is represented by "X" and the second player by "O". 
When a player clicks on a button, its text changes to either "X" or "O", depending on whose turn it is. 
This is done by calling the click function, which takes two arguments: the button that was clicked, and the current player mode.

The game logic is handled by the click function. It first checks if the game is over, in which case it returns without doing anything. 
It then sets the text of the button to the current player's symbol and checks if the player has won. 
If the player has won, it displays a message box with the winner's name and resets the board. 
If the game is not over and no player has won, it switches the player mode and continues the game.



The `button(mode)` function creates the game board.
It creates 9 buttons, one for each square on the board, and places them in a 3x3 grid using the `grid()` method. 
Each button is assigned a command that calls the `click()` function with the button object and the mode argument as parameters. 
The `b_exit` and `b_reset` buttons are also created and placed at the bottom of the game board.

The `full_board(mode)` function checks if the board is full and displays a message box with the result of the game if it is. 
The full_board function checks if the game is over, that is, if all the cells on the board are filled with either "X" or "O". 
If this is the case and no player has won, it displays a message box that says "IT'S DRAW" and resets the board.


The `reset(mode)` function resets the game by removing all the buttons and creating new ones. 
It also sets the `game` variable to True, indicating that the game is still in progress.

The `click(button, mode)` function is called whenever a player clicks on a button. 
It checks if the game is over or not, and if not, it sets the text of the button to the appropriate symbol (either X or O), depending on whose turn it is. 
It then checks if there is a winner by calling the `check_win()` function. 
If there is a winner, it displays a message box with the result of the game and sets the `game` variable to False to indicate that the game is over.

The `check_win()` function checks all the possible winning combinations on the board and returns True if there is a winner, and False if not.

The "Exit" button is used to exit the game.

Overall, this program provides a simple GUI for a tic-tac-toe game that can be played in either single or two-player mode. 
It uses the tkinter library to create the GUI and provides functions to check for a winner, reset the game, and exit the program.
