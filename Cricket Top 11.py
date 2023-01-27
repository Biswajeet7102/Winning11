#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json


# **Match Summary**

# In[89]:


with open(r"C:\Users\KIIT\Downloads\5_CricketT20Analytics\data_collection\t20_json_files\t20_wc_match_results.json") as f:
    data=json.load(f)
data


# In[90]:


df_summary=pd.DataFrame(data[0]['matchSummary'])
df_summary


# **Bowling performance**

# In[91]:


with open(r"C:\Users\KIIT\Downloads\5_CricketT20Analytics\data_collection\t20_json_files\t20_wc_bowling_summary.json") as f:
    data=json.load(f)
data


# In[92]:


all_records=[]
for item in data:
    all_records.extend(item['bowlingSummary'])
all_records
df_bowling=pd.DataFrame(all_records)
df_bowling


# **Batting Summary**

# In[93]:


with open(r"C:\Users\KIIT\Downloads\5_CricketT20Analytics\data_collection\t20_json_files\t20_wc_batting_summary.json") as f:
    data=json.load(f)
data


# In[94]:


all_records=[]
for item in data:
    all_records.extend(item['battingSummary'])
df_batting=pd.DataFrame(all_records)
df_batting


# In[95]:


df_batting["out/not_out"]=df_batting.dismissal.apply(lambda x :"out" if len(x)>0 else "not_out" )
df_batting


# In[96]:


df_batting.drop(columns=["dismissal"],inplace=True)
df_batting


# **Player performance**

# In[97]:


with open(r"C:\Users\KIIT\Downloads\5_CricketT20Analytics\data_collection\t20_json_files\t20_wc_player_info.json") as f:
    data=json.load(f)
data


# In[98]:


df_player_performance=pd.DataFrame(data)
df_player_performance


# In[102]:


match_id_dict={}

for id,row in df_summary.iterrows():
    key1=row['team1'] + ' Vs '+ row['team2']
    key2=row['team2'] + ' Vs '+ row['team1']
    
    match_id_dict[key1]=row["scorecard"]
    match_id_dict[key2]=row["scorecard"]
match_id_dict
    


# In[103]:


df_batting["scoreboard"]=df_batting["match"].map(match_id_dict)


# In[104]:


df_batting


# In[105]:


df_summary

