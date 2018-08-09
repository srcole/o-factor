
import numpy as np
import pandas as pd
from collections import defaultdict

import requests
from bs4 import BeautifulSoup
import re
import os
import time
import csv

import matplotlib.pyplot as plt

import os
if not os.path.exists('data/'):
    os.makedirs('data/')

df = pd.read_csv('PMC-ids.csv')
df_keep = df[df['Journal Title']=='PLoS Comput Biol']
df_keep = df_keep[df_keep['Year']>=2014]
df_keep.reset_index(inplace=True, drop=True)

apikey = open('apikey.txt', 'r').read()

db = 'pmc'
base = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'

# Load keywords# Load
with open('keywords.csv', 'r') as f:
    reader = csv.reader(f)
    terms = list(reader)[0]

# Number of characters to extract around keywords# Numbe
span_buffer = 100

# Saving parameters
N_previous = 0
N_chunk = 10000
N_save = 100

# Load previous computation
if N_previous > 0:
    dfs_articles = {}
    for k in terms + other:
        csv_name = 'data/{:s}_{:d}.csv'.format(k, N_previous)
        dfs_articles[k] = [pd.read_csv(csv_name, index_col=0)]
else:
    dfs_articles = defaultdict(list)

for i, row in df_keep.loc[N_previous + 1:].iterrows():
    # Get full text of 1 paper
    pmcid = row['PMCID']
    s = '{:s}db={:s}&id={:s}'.format(base, db, pmcid, apikey)
    out = requests.get(s)
    bs = BeautifulSoup(out.content, 'lxml')

    # DFs of terms
    for term in terms:
        dict_term = defaultdict(list)
        for s in re.finditer(term, out.text, re.IGNORECASE):
            save_span = s.span()
            sent = out.text[(save_span[0] - span_buffer):(save_span[1] + span_buffer)]

            dict_term['PMCID'].append(pmcid)
            dict_term['sentence'].append(sent)
        dfs_articles[term].append(pd.DataFrame(dict_term))

    # Save output every N
    if (i % N_save == 0) & (i > 0):
        print(i)
        for k in dfs_articles.keys():
            df_save = pd.concat(dfs_articles[k])
            df_save.to_csv('data/{:s}_{:d}.csv'.format(k, i))

            # Delete last file Unless
            if (i - N_save) % N_chunk > 0:
                os.remove('data/{:s}_{:d}.csv'.format(k, i - N_save))

        if i % N_chunk == 0:
            if i > 0:
                dfs_articles = defaultdict(list)

# Save output when finish
for k in dfs_articles.keys():
    df_save = pd.concat(dfs_articles[k])
    df_save.to_csv('data/{:s}_{:d}.csv'.format(k, i))
    os.remove('data/{:s}_{:d}.csv'.format(k, int(np.round(i - (N_save / 2 - 1), -2))))


