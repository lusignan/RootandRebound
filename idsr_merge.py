import numpy as np
import pandas as pd

contacts = pd.read_csv('# contacts file path')
contacts.rename(columns={'ID': 'clientid'}, inplace=True)

matters = pd.read_csv('# matters file path')
matters.rename(columns={'Client ID': 'clientid'}, inplace=True)

idsr = pd.merge(contacts, matters, how='inner', on='clientid')

idsr.to_csv('# destination file path', index=False)


