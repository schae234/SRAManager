#!/usr/bin/python3

from camoco import *
from analysis import *

# Load our Camoco instance
e = Camoco.yaml("/home/rob/Codes/root_pipeline/Camoco/tests/EColi.yaml",title="E.Coli_Test")

# Run a mapping analysis 

a = MappingAnalysis(camoco_inst=e, title="EColi Mapping") 
a.run()

