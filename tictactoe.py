#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 23:07:44 2021

@author: path
"""

import numpy as np
import pandas as pd
import random, pprint
from scipy.ndimage.interpolation impot shift


# ai modules
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD

class TicTacToe(object):
    
    def __init__(self):
        
        # 1: player1, 0: player0, 2: available
        self.board = np.full((3,3), 2)
        
    #who is start first
    def whoStart(self):
        turn = np.random.randint(0,2 size=1)
        
        if turn == 0:
            self.activePlayer = 0
        elif turn == 1:
            self.activePlayer = 1
            
        return self.activePlayer
        
    #move
    def move(self):
        if self.board[coord] !=2 or self.gameStatus() != 'In Progress' or self.activePlayer != player:
            raise ValueError('Geçersiz Hamle')
        
        self.board[coord] = player
        self.activePlayer = 1 - player
        
        return self.gameStatus(), self.board
    
    def gameStatus(self):
        # win - for row
        for i in range(self.board.shape[0]):
            if 2 not in self.board[i, :] and len(set(self.board[i,:])) == 1:
                return 'Win'
            
        
        # win - for column
        for j in range(self.board.shape[1]):
            if 2 not in self.board[:, j] and len(set(self.board[:, j])) == 1:
                return 'Win'
            
        # win - for cross
        if 2 not in np.diag(self.board) and len(set(np.diag(self.board))) == 1:
            return 'Win'
        
        # win - for cross / other
        if 2 not in np.diag(np.fliplr(self.board)) and len (set(np.diag(np.fliplr(self.board)))) == 1:
            return "Win"
        
        # scorless
        if 2 not in self.board:
            return 'scorless'
        else:
            return 'In rogress'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        