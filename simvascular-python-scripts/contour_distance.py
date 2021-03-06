#!/usr/bin/env python

"""
This script defines the 'ContourDistance' class used to compute the distance between 
the centers of two contours for a segmentation generated by the SimVascular 
'SV 2D Segmentation' tool.

A Path name corresponds to a data node under the SimVascular 
'SV Data Manager' 'Paths' node. 

To use the script from SimVascular Python Console

  1) Open the SimVascular Python Console
  2) Select the 'Text Editor' tab at the bottom the console panel
  3) Read in the contour_distance.py script using the 'Load script from disk' button
  4) Execute the script by selecting the 'Run the current script' (play) button 

Example: Using 'ContourDistance' for the SimVascular DemoProject

## Create contours IDs for the SV Data Manager Segmentations 
#  'aorta' data node into the Data Manager Repository.
#
# The number of contours are the number of contours defined in the
# 'SV 2D Segmentation' 'Contour List:'. 
#
seg_name = 'aorta'
num_contours = 39
contour_ids = list(range(num_contours))

# Create a ContourDistance object with contour_ids.
contour = ContourDistance(seg_name, contour_ids)

# Calculate the distance between contour centers.
id1 = 4
id2 = 20
contour.dist(id1,id2)

"""

from sv import *
import vtk
import math

class ContourDistance(object):
    """ This class is used to calculate distances between contour centers.
    """
    def __init__(self, seg_name, contour_ids):
        """ Initialize the ContourDistance object

        Args:
            seg_name (string): The name of a SimVascular Segmentation data node.
            contour_ids(list[int]): The list of contour IDs for the segmentation.
        """
        self.seg_name = seg_name
        self.contour_ids = contour_ids 
        print('[ContourDistance] Repository name: {0:s}'.format(self.seg_name))
        self.repo_contour_ids = [seg_name+'_contour_'+str(i) for i in contour_ids]
        print('[ContourDistance] Number of contour IDs: {0:d} '.format(len(self.repo_contour_ids)))

        # Add the Path to the Repository.
        try:
            GUI.ExportContourToRepos(self.seg_name, self.repo_contour_ids)
            print("[ContourDistance] Add '{0:s}' to the repository.".format(self.seg_name))
        except:
            pass

        #print('[ContourDistance] Repository: {0:s}'.format(' '.join(Repository.List())))
        self.calc_centers()

    def calc_centers(self):
        """ Calculate the contour centers.

        Create a VTK center of mass filter to calculate contour centers.
        """
        centers = []
        for id in self.repo_contour_ids:
            print(id)
            contour = Repository.ExportToVtk(id)
            com_filter = vtk.vtkCenterOfMass()
            com_filter.SetInputData(contour)
            com_filter.Update()
            center = com_filter.GetCenter()
            centers.append(center)
        #_for id in self.repo_contor_ids
        self.centers = centers
    #_calc_centers(self)

    def dist(self, id1, id2):
        """ Calculate the distance between two contour centers.
        """
        if (id1 < 0) or (id1 > len(self.centers)-1):
            print("[ContourDistance] id1 '{0:3d}' is out of range".format(id1))
            return

        if (id2 < 0) or (id2 > len(self.centers)-1):
            print("[ContourDistance] id2 '{0:3d}' is out of range".format(id2))
            return

        dist = 0.0
        for id in range(id1,id2):
            c1 = self.centers[id];
            c2 = self.centers[id+1];
            distSquared = vtk.vtkMath.Distance2BetweenPoints(c1,c2)
            dist += math.sqrt(distSquared)
        #_for id in range(id1,id2)
        print("[ContourDistance] Distance between IDs '{0:3d}' and '{1:3d}' is {2:f}".format(id1, id2, dist))
    #_dist(self, id1, id2)
#_class ContourDistance(object)

