# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:19:15 2021

@author: ben
"""

from myModules.TableTop import TableTop
from myModules.ToyRobot import ToyRobot


TT=TableTop()
TR=ToyRobot(TT)

TR.place("NORTH",0,0)
TR.rotate_left()
TR.report()

"""
TR.place("EAST",1,2)
TR.move()
TR.move()
TR.rotate_left()
TR.move()
TR.report()
"""

