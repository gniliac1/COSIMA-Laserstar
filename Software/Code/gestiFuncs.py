# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:06:09 2018

@author: Cailing
"""
import numpy as np

def loadUser( fileName ) :
    userFile = np.genfromtxt( fileName, dtype='str' )
    return userFile

userFile = loadUser('../data/user1.txt')

    