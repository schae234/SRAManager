#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

import os

class ReferenceError(Exception):
    pass

class Reference(object):
    label = ""
    path  = ""

    def __init__(self, label, path):
        self.label = label
        # check that the passed in path does exist
        try: 
            os.access(path, R_OK)
        except IOError as e:
           raise ReferenceError("Cannot ") 
