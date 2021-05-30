# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:23:06 2021

@author: ruscal
"""

# test_TableTop.py

import pytest
from myModules.TableTop import TableTop


def test_default_play_area_size():
    TT = TableTop()
    assert len(TT.play_area[0]) == 5
    assert len(TT.play_area[1]) == 5
    
def test_custom_pay_area_size():
    TT = TableTop(20,50)
    assert len(TT.play_area) == 20
    assert len(TT.play_area[0]) == 50
    
def test_is_free_inside_playarea():
    TT = TableTop()
    assert TT.is_free(0,0) == True
    assert TT.is_free(4,4) == True
    assert TT.is_free(4,2) == True

def test_is_free_outside_playarea():
    TT = TableTop()
    assert TT.is_free(-1,0) == False
    assert TT.is_free(0,-1) == False    
    assert TT.is_free(6,4) == False
    assert TT.is_free(4,8) == False
    
def test_place_object_valid_placement():
    TT = TableTop()    
    assert TT.place_object("Test str") == True
    assert TT.place_object("Test str","NORTH",3,2) == True
    assert TT.place_object("Test str","SOUTH",2,4) == True
    assert TT.place_object("Test str","EAST",1,3) == True
    assert TT.place_object("Test str","WEST",0,1) == True
    
def test_place_object_invalid_placement():
    TT = TableTop()    
    assert TT.place_object("Test str","fffs") == False
    assert TT.place_object("Test str","NssORTH",3,2) == False
    assert TT.place_object("Test str","SOUTH",6,4) == False
    assert TT.place_object("Test str","EAST",1,6) == False
    assert TT.place_object("Test str","WEasdgfST",0,6) == False
    
def test_remove_object_position_occupied():
    TT = TableTop()
    TT.place_object("Test str","NORTH",3,2)
    assert TT.remove_object(3,2) == True

def test_remove_object_position_unoccupied():
    TT = TableTop()
    assert TT.remove_object(3,2) == False
    
def test_find_object_object_exists_on_playfield():
    TT = TableTop()
    TT.place_object("test","NORTH",3,2)
    location = TT.find_object("test")
    assert location["column"] == 2
    assert location["row"] == 3
    assert location["facing"] == "NORTH"
    
def test_find_object_object_notexists_on_playfield():
    TT = TableTop()
    location = TT.find_object("test")
    assert location == False
    
def test_rotate_object():
    TT = TableTop()
    TT.place_object("test","NORTH",3,2)
    TT.rotate_object("test",1)
    location = TT.find_object("test")
    assert location["facing"] == "EAST"

    TT.rotate_object("test",2)
    location = TT.find_object("test")
    assert location["facing"] == "WEST"
    
    TT.rotate_object("test",3)
    location = TT.find_object("test")
    assert location["facing"] == "SOUTH"
    
    TT.rotate_object("test",4)
    location = TT.find_object("test")
    assert location["facing"] == "SOUTH"
    
    TT.rotate_object("test",5)
    location = TT.find_object("test")
    assert location["facing"] == "WEST"
    
    TT.rotate_object("test",-1)
    location = TT.find_object("test")
    assert location["facing"] == "SOUTH"

    TT.rotate_object("test",-2)
    location = TT.find_object("test")
    assert location["facing"] == "NORTH"
    
    TT.rotate_object("test",-3)
    location = TT.find_object("test")
    assert location["facing"] == "EAST"
    
    TT.rotate_object("test",-4)
    location = TT.find_object("test")
    assert location["facing"] == "EAST"
    
    TT.rotate_object("test",-5)
    location = TT.find_object("test")
    assert location["facing"] == "NORTH"
    
    
    
    
    