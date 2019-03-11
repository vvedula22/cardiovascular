#!/usr/bin/env python

"""
This script computes the distance between the centers of two contours
for a segmentation generated by the SimVascular 'SV 2D Segmentation' 
module.

The script is read in from the SimVascular Python Console Text Editor.

"""

from sv import *
import vtk
import math

def calc_dist(id1, id2):
    """ Calculate the distance between two contour centers.
    """

    ## Get the contour centers.
    #
    # Create a VTK center of mass filter to calculate
    # contour centers.
    #
    centers = []
    for id in range(int(id1), int(id2)+1):
        contour = Repository.ExportToVtk(str(id))
        com_filter = vtk.vtkCenterOfMass()
        com_filter.SetInputData(contour)
        comm_filter.Update()
        center = com_filter.GetCenter()
        centers.append(center) 

    ## Calculate the distance between centers.
    dist = 0.0
    for id in range(0,len(pts)-1):
        c1 = centers[id];
        c2 = centers[id+1];
        distSquared = vtk.vtkMath.Distance2BetweenPoints(c1,c2)
        dist += math.sqrt(distSquared)

    print('>>> Distance between %s and %s = %f' % (id1, id2, dist))
   
## Put the contour IDs into the SV Python Repository.
#
num_contours = 38
ids = list(range(num_contours))
contour_ids = [str(i) for i in ids]

## Store the contours IDs for the Data Manager Segmentations 
#  'aorta' data node into the Data Manager Repository.
#
path_name = 'aorta'
try:
    GUI.ExportContourToRepos(path_name, contour_ids)
except:
   print('Repository already defined')

# Calculate the distance between contours.
calc_dist('1', '16')

