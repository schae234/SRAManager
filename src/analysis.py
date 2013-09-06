#!/usr/bin/python3

import camoco as camoco
import pypeline as pypeline

from pypeline.node import Node, CommandNode, MetaNode
from pypeline.atomiccmd.command import AtomicCmd
from pypeline.atomiccmd.sets import ParallelCmds
from pypeline.atomiccmd.builder import \
     create_customizable_cli_parameters, \
     use_customizable_cli_parameters, \
     AtomicCmdBuilder, \
     apply_options

class Analysis(object):
    ''' This class implements a analyis done on a camoco object
        Each instance of the class will be a different type of analysis
        which takes in a camoco instance as input and runs the actual
        analysis as implemented by the pypeline class. This makes
        the approach to running and extending different pypeline
        instances universal and easily extensible, especially in 
        relation to the short read archive.
    '''

    def __init__(self, camoco_inst, title=""):
        ''' constructor for analysis '''
        self.title = title
        self.nodes = []
        self.pypeline = pypeline.Pypeline() 
        self.camoco = camoco_inst
  
    def run(self):
        ''' Implement in Child Class '''

    def store(self):
        ''' store analysis results '''
 



class MappingAnalysis(Analysis):

    def __init__(self, camoco_inst, title):
        super(Analysis,self).__init__()
        self.nodes = [
            
        ] 


    def run(self):
        self.pypeline.add_nodes(self.nodes)
        self.pypeline.run()


class SRAMappingNode(CommandNode):
    @create_customizable_cli_parameters
    def customize(self, reference, in_sra, out_bam, dependencies = ()):

    @use_customizable_cli_parameters:
    def __init__(self, parameters):
        commands = [parameters.commands[k].finalize() for k in ("","")]
        description = "<>"
