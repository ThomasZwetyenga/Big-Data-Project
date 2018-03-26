
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import urllib.request, urllib.parse, urllib.error


url = "https://data.enedis.fr/explore/dataset/consommation-electrique-par-secteur-dactivite-commune/download/?format=csv&refine.annee=2016&timezone=Europe/Berlin&use_labels_for_header=true"
file_name ="consommation-electrique-par-secteur-dactivite-commune_2016.csv"

print("downloading with urllib, first file")
urllib.request.urlretrieve(url, file_name)

local_filename, headers = urllib.request.urlretrieve(url)
html = open(local_filename)
print("Done !\n")

url2 = "https://data.enedis.fr/explore/dataset/consommation-electrique-par-secteur-dactivite-commune/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true"
file_name2 ="consommation-electrique-par-secteur-dactivite-commune_all.csv"

print("downloading with urllib second file")
urllib.request.urlretrieve(url2, file_name2)

local_filename2, headers2 = urllib.request.urlretrieve(url2)
html = open(local_filename2)
print("Done !\n")



# In[2]:


df =pd.read_csv("consommation-electrique-par-secteur-dactivite-commune_2016.csv", sep=";", encoding = 'utf8', low_memory=False)
df2 =pd.read_csv("consommation-electrique-par-secteur-dactivite-commune_all.csv", sep=";", encoding = 'utf8', low_memory=False)


# In[3]:


df.dtypes


# In[4]:


df[df['Nb sites Industrie']>df['Nb sites Industrie'].mean()]


# In[5]:


distinct_commune = df['Nom commune'].unique()
NB_distinct_commune = len(distinct_commune)
NB_distinct_commune


# In[6]:


distinct_département = df['Nom département'].unique()
NB_distinct_département = len(distinct_département)
NB_distinct_département


# In[7]:


distinct_region = df['Nom région'].unique()
NB_distinct_region = len(distinct_region)
NB_distinct_region


# In[8]:


df_resi = df[['Nb sites Résidentiel','Nom région','Conso totale Résidentiel (MWh)','Conso moyenne Résidentiel (MWh)']]


# In[9]:


df_resi_sum = df_resi.groupby(['Nom région']).sum()


# In[10]:


df_resi_sum


# In[11]:


df_resi_sum.plot.bar()


# In[12]:


df_conso = df[['Conso totale Industrie (MWh)','Nom région','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]


# In[13]:


df_conso_sum = df_conso.groupby(['Nom région']).sum()


# In[14]:


df_conso_sum


# In[15]:


df_conso_sum.plot.bar()


# In[16]:


df_info_region = df[['Conso totale Industrie (MWh)','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]
df_info_region[df['Nom région']=='Provence-Alpes-Côte d\'Azur'].sum().plot.pie()


# In[17]:


df_resi2 = df2[['Année','Nb sites Résidentiel','Conso totale Résidentiel (MWh)','Conso moyenne Résidentiel (MWh)']]
df_resi2[df2['Nom région']=='Provence-Alpes-Côte d\'Azur'].groupby(['Année']).sum()


# In[18]:


df_indu2 = df2[['Année','Nb sites Industrie','Conso totale Industrie (MWh)']]
df_indu2[df2['Nom région']=='Provence-Alpes-Côte d\'Azur'].groupby(['Année']).sum()


# In[19]:


df_resi2[df2['Nom région']=='Provence-Alpes-Côte d\'Azur'].groupby(['Année']).sum().plot.bar()


# In[20]:


df_indu2[df2['Nom région']=='Provence-Alpes-Côte d\'Azur'].groupby(['Année']).sum().plot.bar()


# In[21]:


df_departement = df[['Nom région','Nom département','Conso totale Industrie (MWh)','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]
df_departement[df_departement['Nom région']== 'Provence-Alpes-Côte d\'Azur'].groupby(['Nom département']).sum()


# In[22]:


df_departement[df_departement['Nom région']== 'Provence-Alpes-Côte d\'Azur'].groupby(['Nom département']).sum().plot.bar()


# In[23]:


df_ville = df[['Nom département','Nom commune','Conso totale Industrie (MWh)','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]
df_ville_sum = df_ville[df_ville['Nom département']== 'Vaucluse'].groupby(['Nom commune', 'Nom département']).sum()
df_ville_sum


# In[24]:


df_ville_sum[df_ville_sum['Conso totale Industrie (MWh)']<df['Conso totale Industrie (MWh)'].mean()]

