# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:19:15 2021

@author: ruscal
"""
import fileinput
import re
from myModules.TableTop import TableTop
from myModules.ToyRobot import ToyRobot

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
        
        
            