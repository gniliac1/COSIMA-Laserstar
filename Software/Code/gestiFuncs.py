# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:06:09 2018

@author: Cailing
"""

#import userModel

def loadUser( fileName='data/test.usr' ) :
    myUser = userModel.UserModel( fileName )
    return myUser
	
def readIntgersFromSerialPort(port,nIntegers):
	"This function reads in a message consisting of nIntegers integer data from a specified serial port"
	# wait for valid data
	while True:
		# try to read data
		newData = port.readline()
		# if data has been received
		if newData:
			# try to decode the string
			newData = newData.decode("ascii").split(" ")
			# check whether the data is valid and consists of nIntegers integers
			if len(newData) == nIntegers:
				# received data is valid, so leave the loop and process the data
				break
	return newData