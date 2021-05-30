# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:19:15 2021

@author: ruscal
"""

import sys
import fileinput
import re
from myModules.TableTop import TableTop
from myModules.ToyRobot import ToyRobot

if len(sys.argv) > 1:
    # Process txt file with appropriate commands 
    TT=TableTop()
    TR=ToyRobot(TT)
    for line in fileinput.input():
        if re.search("PLACE",line):
            m = re.match("PLACE\s+(\d+),(\d+),(.+)",line)
            if m is not None:
                row = m.group(1)        
                column =  m.group(2)
                facing = m.group(3)
                TR.place(facing,int(row),int(column))
        if re.search("MOVE",line):
            TR.move()
        if re.search("LEFT",line):
            TR.rotate_left()
        if re.search("RIGHT",line):
            TR.rotate_right()
        if re.search("REPORT",line):
            print(TR.report())
else:
    #no file passed        
    print(
        '''
        Error : Command file not passed to toy-robot.py
        
        This program simulates a ToyRobot playing on a 5x5 grid
                
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
        '''
        )
            