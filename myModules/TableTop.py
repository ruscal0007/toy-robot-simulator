# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:34:35 2021


"""

# This class represents a tabletop that toy-robot objects can be placed on
# default size is 5x5 
# Python doesnt inheirently support arrays so using multidimensional list to represent the play area of the tabletop
# Should be able to store objects in row, column index of multidimension list so can accomodate for more than 1 robot in play area or other obstacles
class TableTop:
    def __init__(self, width = 5, length = 5):
        self.play_area = []
        for j in range(width):
            column = []
            for i in range(length):
                column.append(0)
            self.play_area.append(column)

    def showfield(self):
        self.play_area[3][4] = 3
        print(self.play_area)