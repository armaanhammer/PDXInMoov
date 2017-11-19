#!/bin/python
'''
This module contains an Inmoov Forearm

Authors:
    Brett Creeley
    Matty Baba "Black Sheep" Allos
    Dai Ho
'''
from Wrist import Wrist
from Hand import Hand

class Forearm(object):
    '''
    This class represents an Inmoov Forearm
    '''

    def __init__(self, pinky_channel, ring_channel, mid_channel,
                 index_channel, thumb_channel, wrist_channel):
        '''
        Build an Inmoov Forearm
        '''
        self.wrist = Wrist(wrist_channel)
        self.hand = Hand(pinky_channel, ring_channel, mid_channel, index_channel, thumb_channel)

    def rotate_wrist(self, degrees):
        '''
        Rotate the Wrist for this Hand
        '''
        self.wrist.rotate(degrees)