import math
import sys
from collections import defaultdict

def load_instance(filename):
    edges = []
    neighbours = defaultdict(list)
    neigh = defaultdict(list)
    flag = True
    f = open(filename, 'r')
    for line in f:

        if flag == True:
            nnodes, nedges = [int(x) for x in line.split()]
            flag = False
        else:
            e1, e2 = [int(x) for x in line.split()]

            neigh[e1].append(e2)
            if e1 != e2:
                edges.append((min(e1, e2), max(e1, e2)))
                neighbours[e1].append(e2)
                neighbours[e2].append(e1)
            else:
                nedges = nedges - 1
    f.close()

    f = []
    

    for v in neighbours:
        f.append(v)

    nodes = []

    for v in neighbours:
        nodes.append(v)

    lista_adj = []

    for n in nodes:
        lista_adj.append(neighbours[n])

    
    matrix = []

    for key in neighbours:
        line = [0]*nnodes
        for element in neighbours[key]:
            line[element-1] = 1
        matrix.append(line)
    
    return nnodes, nedges, edges, neighbours, lista_adj, matrix


def print_instance(qtd_nodes, qtd_edges, edges, neighbours):
    print(str(qtd_nodes)+" "+str(qtd_edges))

    for e in edges:
        print(str(e[0])+" "+str(e[1]))

    for i in neighbours:
        print(neighbours[i])

    print(neighbours)


# if __name__ == "__main__":

nome_arquivo = "/home/joaovitor/Documents/TCC/research-cefet/bandwidth-reduction/data/494_bus.mtx"
#qtd_nodes, qtd_edges, edges, neighbours, lista_adj = load_instance(nome_arquivo)

# print_instance(qtd_nodes, qtd_edges, edges, neighbours)

nnodes, nedges, edges, neighbours, lista_adj, matrix = load_instance(nome_arquivo)
f = [None]*len(neighbours)

for line in range(len(matrix)):
    print(matrix[line])

# print("nnodes: ",nnodes)
# print("nedges: ",nedges)
# print("edges: ",edges) 
# print("neighbours: ",neighbours)
# print("lista_adj: ",lista_adj)
