#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

import os
import yaml
from camoco import *
from reference import Reference
from study import Study
from experiment import Experiment
from sample import Sample
from run import Run

class FlatCamocoError(Exception):
    pass

class FlatCamoco(object):
    ''' Defines a FlatFile for a Camoco Class '''
    def __init__(self, path):
        self.path = path
        try:
            self.yaml = yaml.load(open(self.path,'r'))['Camoco']
        except Exception as e:
            raise FlatCamocoError("Failed to load flat file: {}".format(self.path))

    def __enter__(self):
        return(self)

    def __exit__(self, type, value, traceback):
        del(self)

    def __str__(self):
        return str(self.expanded)

    @property
    def title(self):
        return self.yaml['Title']       

    @property
    def accession(self):
        return self.yaml['Accession']

    @property
    def options(self):
        return self.yaml['Options']  
    
    @property
    def references(self):
        return set(Reference(r['Label'],r['Path']) for r in self.yaml['References'])

    @property
    def samples(self):
        return set([Sample(s['Accession'],s['Title']) for s in self.yaml['Samples']])
    
    @property
    def studies(self):
        return set(Study(
            each_study['Accession'],
            title = each_study['Title'],
            submitter = each_study['Submitter'],
            experiments = set(
                Experiment(
                    each_exp['Accession'] ,
                    title = each_exp['Title'],
                    instrument = each_exp['Instrument'],
                    sample = each_exp['Sample'],
                    runs = set(
                        Run(
                            each_run['Accession'],
                            path = each_run['Path']) for each_run in each_exp['Runs']
                    )
                 ) for each_exp in each_study['Experiments']
            )
        ) for each_study in self.yaml['Studies'])
