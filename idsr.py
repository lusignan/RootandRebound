import numpy as np
import pandas as pd

contacts = pd.read_csv('/Users/zacdelusignan/Downloads/contacts_2020-12-11.csv')
contacts.rename(columns={'ID': 'clientid'}, inplace=True)

matters = pd.read_csv('/Users/zacdelusignan/Downloads/matters_2020-12-11.csv')
matters.rename(columns={'Client ID': 'clientid'}, inplace=True)

idsr = pd.merge(contacts, matters, how='inner', on='clientid')

idsr.to_csv('/Users/zacdelusignan/Desktop/2020-12-11_MERGE.csv', index=False)


