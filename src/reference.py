#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

import os


class ReferenceError(Exception):
    pass
class Reference(object):

    def __init__(self, label, path):
        self.label = label
        self.path = path
        # check that the passed in path does exist
        try: 
            os.access(path, os.R_OK)
        except IOError as e:
           raise ReferenceError("Cannot open reference file: {}".format(path)) 
