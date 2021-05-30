# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:36:34 2021

@author: ruscal
"""

# test_TableTop.py

import pytest
from myModules.ToyRobot import ToyRobot
from myModules.TableTop import TableTop

def test_valid_place_and_remove_on_tabletop():
    TT=TableTop()
    TR=ToyRobot(TT)
    assert TR.place() == True
    assert TR.remove() == True
    assert TR.place("NORTH",2,0) == True
    assert TR.remove() == True
    assert TR.place("WEST",2,3) == True
    assert TR.remove() == True
    assert TR.place("EAST",1,4) == True
    assert TR.remove() == True
    assert TR.place("SOUTH",3,2) == True
    assert TR.remove() == True    
    
def test_invalid_place_on_tabletop():
    TT=TableTop()
    TR=ToyRobot(TT)
    assert TR.place("NfvcORTH",2,0) == False
    assert TR.place("WEST",5,3) == False
    assert TR.place("EAdddST",7,4) == False
    assert TR.place("South",3,2) == False
    assert TR.place("SOUTH",3,7) == False
    
def test_report():
    TT=TableTop()
    TR=ToyRobot(TT)
    assert TR.report() == False
    TR.place()
    assert TR.report() == "0,0,NORTH"    

def test_rotate_left():
    TT=TableTop()
    TR=ToyRobot(TT)
    TR.place()
    TR.rotate_left()    
    assert TR.report() == "0,0,WEST"
    TR.rotate_left()    
    assert TR.report() == "0,0,SOUTH"
    TR.rotate_left()    
    assert TR.report() == "0,0,EAST"
    TR.rotate_left()    
    assert TR.report() == "0,0,NORTH"

def test_rotate_right():
    TT=TableTop()
    TR=ToyRobot(TT)
    TR.place()
    TR.rotate_right()    
    assert TR.report() == "0,0,EAST"
    TR.rotate_right()    
    assert TR.report() == "0,0,SOUTH"
    TR.rotate_right()    
    assert TR.report() == "0,0,WEST"
    TR.rotate_right()    
    assert TR.report() == "0,0,NORTH"


def test_move_on_tabletop():
    TT=TableTop()
    TR=ToyRobot(TT)
    TR.place("NORTH",0,0)
    assert TR.move() == True
    assert TR.report() == "0,1,NORTH"
    assert TR.move() == True
    assert TR.report() == "0,2,NORTH"
    assert TR.move() == True
    assert TR.report() == "0,3,NORTH"
    assert TR.move() == True
    assert TR.report() == "0,4,NORTH"
    assert TR.move() == False
    assert TR.report() == "0,4,NORTH"
    TR.rotate_left()
    assert TR.move() == False
    assert TR.report() == "0,4,WEST"
    TR.rotate_left()
    assert TR.move() == True
    assert TR.report() == "0,3,SOUTH"
    TR.rotate_left()
    assert TR.move() == True
    assert TR.report() == "1,3,EAST"
    assert TR.move() == True
    assert TR.report() == "2,3,EAST"
    assert TR.move() == True
    assert TR.report() == "3,3,EAST"
    assert TR.move() == True
    assert TR.report() == "4,3,EAST"
    assert TR.move() == False
    assert TR.report() == "4,3,EAST"
    
    
    
    