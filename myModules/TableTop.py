# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:34:35 2021


"""

# This class represents a tabletop that toy-robot objects can be placed on
# default size is 5x5 
# Python doesnt inheirently support arrays so using multidimensional list to represent the play area of the tabletop
# Should be able to store objects in row, column index of multidimension list so can accomodate for more than 1 robot in play area or other obstacles
class TableTop:
    def __init__(self, rows = 5, columns = 5):
        self.play_area = []
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

#function to place object(could be robot or obstacle) on board for first time     
    def place_object(self,theObj,row = 0,column = 0):
#check if position is occupied
        if self.is_free(row,column):
            self.play_area[row][column] = theObj
        else:
            return False