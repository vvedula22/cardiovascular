#!/usr/bin/env python

class Parameters():
    """ The Parameter class stores the input parameters.
    """
    FILE_NAME_SEP = "_"
    DATA_FILE_EXTENSION = ".dat"

    def __init__(self):
        self.data_names = None

        self.output_directory = None
        self.results_directory = None

        ## Solver parameters.
        self.solver_file_name = None
        self.model_name = None
        self.num_steps = None
        self.time_step = None
        self.times = None
        self.time_range = None

        self.segment_names = None
        self.all_segments = False
        self.outlet_segments = False

        self.output_file_name = None
        self.output_format = None 

        self.display_geometry = False
        self.node_sphere_radius = 0.1
