# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:54:59 2021

 ToyRobot Class
 This class represents a ToyRobot
  

Attributes
-----------
PlayTable : TableTop
    PlayTable is the TableTop that the robot will be operating on

Methods
   move() 
       will move the robot forward one square in whatever direction it is facing
   
   place(facing = "NORTH",row = 0 ,column = 0)
       Will place ToyRobot on PlayTable play_area at position row,column facing a direction indicated by facing
   
   remove()
       will remove ToyRobot from PlayTable play_area

   rotate_left()
       will rotate anti-clockwise ToyRobot on PlayTable play_area
       
   rotate_right()
       will rotate clockwise ToyRobot on PlayTable play_area
      
   report()
       will report the ToyRobot current position and facing direction on PlayTable play_area

"""

class ToyRobot:
    def __init__(self, TT):
        """
        

        Parameters
        ----------
        TT : TableTop
            TableTop object that ToyRobot will operate on.

        Returns
        -------
        None.

        """
        self.PlayTable = TT

    def move(self):
        """
        

        Returns
        -------
        True
            if the ToyRobot successfully moves.
        False
            if the ToyRobot fails to move.

        """
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
        """
        

        Parameters
        ----------
        facing : Str, optional
            Valid facing direction must be listed in PlayTable.facing_direction. The default is "NORTH".
        row : Int, optional
            row position of PlayTable play_area where to place. The default is 0.
        column : Int, optional
            column position PlayTable play_area where to place. The default is 0.

        Returns
        -------
        True
            successfully placed ToyRobot on PlayTable play_area.
        False
            failed to play ToyRobot on PlayTable play_are.

        """
        # scope says PLACE can be executed multiple times
        location = self.PlayTable.find_object(self)
        if  location == False:
            return self.PlayTable.place_object(self,facing,row,column)
        else:
            #robots already on table so remove and replace
            self.PlayTable.remove_object(location["row"],location["column"])
            return self.PlayTable.place_object(self,facing,row,column)
        return False
    
    def remove(self):
        """
        

        Returns
        -------
        False
            Failed to remove from PlayTable because it wasnt in play_area.
        True
            Successfully removed from PlayTable play_area
        """
        #check to see if robot on TableTop
        location = self.PlayTable.find_object(self)
        if location == False:
            return False
        return self.PlayTable.remove_object(location["row"],location["column"])
    
    
    #Function to rotate robot left(anti-clockwise) on the TableTop     
    def rotate_left(self):
        """
        

        Returns
        -------
        True
            Rotation on PlayTable play_area successfull.
        False
            Rotation on PlayTable play_area failed.

        """
        if self.PlayTable.rotate_object(self,-1):
            return True
        else:
            return False

    #Function to rotate robot right(clockwise) on the TableTop     
    def rotate_right(self):
        """
        

        Returns
        -------
        True
            Rotation on PlayTable play_area successfull.
        False
            Rotation on PlayTable play_area failed.

        """

        if self.PlayTable.rotate_object(self,1):
            return True
        else:
            return False
        
    def report(self):
        """
        

        Returns
        -------
        Str
            Returns position of ToyRobot on PlayTable play_area as string of format  row,column,facing .
        False
            ToyRobot not found on PlayTable play_area

        """
        location = self.PlayTable.find_object(self)
        if location == False:
            return False
        else:
            return(str(location["row"]) + "," + str(location["column"])  + "," + location["facing"])
            