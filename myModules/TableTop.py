# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:34:35 2021


"""

# This class represents a TableTop that objects such as ToyRobot can be placed on
# default size is 5x5 
# The T
class TableTop:
    def __init__(self, rows = 5, columns = 5):
        self.play_area = []

# Valid facing directions in text stored in this list
# by storing the facing direction as the index of this list in play_area we can easily do rotation with +1 -1
        self.facing_direction = ["NORTH","EAST","SOUTH","WEST"]
        
        for j in range(rows):
            column = []
            for i in range(columns):
                column.append(None)
            self.play_area.append(column)

    def showfield(self):

#Print out the playfield in a nice format
#for now just dumping it, will fix later
        print(self.play_area)
        
    def is_free(self,row,column):
        if self.play_area[row][column] is not None:
            return False
        else:
            return True

#function to place object(could be robot or obstacle) on board facing in a certain direction
#facing direction is passed as a string but stored as an integer so rotation can be performed by incrementing or decrementing value     
    def place_object(self,theObj,facing = "NORTH", row = 0,column = 0):
#check if position is occupied
        if self.is_free(row,column):
            self.play_area[row][column] = [theObj,self.facing_direction.index(facing)]
            return True
        else:
            return False


#function to remove object from playboard
#returns false if there was no object to remove
#returns true if an object was removed
#either way the row,column at the end will contain None    
    def remove_object(self,row,column):
        if self.play_area[row][column] is not None:
            self.play_area[row][column] = None
        else:
            return False

#find the position of an object on the play area
    def find_object(self,theObj):
        for j in range(len(self.play_area)):
            for i in range(len(self.play_area[j])):
                if type(self.play_area[j][i]) == list:
                    if self.play_area[j][i][0] is theObj:
                        return {"row" : j,"column" : i,"facing" : self.facing_direction[self.play_area[j][i][1]]}
        return False
# rotate object on playfield , steps are positive for clockwise , steps are negative for anti-clockwise    
    def rotate_object(self,theObj,steps = 1):
        location = self.find_oject(theObj)
        self.play_area[location["row"]][location["column"]][1] = (self.facing_direction.index(location["facing"])+ steps) % len(self.facing_direction)