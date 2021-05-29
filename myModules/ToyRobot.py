# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:54:59 2021

@author: ben
"""

class ToyRobot:
    def __init__(self, TT):
        self.PlayTable = TT
#This Toy Robot moves one square ahead in the direction it is facting when the MOVE command is called
#How the Robot moves is goverened here, you may have robots that move in a different manner so they shouldnt have that logic in the TableTop
    def move(self):
        #where is the robot currently
        location = self.PlayTable.find_object(self)
        if location == False:
            return False
        else:
            #Work out where the robots destination is
            if location["facing"] == "NORTH":
                destination_row = location["row"] 
                destination_column = location["column"] + 1
            elif location["facing"] == "SOUTH":
                destination_row = location["row"] 
                destination_column = location["column"] - 1
            elif location["facing"] == "EAST":
                destination_row = location["row"] + 1
                destination_column = location["column"] 
            elif location["facing"] == "WEST":    
                destination_row = location["row"] -1
                destination_column = location["column"] 
            # if the robot is successfully moved to the new location we can then free the old location
            # if the robot cant be placed in the new location it stays in the old
            if self.PlayTable.place_object(self,location["facing"], destination_row,destination_column):
                self.PlayTable.remove_object(location["row"],location["column"])
                return True
            else:
                return False
    
    def place(self,facing = "NORTH",row = 0 ,column = 0):
        return self.PlayTable.place_object(self,facing,row,column)
    
    #Function to rotate robot left(anti-clockwise) on the TableTop     
    def rotate_left(self):
        if self.PlayTable.rotate_object(self,-1):
            return True
        else:
            return False

    #Function to rotate robot right(clockwise) on the TableTop     
    def rotate_right(self):
        if self.PlayTable.rotate_object(self,1):
            return True
        else:
            return False
        
    def report(self):
        location = self.PlayTable.find_object(self)
        if location == False:
            print("ToyRobot not placed on table")
        else:
            print(str(location["row"]) + "," + str(location["column"])  + "," + location["facing"])
            