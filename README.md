# IPSC-Gene-Classification

# Context
  In 2018 Biddy et al used CellTagging to see whether Fibroblast cells that could successfully reprogram (iEP) expressed certain genes in it's early stages that unsuccessful (dead-end) cells did not. The results of his study concluded that successfully reprogramed cells did express different genes in the fibroblast stage that could predict whether a cell would become reprogramed or not, such as Apoa1, Cdh1, and Mettl7a1. 
  I expanded on Biddy's study and built a classifier that could predict iEP vs dead-end results from early gene expression. My goal was to recreate Biddy's pipeline without CellTagging and use Cellrank for early Fibroblast labels. I then trained a classifier to predict fate from early gene expression without Biddy's marker genes (Apoa1, Cdh1, Col1a2, etc). 


  # Results 
  The results point strongly to the fact that fate is predictable from early gene expression. The classifier was able to predict fate successfully from Fibroblast gene expression with an AUC of 0.88 - 0.96 at the earliest timepoints. 
  
  <img width="395" height="305" alt="AUC_graph_actual" src="https://github.com/user-attachments/assets/b0f12583-f6ea-46ce-a44a-44c0de7e44ca" />
  
  "graph of AUC vs Timepoint separated into bins of similar population"

  Additionally, even though I excluded the marker genes Biddy's paper found, the top dead-end predictor genes matched Fibroblast identity, a core finding in Biddy's paper. Across runs, dead-end predictors consistently include fibroblast/ECM genes (Pdgfra, Fgf7, Sdc4, Adamts1, Col5a2, Angptl2), essentially reconstructing the bifurcating trajectory and independently confirming the two-fate structure. 
  
<img width="135" height="168" alt="Screenshot 2026-08-11 at 9 55 25 PM" src="https://github.com/user-attachments/assets/43e2236a-8343-4b16-8fbb-51efcafdeea8" />

  "screenshot of top Dead-end predictors from one classifier run. Fibroblast genes Col5a2 and Pdgfra are present"

  <img width="568" height="404" alt="cell_type_paga" src="https://github.com/user-attachments/assets/89d88ae9-b837-4b6f-9955-f7b15e277722" />
  
  "image of textbook Y shape demonstrating two-fate structure. Other relationships are much smaller and characterized by comparatively weaker lines on PAGA graph"


# How to Run
1. Download the mtx.gz files from https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99915
2. Download libraries: pip install scanpy numpy scipy leidenalg igraph harmonypy cellrank 
3. Run pipeline, Note: I needed to use Colab on my macbook to run this as I didn't have enough RAM normally


# Limitations
  In the original paper Biddy used CellTagging to track cells across lineages. This way they could be certain if a Fibroblast cell became reprogrammed or not. Since this project centered around Single Cell RNA Analysis, I chose the ditch this computationally heavy step and use Cellrank. However using Cellrank comes with limitations, such as fate labels the classifier trains on may not be entirely accurate. Since Cellrank labels come from transcriptionally similar cells in graphical space biased towards increasing pseudotime, the classifier may have learned to simple predict this relationship instead of actual iEP vs deadend gene expression. This could be one reason the AUC is very high even at the earliest timepoint.

# Project Improvements
  Actually use CellTagging like Biddy did in his paper to accurately track fate labels across lineages. This would reduce noise and is a much better alternative to Cellrank. 
