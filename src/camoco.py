#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>


import os
from flat import FlatCamoco  
from reference import Reference
from study import Study
from experiment import Experiment
from sample import Sample
from run import Run
import pickle as pickle

class CamocoError(Exception):
    pass

class Camoco(object):
    '''Camoco is a SRA project management system'''

    def __init__(self, working_dir="~/.camoco", title=None, accession=None):
        '''constructor for camoco class'''
        self.wdir = os.path.expanduser(working_dir)
        self.title = title
        self.accession = accession
        self.options = dict()
        self.references = set()
        self.studies    = set()
        self.samples    = set()
        # Check the the working directory is valid
        if not os.path.exists(self.wdir):
            # Try to create the dir
            try: 
                os.mkdir(self.wdir)
            except PermissionError as e: 
                sys.stderr.write("ERROR!: Cannot Open provided working dir: {}".format(working_dir))
        # Change to that Dir
        self.oldwd = os.getcwd()
        os.chdir(self.wdir)
        # try loading saved Camoco projects
        save = "{}/{}.cam".format(self.wdir,self.title)
        if os.access(save,os.R_OK) and os.stat(save).st_size > 0:
            self.load()

    def __str__(self):
       ''' String representation of class '''
       return '''Camoco {}'''.format(self.title)

    def add_study(self, study):
        '''Add a new study to the class'''
        try:
            assert isinstance(study,Study)
        except AssertionError as e:
            raise CamocoError("Unable to add Study: {}".format(str(e)))
        else:
            # Only add studies which haven't been added
            if study.accession not in [s.accession for s in self.studies]:
                self.studies.add(study)

    def add_reference(self, reference):
        ''' Add a new Reference to the class'''
        try:
            assert isinstance(reference, Reference )
        except AssertionError as e:
            raise CamocoError("Unable to add Reference: {}".format(str(e)))
        else:
            # Only add references with new paths
            if reference.path not in [r.path for r in self.references]:
                self.references.add(reference)

    def del_reference(self, label):
        ''' remove a reference by label '''
        current_length = len(self.references)
        self.references = self.references.difference(
            set([x for x in self.references if self.label == label])
        )
    
    def add_sample(self, sample):
        ''' add a new Sample to the class '''
        try:
            assert isinstance(sample, Sample)
        except AssertionError as e:
            raise CamocoError("non Sample class instance added")
        else:
            self.samples.add(sample)
    
    def add_samples(self, samples):
        ''' add a list of samples to the instance '''
        for s in samples:
            self.add_sample(s)

    ''' ---------------------------------------------------------
        Camoco Class Specific Methods
    '''

    @classmethod
    def yaml(self, yaml_file, working_dir="~/.camoco", title=None, accession=None):
        ''' ALT CONSTR: create a camoco class from a yaml file'''
        c = self(working_dir,title=title,accession=accession)
        with FlatCamoco(yaml_file) as fc:
            c = self(working_dir,title,accession)
            c.title = fc.title
            c.accession = fc.accession
            c.optiosn = fc.options
            c.references = fc.references
            c.samples = fc.samples
            c.studies = fc.studies
        return c 
        
    def save(self, path=None):
        ''' this saves the camoco to the working directory '''
        with open("{}/{}.cam".format(self.wdir,self.title),'wb') as f:
            try:
                pickle.dump(self, f)
            except pickle.PickleError as e:
                print("Failed to pickle: {}".format(e))

    def load(self,path=None):
        with open("{}/{}.cam".format(self.wdir,self.title),'rb') as f:
            p = pickle.load(f)
            self.__dict__.update(p.__dict__)

import curses

class Camoco_Curses_UI(Camoco):

    def __init__(self, working_dir="~/.camoco"):
        self.screen_state = 0
        Camoco.__init__(self, working_dir)
        ''' Start the UI '''
        self.start_curses_ui()

    def start_curses_ui(self):
        while self.screen_ui != ord('4'):
            screen = curses.initscr()
            screen.clear()
            screen.border(0)
            screen.addstr(2, 2, "Welcome to Camoco!(Press enter to continue...)")
            screen.addstr(4, 4, "1 - add study")
            screen.addstr(5, 4, "2 - load study")
            screen.addstr(6, 4, "3 - exit")
            screen.refresh()
            self.screen_ui = screen.getch()

            if self.screen_state == 1:
                curses.endwin()
                screen.addstr("Study Added")
            elif self.screen_state == 2 :
                curses.endwin()
                screen.addstr("Study Loaded")
            else:
                curses.endwin()
                screen.addstr("Invalid input!")
               
        curses.endwin()

