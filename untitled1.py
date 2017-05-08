#!/usr/bin/env python
import pickle
import rospy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sensor_msgs.msg import LaserScan
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':

    laser_data = pickle.load( open( "laser_scan_data_training_set2", "rb"))
    comments = pickle.load( open( "comments_training_set2", "rb"))
    print len(comments)
    labels = {'15_0':0, '30_0':1, '45_0':2, '15_l':3, '30_l':4,'45_l':5, '15_r':6, '30_r':7, '45_r':8, 'empty':9}
              
    for i in range(len(comments)):
        plt.figure(i)
        
        plt.subplot(211)
        plt.plot(laser_data[i].ranges, 'b')
        plt.title(comments[i])
        plt.ylabel('Range')
        
        plt.subplot(212) 
        plt.plot(laser_data[i].intensities, 'r') 
        plt.ylabel('Intensitie')
        
        plt.show()
    
#    for i in range(len(comments)):
#        if i !=0:
#            
#                plt.figure(len(comments)+i)
#                plt.subplot(211)
#                plt.title(comments[i] + " - empty space in front")
#                plt.plot(np.subtract(laser_data[i].ranges, laser_data[0].ranges), 'b')
#                plt.ylabel('Range')
#                plt.subplot(212) 
#                plt.plot(np.subtract(laser_data[i].intensities, laser_data[0].intensities), 'r') 
#                plt.ylabel('Intensitie')
#
#    print "Angle Min: %f " % laser_data[0].angle_min
#    print "Angle Max: %f " % laser_data[0].angle_max
#    print "Angle Increment: %f " %  laser_data[0].angle_increment
#                                        
#    print "Range Min: %f" % laser_data[0].range_min
#    print "Range max: %f" % laser_data[0].range_max



