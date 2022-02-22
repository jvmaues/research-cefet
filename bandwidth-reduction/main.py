import datetime
from os import error
import csv
import datetime
from numpy import arange
import math
import read_filenames as rf
import read_Instances

#Algoritmos testados

mypath = "/home/joao/Documents/CEFET/IC/Bandwidth-reduction/Codes/oficial/data"

list_path = rf.readFilesInDict(mypath, '.mtx')

A = [[1,4], [0,2,4], [1,3], [2,4,5], [0,1,3], [3]]
f1 = [2, 3, 4, 1, 5, 6]

B = [[1], [0, 2, 3], [1], [1, 4], [3]]
f2 = [3, 1, 2, 5, 4]

def dif(p, q):
    return abs(p-q)
        
def measureBand(A, f):
    width = 0
    for v in range(len(A)):
        for adj in A[v]:
            temp = dif(f[v], f[adj])
            if temp > width:
                width = temp
            
    return width


with open('resultados.csv', mode='a+') as csv_file:

        fieldnames = ['instance','timestamp', 'constructive', 'constructive random',  'cuchill mckee', 'reverse cuchill mckee' ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for instance_path in list_path:

                instance_name = instance_path.replace(mypath, "").replace("/", "").replace(".mtx", "")

                nnodes, nedges, edges, neighbours, lista_adj = ri.load_instance(instance_path)

                try:
                        w1 = initialS(lista_adj)
                except:
                        w1 = "error"
                try:
                        w2 = initialSrandom(lista_adj)
                except:
                        w2 = "error"
                try:
                        w3 = cth.cutchill(edges)
                except:         
                        w3 = "erro"
                try:
                        w4 = cth.reverse_cutchill(edges)
                except: 
                        w4 = "erro"
                
                writer.writerow({'instance': instance_name,
                                 'timestamp': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                 'constructive': w1,
                                 'constructive random': w2,
                                 'cuchill mckee': w3,
                                 'reverse cuchill mckee': w4})