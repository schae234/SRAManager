#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

from sample import Sample

class Experiment(object):
    ''' An experiment holds meta data on Runs from a 
        certain Experiment. It can hold important
        information on conditions and technological specifications 

        YAML:
           - Title: "Zea mays ssp. mays L. Tzi8 seedling root RNA-Seq"
             Accession: SRX129813
             Instrument: Illumina HiSeq 2000
             Sample: SRS300579
             Runs: 
                - SRR445655

'''
    samples = set()

    def __init__(self, accession, title=None, instrument=None, sample=None, runs=set()):
        ''' constructor for Experiment class '''
        self.accession = accession
        self.title = title
        self.instrument = instrument
        self.runs = runs
       
    def add_run(self, run):
        ''' add a run to the experiment '''
        try:
            assert isinstance(run, Run)
        except AssertionError as e:
            raise ExperimentError("Attempted to add non run instance")
        else:
            self.runs.add(run) 

    def add_sample(self,sample):
        ''' experiments can share samples '''
        try: 
            assert isinstace(sample, Sample)
        except AssertionError as e:
            raise ExperimentError("Attempted to add non sample instance")
