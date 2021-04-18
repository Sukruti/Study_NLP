import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()
print('The sentence is ...')
sentence="Facebook invented a new way to build computers and other data center hardware called the Open Compute " \
         "Project (OCP).\n This project has saved Facebook $1 billion in three years, CEO Mark Zuckerberg said, " \
         "plus Facebook offers the hardware designs to anyone who wants them, for free"
print(sentence)
doc = nlp(sentence)
print('Here is what Named Entity Recognization done NLP spacy Library...')
print([(X.text, X.label_) for X in doc.ents])
print(displacy.render(doc,style='ent'))

