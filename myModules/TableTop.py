# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:34:35 2021

 TableTop Class
 This class represents a TableTop that objects such as ToyRobot can be placed on
 default size is 5x5 

Attributes
-----------
play_area : list
    a multidimensional list that stores objects currently in play on the table

facing_direction : list
    a list of the valid facing directions for objects on the table
    
Methods
   is_free(row,column) 
       returns if position on play_area defined by row,column is free or not
   
   place_object(self,theObj,facing = "NORTH", row = 0,column = 0)
       Will place an object on play_area at position row,column facing a direction indicated by facing
   
   remove_object(row,column)
       will remove whatever object is in row,column position on play_are

   find_object(theObj)
       will find position and facing direction of theObj in play_area
       
   rotate_object(theObj,steps)
       will rotate theObj facing direction in play_area by steps amount

"""

class TableTop:
    def __init__(self, rows = 5, columns = 5):
        """
        

        Parameters
        ----------
        rows : Int, optional
            The size of the play area in rows. The default is 5.
        columns : Int, optional
            The size of the play area in columns. The default is 5.

        Returns
        -------
        None.

        """
        self.play_area = []
        self.facing_direction = ["NORTH","EAST","SOUTH","WEST"]

        #creating the play_area as a multidimensional list        
        for j in range(rows):
            column = []
            for i in range(columns):
                column.append(None)
            self.play_area.append(column)


    def is_free(self,row,column):
        """
        

        Parameters
        ----------
        row : Int
            row position in play area to remove object from.
        column : Int
            column position in play area to remove object from.

        Returns
        -------
        
        False 
            if object cant be removed or doesnt exist on play area or invalid row,column combination

        True 
            if object removed and row,column position set to None
        """
    # check if indexes are valid 
        if 0 <= row < len(self.play_area):
            if 0 <= column < len(self.play_area[0]):
                if self.play_area[row][column] is not None:
                    return False
                else:
                    # if code gets here nothing is in the desired position on play area
                    return True
        return False
    
    def place_object(self,theObj,facing = "NORTH", row = 0,column = 0):
        """
        

        Parameters
        ----------
        theObj : ToyRobot but could be any other object
            The object to be placed on the play_area.
        facing : str, optional
            a valid facing direction. The default is "NORTH".
        row : Int, optional
            row position to place the object. The default is 0.
        column : TYPE, optional
            column position to place the object. The default is 0.

        Returns
        -------
        True 
            if object successfully placed in play_area
        False 
            if object unsuccessfully placed in play_area

        """
        #check if position is occupied, use exception handling to capture invalid row,column indexes or other errors
        try :
            if self.is_free(row,column):
                self.play_area[row][column] = [theObj,self.facing_direction.index(facing)]
                return True
            else:
                return False
        #if an error occurs due to invalid row, column or other object placement will fail and return false            
        except:
            return False


    def remove_object(self,row,column):
        """
        

        Parameters
        ----------
        row : Int
            row position of where object to be removed is.
        column : TYPE
            column position of where object to be removed is.

        Returns
        -------
        True
            if object successfully removed.
        False
            if object unsuccessfully removed i.e wasnt in play_area
        
        """
        if self.play_area[row][column] is not None:
            self.play_area[row][column] = None
            return True
        else:
            return False

    def find_object(self,theObj):
        """
        

        Parameters
        ----------
        theObj : ToyRobot but could be any other object
            The object to search for in the play_area.

        Returns
        -------
        Dictionary
            after successfully finding theObj in play area it will return a dictionary object of the form {"row" : row, "column" : column, "facing" : facing}
        False
            failure to find theObj in play_area
        """
        for j in range(len(self.play_area)):
            for i in range(len(self.play_area[j])):
                if type(self.play_area[j][i]) == list:
                    if self.play_area[j][i][0] is theObj:
                        return {"row" : j,"column" : i,"facing" : self.facing_direction[self.play_area[j][i][1]]}
        return False

    def rotate_object(self,theObj,steps = 1):
        """
        

        Parameters
        ----------
        theObj : ToyRobot but could be other object
            The object on the play_area to be rotated.
        steps : Int, optional
            the number of steps rotate the object
            negative numbers indicate rotate anti-clockwise
            positive number indicate rotate clockwise
            The default is 1.

        Returns
        -------
        False
            returns false when object couldnt be roated because it is not on the play_area.
        True
            theObj was succesfully rotated on play_area
        """
        location = self.find_object(theObj)
        if location == False:
            return False
        else:
            self.play_area[location["row"]][location["column"]][1] = (self.facing_direction.index(location["facing"])+ steps) % len(self.facing_direction)
            return True