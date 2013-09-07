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
        # for each of the SRA, start a mapping node
        self.nodes = [
            
        ] 


    def run(self):
        self.pypeline.add_nodes(self.nodes)
        self.pypeline.run()


class SRAMappingNode(CommandNode):
    @create_customizable_cli_parameters
    def customize(self, reference, sra_infile, bam_outfile, ):
        ''' Customize CLI parameters for Mapping commands '''
        #------------------------------------------
        # Dump SRA file into fastq format
        #------------------------------------------
        fastq_dump = AtomicCmdBuilder(['fastq-dump', '%(IN_SRA)s'],
                            IN_SRA = infile,
                            TEMP_OUT_MATE1 = '',
                            TEMP_OUT_MATE2 = '',
                    ) 
        fastq_dump.set_option('')
        #------------------------------------------
        # Remove Adapters
        #------------------------------------------
        adapter_rm = AtomicCmdBuilder(['AdapterRemoval'],
                        TEMP_IN_READS_1 = '',
                        TEMP_IN_READS_2 = '',
                        TEMP_OUT_BASENAME = ''; 
                        TEMP_OUT_LINK_PAIR1 = '',
                        TEMP_OUT_LINK_PAIR2 = '',
                        TEMP_OUT_LINK_ALN = '',
                        TEMP_OUT_LINK_ALN_TRUNC = '',
                        TEMP_OUT_LINK_UNALN = '',
                        TEMP_OUT_LINK_DISC = '',
                    )
        # Allow 1/3 mismatches in the aligned region
        adapter_rm.set_option("--mm", 3, fixed = False)
        # Minimum length of trimmed reads
        adapter_rm.set_option("--minlength", 25, fixed = False)
        # Trim Ns at read ends
        adapter_rm.set_option("--trimns", fixed = False)
        # Trim low quality scores
        adapter_rm.set_option("--trimqualities", fixed = False)
        # Offset of quality scores
        adapter_rm.set_option("--qualitybase", 33, fixed = False)
        adapter_rm.set_option('--collapse')
        # Uncompressed mate 1 and 2 reads (piped from fastq-dump)
        adapter_rm.set_option("--file1", "%(TEMP_IN_READS_1)s")
        adapter_rm.set_option("--file2", "%(TEMP_IN_READS_2)s")
        # Prefix for output files, ensure that all end up in temp folder
        adapter_rm.set_option("--basename", "%(TEMP_OUT_BASENAME)s")
        # Output files are explicity specified, to ensure that the order is the same here
        # as below. A difference in the order in which files are opened can cause a deadlock,
        # due to the use of named pipes (see __init__).
        adapter_rm.set_option("--output1", "%(TEMP_OUT_LINK_PAIR1)s")
        adapter_rm.set_option("--output2", "%(TEMP_OUT_LINK_PAIR2)s")
        adapter_rm.set_option("--outputcollapsed", "%(TEMP_OUT_LINK_ALN)s")
        adapter_rm.set_option("--outputcollapsedtruncated", "%(TEMP_OUT_LINK_ALN_TRUNC)s")
        adapter_rm.set_option("--singleton", "%(TEMP_OUT_LINK_UNALN)s")
        adapter_rm.set_option("--discarded", "%(TEMP_OUT_LINK_DISC)s")

        # Return the commands
        return {
            "fastq_dump" = fastq_dump,
            "adapter_rm" = adapter_rm,
        }

    @use_customizable_cli_parameters:
    def __init__(self, parameters):
        commands = [parameters.commands[k].finalize() for k in ("fastq_dump","adapter_rm")]
        description = "<Mapping Pipeline>"

        CommandNode.__init__(self,
                             description  = description,
                             command      = ParallelCmds(commands),
                             dependencies = parameters.dependencies)
