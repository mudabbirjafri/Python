#import Libraries
import numpy as np
import pandas as pd
import os
os.chdir('C:/Users/jafris/Documents/Python Scripts/Marketing Analysis')
#Run a lead report in salesforce and download with UTF-8 Encoding
leads= pd.read_csv('All_Leads.csv')
leads=leads.rename(columns={"Company / Account": "Account Name"}) #update the column name
# leads.head()
#Run a contacts report in salesforce and download with UTF-8 Encoding
contacts = pd.read_csv('All_Contacts.csv')
# contacts.head()
#Merge the leads and contacts into a single dataframe
df1 = pd.concat([leads, contacts], axis=0, join='outer', sort= 'True').sort_index()
# df1.head()
#sort values by Email
df1.sort_values("Email", inplace = True)
#drop duplicate emails (contact or leads) keeong the first match
df1.drop_duplicates(subset ="Email",
                     keep = 'first', inplace = True)

#Load the list of new leads from a trade show
new_leads = pd.read_csv('New_Leads.csv', encoding ='utf-8')
# new_leads.head()
#join the new leads from tradeshow to the salesforce data
result = new_leads.merge(df1.drop_duplicates(), on=['Email'],
                   how='left', indicator=True)

#write out the net new leads into an excel file with the new column "-merge", filter values by Left only to find net new leads that never existed in salesforce
result.to_excel("Net_NewLeads_result.xlsx", sheet_name='New Leads', encoding='utf-8')





#join the new leads from tradeshow to the salesforce data
# net_new_join = pd.concat([df1, new_leads], axis=0, join='outer', sort= 'True').sort_index()

# net_new_leads = net_new_join[net_new_join.duplicated(['Email'],keep='first')]
# net_new_leads.head()
