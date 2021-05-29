# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:54:59 2021

@author: ben
"""

class ToyRobot:
    def __init__(self,name):
        self.name = name

#This Toy Robot moves one square ahead in the direction it is facting when the MOVE command is called
#How the Robot moves is goverened here, you may have robots that move in a different manner so they shouldnt have that logic in the TableTop
    def move(self,TTobj):
        #where is the robot currently
        location = TTobj.find_object(self)
        #Work out where the robots destination is
        if location["facing"] == "NORTH":
            destination_row = location["row"] + 1
            destination_column = location["column"]
        elif location["facing"] == "SOUTH":
            destination_row = location["row"] - 1
            destination_column = location["column"]
        elif location["facing"] == "EAST":
            destination_row = location["row"]
            destination_column = location["column"] + 1
        elif location["facing"] == "WEST":    
            destination_row = location["row"] 
            destination_column = location["column"] -1
        # if the robot is successfully moved to the new location we can then free the old location
        # if the robot cant be placed in the new location it stays in the old
        if TTobj.place_object(self,location["facing"], destination_row,destination_column):
            TTobj.remove_object(location["row"],location["column"])
    
    def place(self,TTobj,facing = "NORTH",row = 0 ,column = 0):
        return TTobj.place_object(self,facing = "NORTH", row = 0,column = 0)
    def rotate_left(self,TTobj):
        return 
            