# Language Translator
import pandas as pd
import numpy as np
import os
os.chdir('C:/Users/jafris/Documents/Python Scripts')
from googletrans import Translator  # Import Translator module from googletrans package
Source= []
df = pd.read_csv('Account_Names.csv')
# df.head(50)
translator = Translator() # Create object of Translator.
for i in df['Account Name']:
    try:
        translated = translator.translate(i)
        Source.append(translated.text)
    except:
        pass
df['Account Name_Trans'] = Source
df.head()
