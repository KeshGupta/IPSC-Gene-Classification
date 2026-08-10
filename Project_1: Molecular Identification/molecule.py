   # save as h5ad file for later use


import scanpy as sc
import pandas as pd
import numpy as np

data = sc.read_mtx('data/matrix.mtx.gz').T   # .T -> cells x genes

barcodes = pd.read_csv("data/barcodes.tsv.gz", sep='\t', header=None)
features = pd.read_csv("data/features.tsv.gz", sep='\t', header=None)

data.obs_names = barcodes[0].values
data.var_names = features[1].values   # column 1 = gene symbols (switch to [0] if head() shows symbols there)
data.var['gene_ids'] = features[0].values   # keep IDs too, handy later
data.var_names_make_unique()

print("cells x genes:", data.shape)

print(data.obs.head())

sc.pp.filter_genes(data, min_cells = 3)

# flag mitochondrial genes. This dataset is MOUSE, so the prefix is lowercase 'mt-'
data.var['mt'] = data.var_names.str.startswith('mt-')

# now calculate_qc_metrics can compute pct_counts_mt per cell
sc.pp.calculate_qc_metrics(data, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)


data = data[data.obs['n_genes_by_counts'] > 200]
data = data[data.obs['n_genes_by_counts'] < 6000]
data = data[data.obs['total_counts'] < 50000]
data = data[data.obs['pct_counts_mt'] < 10]  


data.obs['suffix'] = pd.Series(data.obs_names, index=data.obs_names).str.extract(r'(-\d+)$', expand=False).values

suffix_order = ['-2','-1','-3','-4','-5','-6','-7','-8']
data.obs['timepoint'] = pd.Categorical(data.obs['suffix'], categories=suffix_order, ordered=True)

print(data.obs['timepoint'].value_counts().sort_index())

data.write("data/data_qc_filtered.h5ad")

print("done")

