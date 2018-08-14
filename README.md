# Candy-Crush
This problem is about implementing a basic elimination for Candy Crush. Given a 2D integer array
board representing the grid of candy, different positive integers board[i][j] represent different
types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty.
The given board represents the state of the game following the player's move. Now, you need to
restore the board to a stable state by crushing candies according to the following rules:

(1) If three or more candies of the same type are adjacent vertically or horizontally, "crush" them
all at the same time ‐ these positions become empty.

(2) After crushing all candies simultaneously, if an empty space on the board has candies on top of
itself, then these candies will drop until they hit a candy or bottom at the same time. (No new
candies will drop outside the top boundary.)

(3) After the above steps, there may exist more candies that can be crushed. If so, you need to
repeat the above steps.

(4) If there does not exist more candies that can be crushed (ie. the board is stable), then return
the current board.

You need to perform the above rules until the board becomes stable, then return the current board.
Sample Input/Output: (read from candy_input.txt, output to candy_output.txt)

Example Input 1:
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[6
10,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

Example Output 1:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,41
4],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

Example Input 2:
[[9,9,7,9,9,9],[7,7,6,8,9,9],[5,6,5,6,8,8],[1,5,1,4,1,1],[2,1,4,1,1,1],[1,4,1,3,1,1],[1,1,2,1,3,1],[1,2,1,1,1,
3]]

Example Output 2:
[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[9,9,0,0,9,
9]]
