#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

class Experiment(Run):
    ''' An experiment holds meta data on Runs from a 
        certain Experiment. It can hold important
        information on conditions and technological specifications '''

    instrument = None
    sample = None

    def __init__(self, accession, title, instrument, ):
       Run.__init__(self, accession, title) 

     def sample(self):
        assert isinstance(sample, Sample)
        self.sample = Sample


