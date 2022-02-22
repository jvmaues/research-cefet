import numpy as np

import networkx as nx
from networkx.utils import cuthill_mckee_ordering
from networkx.utils import reverse_cuthill_mckee_ordering

# CUTCHILL MCKEE
def cuthill(lista):
    G = nx.Graph()
    G.add_edges_from(lista)
    rcm1 = list(cuthill_mckee_ordering(G))
    A = nx.(G, nodelist=rcm1)
    x1, y1 = np.nonzero(A)
    return(y1 - x1).max() + (x1 - y1).max() + 1


# REVERSE CUTCHILL MCKEE
def reverse_cuthill(lista): 
    G = nx.Graph()
    G.add_edges_from(lista)
    rcm2 = list(reverse_cuthill_mckee_ordering(G))
    B = nx.laplacian_matrix(G, nodelist=rcm2)
    x2, y2 = np.nonzero(B)
    return (y2 - x2).max() + (x2 - y2).max() + 1
