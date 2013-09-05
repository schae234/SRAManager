#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

from experiment import Experiment

class StudyError(Exception):
    ''' Define error class for handling Study exceptions '''
    pass

class Study(object):
    """Implements a SRA Study Object. Identifies the sequencing study
       or project and may contain multiple Experiments. This class is
        simply a container for organizing and staging analyses which
        accept Camococ sub classes """
    
    def __init__(self, accession, title=None, submitter=None,experiments=set() ):
        '''constructor for Study class'''
        self.accession = accession
        self.title = title
        self.submitter = submitter
        self.experiments = experiments
    
    def __len__(self):
        return len(self.experiments)

    def add_experiment(self,experiment):
        ''' safely add an experiment instance to the study'''
        try:
            assert isinstance(experiment, Experiment)    
        except AssertionError as e:
            raise StudyError("Attempted to add non experiment instance to study")
        else:
            self.experiments.add(experiment)
        

