Created by Kojo Idun 
May 23, 2022 

A Python Implementation of Conway's Game of Life

Instructions

First run the program and wait for the pygame window to appear with all the cells.
They should be white at first. 

There are two main states for the program 
started == FALSE or Started state 
started == TRUE or Stopped state

When the game is started you cannot click the cells to change their state anymore

There are a few controls for the application

CONTROLS

S key --> Start the game 
Pressing the S key will start the grid update cycle and play the game 

NOTE:
If there is a "still life" cell pattern that doesn't not change but continues to live on infinitely 
the game will not enter the Stopped state automatically, meaning you won't be able to click on cells 
though it looks like the game is in a stopped state 

You must either reset the grid or pause the grid to click on cells and change their states again

An example of a still life cell pattern can be found here: 
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns 

R key --> Reset the grid 
Pressing the R key sets all the cells back to their dead state and puts the game in its stopped state
You can now click on the cells again to change their state

P key --> Pause the grid
Pressing the P key pauses the state of the grid where it is you can change cell states after pausing 
Pausing only works if the game has been started 


If you have any requests or input feel free to comment