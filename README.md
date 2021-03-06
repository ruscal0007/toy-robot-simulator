# Toy Robot Simulator



## Description

Simulates a toy robot moving on a tabletop.  Robot will not follow commands that would cause it to fall from the tabletop
Commands are read in from a standard text file. see example_a.txt example_b.txt example_c.txt for examples

## Valid Commands

    PLACE X,Y,F
    MOVE
    LEFT
    RIGHT
    REPORT

- PLACE will put the toy robot on the table in position X,Y and facing NORTH,
  SOUTH, EAST or WEST.
- The origin (0,0) can be considered to be the SOUTH WEST most corner.
- The first valid command to the robot is a PLACE command, after that, any
  sequence of commands may be issued, in any order, including another PLACE
  command. The application will discard all commands in the sequence until
  a valid PLACE command has been executed.
- MOVE will move the toy robot one unit forward in the direction it is
  currently facing.
- LEFT and RIGHT will rotate the robot 90 degrees in the specified direction
  without changing the position of the robot.
- REPORT will announce the X,Y and F of the robot

## Usage
        Usage : toy-robot.py <filename> 
        
        Where <filename> is a txt file containing valid ToyRobot commands

        Position 0,0 is the SOUTH WEST corner of the play area
        
    
        Valid commands :
            PLACE X,Y,F
                X,Y position on play area
                F direction robot is facing
                Valid X,Y values 0-4 
                Valid F values "NORTH","EAST","SOUTH","WEST"
            MOVE
                move ToyRobot forward one square on play area
            LEFT
                rotate facing direciton anti-clockwise
            RIGHT
                rotate facing direction clockwise
            REPORT
                show current X,Y,F on pplay area
                
## examples
    See example files named example_x.txt where x is a number