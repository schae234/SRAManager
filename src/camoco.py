#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>


import os
from flat import FlatCamoco  
from reference import Reference
from study import Study
import pickle as pickle

class CamocoError(Exception):
    pass

class Camoco(object):
    '''Camoco is a SRA project management system'''

    def __init__(self, working_dir="~/.camoco" ):
        '''constructor for camoco class'''
        self.wdir = os.path.expanduser(working_dir)
        self.title = ""
        self.accession = ""
        self.options = {}
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
        os.chdir(self.wdir)
        # try loading saved Camoco projects
        if os.access(self.wdir+"/camoco.p",os.R_OK):
            self.load()
        
    def add_study(self, study):
        '''Add a new study to the class'''
        try:
            assert isinstance(study,Study)
        except AssertionError as e:
            raise CamocoError("Unable to add Study: {}".format(str(e)))
        else:
            self.studies.add(study)

    def add_reference(self, reference):
        ''' Add a new Reference to the class'''
        try:
            assert isinstance(reference, Reference )
        except AssertionError as e:
            raise CamocoError("Unable to add Reference: {}".format(str(e)))
        else:
            self.references.add(reference)

    def del_reference(self, label):
        ''' remove a reference by label '''
        current_length = len(self.references)
        self.references = self.references.difference(
            set([x for x in self.references if self.label == label])
        )
    
    def add_sample(self, Sample):
        ''' add a new Sample to the class '''
        try:
            assert isinstance(Sample, 'Sample')
        except AssertionError as e:
            raise CamocoError("non Sample class instance added")
        else:
            self.samples.add(Sample)

    '''
        Camoco Class Specific Methods
    '''

    def import_file(self, path): 
        ''' Load a camoco class from a flat file '''
        with FlatCamoco(path) as f:
            self.__dict__.update(f.expand())

    def export_file(self, path):
        ''' write a camoco class to a flat file '''
        
    def save(self, path=None):
        ''' this saves the camoco to the working directory '''
        with open(self.wdir+"/camoco.p",'wb') as f:
            pickle.dump(self, f)

    def load(self,path=None):
        with open(self.wdir+"/camoco.p",'rb') as f:
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

