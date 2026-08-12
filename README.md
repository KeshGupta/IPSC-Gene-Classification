# IPSC-Gene-Classification

# Context
  In 2018 Biddy et al used CellTagging to see whether Fibroblast cells that could successfully reprogram (iEP) expressed certain genes in it's early stages that unsuccessful (dead-end) cells did not. The results of his study concluded that successfully reprogramed cells did express different genes in the fibroblast stage that could predict whether a cell would become reprogramed or not, such as Apoa1, Cdh1, and Mettl7a1. 
  I expanded on Biddy's study and built a classifier that could predict iEP vs dead-end results from early gene expression. My goal was to recreate Biddy's pipeline without CellTagging and use Cellrank for early Fibroblast labels. I then trained a classifier to predict fate from early gene expression without Biddy's marker genes (Apoa1, Cdh1, Col1a2, etc). 
  The results point strongly to the fact that fate is predictable from early gene expression. The classifier was able to predict fate successfully from Fibroblast gene expression with an AUC of 0.96 at the earliest timepoints. Additionally, the marker genes found by the classifier accurately matches the genes found by Biddy, essentially recreating the whole trajectory with similar results.

# 
