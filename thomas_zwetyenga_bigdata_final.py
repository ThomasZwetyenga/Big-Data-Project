
# coding: utf-8

# In[98]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import urllib.request, urllib.parse, urllib.error


# In[1]:


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



# In[99]:


df =pd.read_csv("consommation-electrique-par-secteur-dactivite-commune_2016.csv", sep=";", encoding = 'utf8', low_memory=False)
df2 =pd.read_csv("consommation-electrique-par-secteur-dactivite-commune_all.csv", sep=";", encoding = 'utf8', low_memory=False)


# In[100]:


df.dtypes


# In[103]:


df[df['Nb sites Industrie']<df['Nb sites Industrie'].mean()]


# In[104]:


distinct_commune = df['Nom commune'].unique()
NB_distinct_commune = len(distinct_commune)
NB_distinct_commune


# In[105]:


distinct_département = df['Nom département'].unique()
NB_distinct_département = len(distinct_département)
NB_distinct_département


# In[106]:


distinct_region = df['Nom région'].unique()
NB_distinct_region = len(distinct_region)
NB_distinct_region


# In[107]:


df_resi = df[['Nb sites Résidentiel','Nom région','Conso totale Résidentiel (MWh)','Conso moyenne Résidentiel (MWh)']]


# In[108]:


df_resi_sum = df_resi.groupby(['Nom région']).sum()


# In[109]:


df_resi_sum


# In[110]:


df_resi_sum.plot.bar()


# In[111]:


df_conso = df[['Conso totale Industrie (MWh)','Nom région','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]


# In[112]:


df_conso_sum = df_conso.groupby(['Nom région']).sum()


# In[113]:


df_conso_sum


# In[114]:


df_conso_sum.plot.bar()


# In[115]:


input_region = input("Entrez une région ")
print(input_region)

df_info_region = df[['Conso totale Industrie (MWh)','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]
df_info_region[df['Nom région']==input_region].sum().plot.pie()


# In[116]:


df_resi2 = df2[['Année','Nb sites Résidentiel','Conso totale Résidentiel (MWh)','Conso moyenne Résidentiel (MWh)']]
df_resi2[df2['Nom région']==input_region].groupby(['Année']).sum()


# In[117]:


df_indu2 = df2[['Année','Nb sites Industrie','Conso totale Industrie (MWh)']]
df_indu2[df2['Nom région']==input_region].groupby(['Année']).sum()


# In[118]:


df_resi2[df2['Nom région']==input_region].groupby(['Année']).sum().plot.bar()


# In[119]:


df_indu2[df2['Nom région']==input_region].groupby(['Année']).sum().plot.bar()


# In[120]:


df_departement = df[['Nom région','Nom département','Conso totale Industrie (MWh)','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]
df_departement[df_departement['Nom région']== input_region].groupby(['Nom département']).sum()


# In[121]:


df_departement[df_departement['Nom région']== input_region].groupby(['Nom département']).sum().plot.bar()


# In[122]:


input_departement = input("Entrez un departement ")
print(input_departement)

df_ville = df[['Code commune','Nom département','Nom commune','Conso totale Industrie (MWh)','Conso totale Résidentiel (MWh)','Conso totale Professionnel (MWh)','Conso totale Tertiaire (MWh)']]
df_ville_sum = df_ville[df_ville['Nom département']== input_departement].groupby(['Nom commune', 'Nom département', 'Code commune']).sum()
df_ville_sum


# In[123]:


df_ville_sum[df_ville_sum['Conso totale Industrie (MWh)']<df['Conso totale Industrie (MWh)'].mean()]


# In[140]:


city_code = input("Entrez ")
print(city_code)


# In[141]:


import feedparser

def RSS_parse(link_rss):
    return feedparser.parse(link_rss) 
    
def get_headlines(link_rss):
    headlines = []
    rss_feed = RSS_parse(link_rss)
    for newsitem in rss_feed['items']:
        headlines.append(newsitem['title'])
    return headlines

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

allheadlines = []
 
newsurls = { 'rssImmo':'https://www.paruvendu.fr/pa/rss/default/rssImmo'}
 
for key,url in newsurls.items():
    allheadlines.extend( get_headlines( url ) )

for x in range(len(allheadlines)):
    if(str(city_code) in allheadlines[x]):
        print(allheadlines[x])
else :
    print('no house for this in the flux righ now')


# In[134]:


print("Fin présentation")


# In[139]:


allheadlines


# In[97]:


print('Grand-Est, Marne, Reims, 51100')

