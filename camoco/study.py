#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>


class Study(object):
    """Implements a SRA Study Object. Identifies the sequencing study
       or project and may contain multiple Experiments"""
    experiments = ()
    
    def __init__(self, ):
        '''constructor for Study class'''
