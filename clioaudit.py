import pandas as pd

#Load the contacts file
contacts = pd.read_csv('# path to contacts file')
contacts.rename(columns={'ID': 'clientid'}, inplace=True)

#Load the matters file
matters = pd.read_csv('# path to matters file')
matters.rename(columns={'Client ID': 'clientid'}, inplace=True)

#Merge the contacts and matters
df = pd.merge(contacts, matters, how='inner', on='clientid')

#Reorder columns
column_names = [
    "Number",
    "Status",
    "Responsible Attorney",
    "Originating Attorney",
    "Created Date",
    "Open Date",
    "Close Date",
    "Pending Date",
    "Primary Address City",
    "Primary Address Province",
    "Primary Address Postal/Zip Code",
    "County",
    "Birth Date",
    "Sex/ Gender Identity",
    "Race / Ethnicity",
    "Asian/Pacific Islander",
    "Languages Spoken",
    "Education Completed?",
    "# of children under 18 at home",
    "Sexual Orientation",
    "Practice Area",
    "Convictions & System Involvement",
    "Last Release or Parole Date",
    "Identity- FIP",
    "Identity- CIP",
    "Identity-Record (No jail/prison)",
    "Identity- Community Svc Provider",
    "Identity- Educator",
    "Identity- Attorney",
    "Identity- Com. Supervision Ofcr.",
    "How Heard about R&R",
    "Referred by which agency/person?",
    "Disablity?",
    "Disability Status?",
    "ARC",
    "Time for Change",
    "FRWEI",
    "CCWF Prison Program",
    "CCC Prison Program",
    "ID & Voting (Issue)",
    "Parole/Probation (Issue)",
    "Housing (Issue)",
    "Public Benefits (Issue)",
    "Employment (Issue)",
    "Court Ordered Debt (Issue)",
    "Family & Children (Issue)",
    "Education (Issue)",
    "Record Cleaning (Issue)",
    "Occupational Licensing (Issue)",
    "Immigration (Issue)",
    "CrimDef/Prison/Warrant (Issue)",
    "Description",
    "ID-Outcome 1",
    "ID-Outcome 2",
    "ID-Outcome 3",
    "ID-Outcome 4",
    "ID-Outcome 5",
    "Voting- Outcome 1",
    "Voting- Outcome 2",
    "Voting- Outcome 3",
    "CS and 290 Outcome 1",
    "CS and 290 Outcome 2",
    "CS and 290 Outcome 3",
    "CS and 290 Outcome 4",
    "CS and 290 Outcome 5",
    "Record Cleaning- Outcome 1",
    "Record Cleaning- Outcome 2",
    "Record Cleaning- Outcome 3",
    "Record Cleaning- Outcome 4",
    "Record Cleaning- Outcome 5",
    "Employment- Outcome 1",
    "Employment- Outcome 2",
    "Employment- Outcome 3",
    "Employment- Outcome 4",
    "Employment- Outcome 5",
    "Housing- Outcome 1",
    "Housing-Outcome 2",
    "Housing- Outcome 3",
    "Housing- Outcome 4",
    "Housing- Outcome 5",
    "Family & Children-Outcome 1",
    "Family & Children-Outcome 2",
    "Family & Children-Outcome 3",
    "Family & Children-Outcome 4",
    "Family & Children-Outcome 5",
    "Court Ordered Debt Outcome 1",
    "Court Ordered Debt Outcome 2",
    "Court Ordered Debt Outcome 3",
    "Court Ordered Debt Outcome 4",
    "Court Ordered Debt Outcome 5",
    "Public Benefit-Outcome 1",
    "Public Benefit-Outcome 2",
    "Public Benefit-Outcome 3",
    "Public Benefit- Outcome 4",
    "Public Benefit- Outcome 5",
    "Education- Outcome 1",
    "Education Outcome 2",
    "Education Outcome 3",
    "Education-Outcome 4",
    "Education-Outcome 5",
    "Immigration-Outcome 1",
    "Immigration- Outcome 2",
    "Immigration- Outcome 3",
    "Immigration- Outcome 4",
    "Immigration- Outcome 5",
    "Criminal Law/Warrants- Outcome 1",
    "Criminal Law/Warrants- Outcome 2",
    "Criminal Law/Warrants- Outcome 3",
    "Criminal Law/Warrants- Outcome 4",
    "Criminal Law/Warrants- Outcome 5",
    "Misc./Other Outcome 1",
    "Misc./Other Outcome 2",
    "Misc./Other Outcome 3",
    "Misc./Other Outcome 4",
    "Misc./Other Outcome 5",
    "SS | Assessment - Outcome 1",
    "SS | Assessment - Outcome 2",
    "SS | Assessment - Outcome 3",
    "SS | Assessment - Outcome 4",
    "SS | Assessment - Outcome 5",
    "SS | 1:1 Individual Counseling 1",
    "SS | 1:1 Individual Counseling 2",
    "SS | 1:1 Individual Counseling 3",
    "SS | 1:1 Individual Counseling 4",
    "SS | 1:1 Individual Counseling 5",
    "SS | Family Counseling 1",
    "SS | Family Counseling 2",
    "SS | Family Counseling 3",
    "SS | Family Counseling 4",
    "SS | Family Counseling 5",
    "SS | Safety Plan 1",
    "SS | Safety Plan 2",
    "SS | Safety Plan 3",
    "SS | Safety Plan 4",
    "SS | Safety Plan 5",
    "SS | Healthcare 1",
    "SS | Healthcare 2",
    "SS | Healthcare 3",
    "SS | Healthcare 4",
    "SS | Healthcare 5",
    "SS | Substance Abuse/ Recovery 1",
    "SS | Substance Abuse/ Recovery 2",
    "SS | Substance Abuse/ Recovery 3",
    "SS | Substance Abuse/ Recovery 4",
    "SS | Substance Abuse/ Recovery 5",
    "SS | Food & Nutrition 1",
    "SS | Food & Nutrition 2",
    "SS | Food & Nutrition 3",
    "SS | Food & Nutrition 4",
    "SS | Food & Nutrition 5",
    "SS | Transportation 1",
    "SS | Transportation 2",
    "SS | Transportation 3",
    "SS | Transportation 4",
    "SS | Transportation 5",
    "SS | Housing Support 1",
    "SS | Housing Support 2",
    "SS | Housing Support 3",
    "SS | Housing Support 4",
    "SS | Housing Support 5",
    "SS | Education 1",
    "SS | Education 2",
    "SS | Education 3",
    "SS | Education 4",
    "SS | Education 5",
    "SS | Job & Career Development 1",
    "SS | Job & Career Development 2",
    "SS | Job & Career Development 3",
    "SS | Job & Career Development 4",
    "SS | Job & Career Development 5",
    "SS | Financial Health 1",
    "SS | Financial Health 2",
    "SS | Financial Health 3",
    "SS | Financial Health 4",
    "SS | Financial Health 5",
    "SS | Leadership/Personal Dev 1",
    "SS | Leadership/Personal Dev 2",
    "SS | Leadership/Personal Dev 3",
    "SS | Leadership/Personal Dev 4",
    "SS | Leadership/Personal Dev 5",
    "SS | Internal Legal Referral 1",
    "SS | Internal Legal Referral 2",
    "SS | Internal Legal Referral 3",
    "SS | Internal Legal Referral 4",
    "SS | Internal Legal Referral 5",
    "SS | Accompaniment/External 1",
    "SS | Accompaniment/External 2",
    "SS | Accompaniment/External 3",
    "SS | Accompaniment/External 4",
    "SS | Accompaniment/External 5",
    "SS | No Outcome/Non-Hire 1",
    "SS | No Outcome/Non-Hire 2",
    "SS | No Outcome/Non-Hire 3",
    "SS | No Outcome/Non-Hire 4", 
    "SS | No Outcome/Non-Hire 5"
]

#Create a new dataframe using only the columns in the list
df = df.reindex(columns=column_names)

#Export the new dataframe as a csv
df.to_csv('# destination path', index=False)