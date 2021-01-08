import pandas as pd
import numpy as np

# Load the contacts file from Clio
contacts = pd.read_csv(#'file path')
contacts.rename(columns={'ID': 'clientid'}, inplace=True)

# Load the matters file
matters = pd.read_csv(#'file path')
matters.rename(columns={'Client ID': 'clientid'}, inplace=True)

# Merge the files based on clientid
idsr = pd.merge(contacts, matters, how='inner', on='clientid')

# Remove timestamp from the contact and matter created date columns
idsr.rename(columns={'Created Date': 'Matter Created Date'}, inplace=True)
idsr['Matter Created Date'] = idsr['Matter Created Date'].str[:11]
idsr['Contact Created Date'] = idsr['Contact Created Date'].str[:11]

# Keep only first part of Zip
idsr['Primary Address Postal/Zip Code'] = idsr['Primary Address Postal/Zip Code'].str[:5]

#Regions
BayArea = {
    'CA - Alameda County',
    'CA - Contra Costa County',
    'CA - Marin County',
    'CA - Napa County',
    'CA - San Francisco County',
    'CA - San Mateo County',
    'CA - Santa Clara County',
    'CA - Solano County',
    'CA - Sonoma County'
}

CentralCoast = {
    'CA - Monterey County',
    'CA - San Luis Obispo County',
    'CA - Santa Cruz County'
}

CentralValley = {
    'CA - Alpine County',
    'CA - Amador County',
    'CA - Calaveras County',
    'CA - El Dorado County',
    'CA - Fresno County',
    'CA - Inyo County',
    'CA - Kern County',
    'CA - Kings County',
    'CA - Madera County',
    'CA - Mariposa County',
    'CA - Merced County',
    'CA - Mono County',
    'CA - Sacramento County',
    'CA - San Benito County',
    'CA - San Joaquin County',
    'CA - Stanislaus County',
    'CA - Tulare County',
    'CA - Tuolumne County',
    'CA - Yolo County'
}

SouthCarolina = {
    'SC - Abbeville County',
    'SC - Aiken County',
    'SC - Allendale County',
    'SC - Anderson County',
    'SC - Bamberg County',
    'SC - Barnwell County',
    'SC - Beaufort County',
    'SC - Berkeley County',
    'SC - Calhoun County',
    'SC - Charleston County',
    'SC - Cherokee County',
    'SC - Chester County',
    'SC - Chesterfield County',
    'SC - Clarendon County',
    'SC - Colleton County',
    'SC - Darlington County',
    'SC - Dillon County',
    'SC - Dorchester County',
    'SC - Edgefield County',
    'SC - Fairfield County',
    'SC - Florence County',
    'SC - Georgetown County',
    'SC - Greenville County',
    'SC - Greenwood County',
    'SC - Hampton County',
    'SC - Horry County',
    'SC - Jasper County',
    'SC - Kershaw County',
    'SC - Lancaster County',
    'SC - Laurens County',
    'SC - Lee County',
    'SC - Lexington County',
    'SC - Marion County',
    'SC - Marlboro County',
    'SC - McCormick County',
    'SC - Newberry County',
    'SC - Oconee County',
    'SC - Orangeburg County',
    'SC - Pickens County',
    'SC - Richland County',
    'SC - Saluda County',
    'SC - Spartanburg County',
    'SC - Sumter County',
    'SC - Union County',
    'SC - Williamsburg County'
    'SC - York County'
}

NorCal = {
    'CA - Butte County',
    'CA - Colusa County',
    'CA - Del Norte County',
    'CA - Glenn County',
    'CA - Humboldt County',
    'CA - Lake County',
    'CA - Lassen County',
    'CA - Mendocino County',
    'CA - Modoc County',
    'CA - Nevada County',
    'CA - Placer County',
    'CA - Plumas County',
    'CA - Shasta County',
    'CA - Sierra County',
    'CA - Siskiyou County',
    'CA - Sutter County',
    'CA - Tehama County',
    'CA - Trinity County',
    'CA - Yuba County'
}

SoCal = {
    'CA - Imperial County',
    'CA - Los Angeles County',
    'CA - Orange County',
    'CA - Riverside County',
    'CA - San Bernardino County',
    'CA - San Diego County',
    'CA - Santa Barbara County',
    'CA - Ventura County'
}

OutOfState = {'Out of State County (please specify)'}

region = {
    'Bay Area': BayArea,
    'Central Coast': CentralCoast,
    'Central Valley': CentralValley,
    'NorCal': NorCal,
    'SoCal': SoCal,
    'South Carolina': SouthCarolina,
    'Out of State': OutOfState
}

# Map regions to county
d1 = {k: oldk for oldk, oldv in region.items() for k in oldv}
idsr['Region'] = idsr['County'].map(d1)

# Write to csv
idsr.to_csv(#'destination file path', index=False)