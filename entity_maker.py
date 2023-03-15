## spacy version 3.3.0
import spacy
from spacy import displacy

ENT = [] ## Array of Entities i.e Text example -> "Artizence"
LABEL = [] ## Array of Label i.e Label example -> "ORG"


def entity_detector_maker(ENT,LABEL):
    entity_detector = spacy.blank("en")
    #Sample text
    patterns = [ ]
    #Create the EntityRuler
    ruler = entity_detector.add_pipe("entity_ruler")
    
    max_range = len(ENT)
    for i in range(0, max_range-1):
        patterns.append({"label":LABEL[i],"pattern": ENT[i]})

    ruler.add_patterns(patterns)

    return entity_detector

nlp = entity_detector(ENT,LABEL)

doc = nlp(preprocess(resume))
displacy.serve(doc, style="ent")

