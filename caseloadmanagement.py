import pandas as pd
import numpy as np

#Load the contacts file
contacts = pd.read_csv('#filepath')
contacts.rename(columns={'ID': 'clientid'}, inplace=True)

#Load the matters file
matters = pd.read_csv('#filepath')
matters.rename(columns={'Client ID': 'clientid'}, inplace=True)

#Merge the contacts and matters
df = pd.merge(contacts, matters, how='inner', on='clientid')

#Remove timestamp from matter created
df.rename(columns ={'Created Date': 'Matter Created Date'}, inplace = True)
df['Matter Created Date'] = df['Matter Created Date'].str[:11]

#Replace empty responsible and originating attorney values with null
df["Responsible Attorney"] = df["Responsible Attorney"].replace(np.nan, "null")
df["Originating Attorney"] = df["Originating Attorney"].replace(np.nan, "null")

#Reorder columns
column_names = [
    "Number",
    "Status",
    "Responsible Attorney",
    "Originating Attorney",
    "Matter Created Date",
    "Open Date",
    "Close Date",
    "Pending Date",    
]

#Create a new dataframe using only the columns in the list
df = df.reindex(columns=column_names)

#Export the new dataframe as a csv
df.to_csv('/caseloadmanagement.csv', index=False)