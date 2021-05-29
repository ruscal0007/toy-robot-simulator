# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:19:15 2021

@author: ben
"""

from myModules.TableTop import TableTop
from myModules.ToyRobot import ToyRobot

TR=ToyRobot(("MyRobot"))
TT=TableTop()
TT.place_object(TR,"EAST")
TR.move(TT)
TT.showfield()
TR.move(TT)
TT.showfield()
