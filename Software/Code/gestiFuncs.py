# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:06:09 2018

@author: Cailing
"""
import userModel

def loadUser( fileName='../data/user1.txt' ) :
    myUser = userModel.UserModel( fileName )
    return myUser