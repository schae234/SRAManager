#!/usr/bin/python3

from camoco import Camoco
from reference import Reference
from study import Study

# Load our Camoco instance
c = Camoco()

# Repeatedly adding these instances to the Camoco class wont hurt it
ZmB73_5a = Reference("Maize B73 Genome Build 5a","~/Codes/root_pipeline/pypeline/tests/data/rCRS.fasta")
c.add_reference(ZmB73_5a)

zeanome = Study("SRP011480", 
        title = "Zeanome",
        submitter = "Iowa State Univ.",
        experiments = set(
            Experiment("SRX129813",
                title = "Zea mays ssp. mays L. Tzi8 seedling root RNA-Seq",
                instrument = 'Illumina HiSeq 2000',
                sample = 'SRS300579',
                runs = set(
                    Run('SRR445655',path=""),
                )
            )
        )            
    )


zeanome.gt
c.add_study(zeanome)
