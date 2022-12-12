#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Reading Data
import pandas as pd 
df=pd.read_csv('data.csv')
df.head()


# In[ ]:


#### Calculating total impressions for the age group 30-34
total_impressions=df.loc[df['age']=='30-34', 'impressions'].sum()
total_impressions


# In[ ]:


#### All ad_ids for every campaign_id (a campaign contains multiple ads)
df.campaign_id.unique()


# In[ ]:


for campaign_id, row in df.iterrows():
    print(row['campaign_id'], row['ad_id'])


# In[ ]:


df1=df.set_index(['campaign_id', 'ad_id'], drop=True)
df1


# In[ ]:


#### Total clicks where report_start between dates 19/08/2017 to 22/08/2017 (both inclusive)
total_clicks=df.loc[(df['reporting_start']=='19/08/2017') | (df['reporting_start']=='20/08/2017') | (df['reporting_start']=='21/08/2017') | (df['reporting_start']=='22/08/2017'), 'clicks'].sum()
total_clicks

