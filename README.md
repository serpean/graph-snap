# Snap.py

Working with graphs https://snap.stanford.edu/

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Exc. 1
Look at the (undirected) graphs 0.edges and 414.edges (from a dataset containing various 
friends lists from Facebook). \
a.  What are the sizes of the connected components of these graphs?\
b. Do the sizes of connected components reflect what you would expect to find? Explain.
## Exc. 2:
Look at the graph links.tsv (containing links between Wikipedia pages) both as a directed and 
undirected graph.\
a. In both cases, what is the diameter of this graph? Which are the 300 nodes with highest 
degrees (and what are their degrees)?\
b. In both cases, delete these nodes from the graph. What is the diameter now?\
c. Is the diameter the same in both the directed and the undirected graph? If not, is one always
smaller than the other? Why should that (not) be? Explain.\
d. Does the directed or undirected case best reflect the underlying data, i.e. links between 
Wikipedia pages? Explain