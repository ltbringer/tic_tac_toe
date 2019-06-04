# A game of Tic-Tac-Toe:

The good thing about this project could be that it will be built with no other library except numpy. numpy being irreplacable for the neat matrix manipulation methods that it can equip you with along with the speed of c++.

You can clone the repo, fork it or however you may please, but take a look at the documentation added to the code.

I have written the expectations in the beginning of the notebook. If it suits you, try to attempt it or atleast run it, if nothing works out for you, you can ask what you couldn't understand in the comments on github.

I have taken a object oriented approach as I felt there could be a synergy between object orient programming and the entities we have to model. If you find code comments annoying, please use an IDE which can help you shut them up easy, I know for instance, PyCharm has some sort of support. Most of the snippets seem huge, but that is again because of being heavily commented. All of the class methods, on an average are 12-14 lines of code.

## Installation
```
git clone git@github.com:AmreshVenugopal/tic_tac_toe.git
pip install numpy
```
That's the only dependency you would need!


## Usage
```
python train.py


> 'Enter the number of epochs for training
> 10000
```
You can view debug information if you set this in your shell:
```
export ENVIRONMENT=DEBUG.
```

## Expectations
### Step 1
What we are trying to model is a tic-tac-toe board. So the least that we need to build is:

- It should have a data-structure which represents a tic-tac-toe board.
- It should support the 'X' or 'O' symbol addition into the board.
- It should be able to declare a winner, in case there is one.
- This means it should be able to calculate if any row, column or diagonal has same values throughout.
- The constructor takes care of points (1), (2) and creates room for making (3) possible, so lets start with that:

- Create the board property, and set it up with 3x3 matrix full of zeroes, we are going forward with a matrix as the data-structure for representing the tic-tac-toe board.
- Establish relationships between symbols to be used on boards with numbers for easier calculation of winner.
- Assign the symbols to a player and a bot.
- Initialize a winner to be None cuz no one has won yet!

### Step 2
- After setting up our board, we need means to play. Don't worry too much about so much code, out of the three methods that you see, two are just wrappers around the first so, it is only the first function that needs attention.

- If a player (bot or human) enters their symbol to be placed somewhere in the board. Insert the corresponding integer instead. For 'X' insert a 2 and for 'O' insert a 1, otherwise let it be a blank cell.
- Draw the board, so that we can track how well have the players been doing. I'll add the code for that in later sections.
Check if the symbol that was just inserted led to a win. (code coming up)
Step 3
- In the previous section, point 3 is quite important. How do we know if someone has won the game? revisit Point 3 - Expectations. We need to find a way to check if any row or column or diagonal has the same value as the last symbol inserted, throughout.

### Step 3.1
Let's cover the diagonal case first, because it has less code and some of the concepts would get covered already, so less to say in the other parts. Before you get flustered with the code, let me let you know that this section too isn't doing much. The last two functions are nearly identical, apart from the iteration variable updation step.

In the method element_diagonal_has_same_value(self, item, item_x, item_y) We are checking if the latest symbol on the board also lies on the left or right diagonal.

### Step 3.2
Brace yourselves, even more code! Although I have tried my best to be clear in the code commends I can understand that so far it would have been really overwhelming. I know exactly how that feels, because, when I was trying this out the first time that's how I felt too. The best I can suggest is, take a break and try some of this by yourself. It will help you connect or even better, think of more efficient ways to do the same thing.

This step is a branch from step 3 where we had to determine if the game has a winner. This step identifies if any of the the rows or columns are having the same values throughout.

### Step 4
Connecting back to Step 2, where I had left out the draw_board and is_winning_move methods, they are now introduced. This is the final snippet of this session.

The method draw_board represents the matrix in a friendly tic-tac-toe board format by inserting values in a string and the method is_winning_move identifies a winner if is_game_over method returns True which has been covered in Step 3.

