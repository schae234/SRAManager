#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

class Run(object):
    ''' A run is a SRA object which contains raw data.
        It can be remote on NCBI servers which means methods
        need to download data to temp dir before running '''
    accession = None
    path = None

    def __init__(self, accession, path = None):
        self.accession = accession
        self.path = path
    
    @property
    def is_local(self):
        ''' returns true if file is locally stored '''
        return False if self.path == None else True

