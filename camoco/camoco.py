#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>


import os
from flat import FlatCamoco  
import pickle

class CamocoError(Exception):
    pass

class Camoco(object):
    '''Camoco is a SRA project management system'''
    wdir = "~/.camoco"
    title = ""
    accession = ""
    options = {}
    references = set()
    studies    = set()
    samples    = set()

    def __init__(self, working_dir="~/.camoco" ):
        '''constructor for camoco class'''
        self.wdir = os.expanduser(working_dir)
        # Check the the working directory is valid
        if not os.path.exists(self.wdir):
            # Try to create the dir
            try: 
                os.mkdir(wdir)
            except: PermissionError 
                sys.stderr.write("ERROR!: Cannot Open provided working dir: {}".format(working_dir))
        # Change to that Dir
        os.chdir(self.wdir)
        
        
    def add_study(self, Study):
        '''Add a new study to the class'''
        assert isInstance(Study,"Study")
        self.studies.add(Study)

    def add_reference(self, Reference):
        ''' Add a new Reference to the class'''
        assert isInstance(Reference, "Reference" )
        try:
            self.references.add(Reference)
        except ReferenceError as e:
            raise CamocoError("Unable to add Reference: {}".format(str(e)))
    
    def add_sample(self, Sample):
        ''' add a new Sample to the class '''
        assert isInstance(Sample, 'Sample')
        self.samples.add(Sample)

    def load_Flatfile(self, path): 
        ''' Load a camoco class from a flat file '''
        with FlatCamoco(path) as f:
            self = f.expand()

    def save_Flatfile(self, path):
        ''' write a camoco class to a flat file '''


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
