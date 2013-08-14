#!/usr/bin/python3
# Copyright 2013 Rob Schaefer <schae234@gmail.com>

import curses

class Camoco(object):
    '''Camoco is a SRA project management system'''
    studies = ()
    screen_ui = 0
    working_dir = "~/.camoco"

    def __init__(self, working_dir="~/.camoco" ):
        '''constructor for camoco class'''
        self.working_dir = working_dir
        
    def add_study(self, study):
        '''Add a new study to '''

    def load_study(self, study_accession):
        '''load a study from the working directory'''

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

            if self.screen_ui == 1:
                curses.endwin()
                screen.addstr("Study Added")
            elif self.screen_ui == 2 :
                curses.endwin()
                screen.addstr("Study Loaded")
            else:
                curses.endwin()
                screen.addstr("Invalid input!")
               
        curses.endwin()
