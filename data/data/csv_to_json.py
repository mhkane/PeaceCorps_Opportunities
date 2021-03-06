import pandas as pd
import json


df = pd.read_csv('pc.csv',encoding = "ISO-8859-1")
df = df.where((pd.notnull(df)), None)
jobs = []


for row_idx, row in df.iterrows():
    job = {}
    job['current_req_status'] = row['CURRENT REQ STATUS']
    job['FY'] = row['FY']
    job['Q'] = row['Q']
    job['AA'] = row['AA']
    job['location'] = row['POST']
    job['sector'] = row['SECTOR']
    job['REQ ID'] = row['REQ ID']
    job['num_vol'] = row['# VOL REQUESTED']
    job['title'] = row['PROJECT TITLE']
    job['language'] = row['LANG']
    job['nominate_deadline'] = row['LAST DATE TO NOMINATE']
    job['invite_deadline'] = row['INVITATION DEADLINE']
    job['STAGING'] = row['STAGING']
    job['live_cond'] = row['Living Conditions [Living_Cond]']
    job['live_cond_comm'] = row['Living Conditions Comments [Condition_Comments]']
    job['skills'] = row['Desired Skills [Desired_Skills]']
    job['proj_desc'] = row['Project Description [Project_Description]']

    jobs.append(job)



with open('pc.json', 'w') as f:
    json.dump(jobs, f)
