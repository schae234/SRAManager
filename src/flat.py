#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

import os
import yaml

class FlatCamocoError(Exception):
    pass

class FlatCamoco(object):
    ''' Defines a FlatFile for a Camoco Class '''
    def __init__(self, path):
        try:
            self = yaml.load(open(self.path,'r'))['Camoco']
        except Exception as e:
            raise FlatCamocoError("Failed to load flat file: {}".format(self.path))

    def __enter__(self):
        return(self)

    def __exit__(self, type, value, traceback):
        del(self.expanded)

    def __str__(self):
        return str(self.expanded)

    def expand(self):
       return 1 
