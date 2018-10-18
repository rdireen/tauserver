# Library for running the wooden server
# 10/13/2018

# Pixel alignment

# Top window:      (0, 0) (0, 1) (0, 2)
# Top bar:         (1, 0) (1, 1) (1, 2)
# Middle window:   (2, 0) (2, 1) (2, 2)
# Middle bar:      (3, 0) (3, 1) (3, 2)
# Bottom window:   (4, 0) (4, 1) (4, 2)
# Bottom bar:      (5, 0) (5, 1) (5, 2)

import opc
import time


class TauLibs:
    def __init__(self):

        self.client = opc.Client('localhost:7890')


        self.topw = [(0, 0, 0)]*3
        self.topb = [(0, 0, 0)]*4
        self.middlew = [(0, 0, 0)] *4
        self.middleb = [(0, 0, 0)]*4
        self.bottomw = [(0, 0, 0)]*4
        self.bottomb = [(0, 0, 0)] *3

        self.outv = self.topw + self.topb + self.middlew + self.middleb + self.bottomw + self.bottomb


    def set_pixel(self, color, row, col):
        if(row == 0):
            self.topw[col] = color
        elif(row == 1):
            self.topb[3 - col] = color
        elif(row == 2):
            self.middlew[col + 1] = color
        elif(row == 3):
            self.middleb[3 - col] = color
        elif(row == 4):
            self.bottomw[col + 1] = color
        elif(row == 5):
            self.bottomb[2 - col] = color 

        self.outv = self.topw + self.topb + self.middlew + self.middleb + self.bottomw + self.bottomb


    def set_row(self, color, row):
        if(row == 0):
            self.topw[0] = color
            self.topw[1] = color
            self.topw[2] = color
        elif(row == 1):
            self.topb[1] = color
            self.topb[2] = color
            self.topb[3] = color
        elif(row == 2):
            self.middlew[1] = color
            self.middlew[2] = color
            self.middlew[3] = color
        elif(row == 3):
            self.middleb[1] = color
            self.middleb[2] = color
            self.middleb[3] = color
        elif(row == 4):
            self.bottomw[1] = color
            self.bottomw[2] = color
            self.bottomw[3] = color
        elif(row == 5):
            self.bottomb[0] = color 
            self.bottomb[1] = color 
            self.bottomb[2] = color 
        
        self.outv = self.topw + self.topb + self.middlew + self.middleb + self.bottomw + self.bottomb

    def clear(self):
        self.topw = [(0, 0, 0)]*3
        self.topb = [(0, 0, 0)]*4
        self.middlew = [(0, 0, 0)] *4
        self.middleb = [(0, 0, 0)]*4
        self.bottomw = [(0, 0, 0)]*4
        self.bottomb = [(0, 0, 0)] *3
        self.outv = self.topw + self.topb + self.middlew + self.middleb + self.bottomw + self.bottomb
   
    def render(self):
        self.client.put_pixels(self.outv)
    
