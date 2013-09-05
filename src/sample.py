#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>


class Sample(object):
    ''' An object which descripted an experimental Sample'''
    def __init__(self, accession, title=None):
        self.accession = accession
        self.title = title
