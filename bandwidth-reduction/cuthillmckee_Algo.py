from collections import defaultdict
import random

'''
Instancie uma fila vazia Q e uma matriz vazia para a ordem de permutação dos objetos R.
S1: Primeiro encontramos o objeto com um grau mínimo cujo índice ainda não foi adicionado a R. 
    Digamos, o objeto correspondente à p-ésima linha foi identificado como o objeto com um grau mínimo. Adicione p a R.
S2: À medida que um índice é adicionado a R, adicione todos os vizinhos do objeto correspondente ao índice selecionado 
    em ordem crescente de grau, em Q. Os vizinhos são nós com valor diferente de zero entre os elementos não diagonais na p-ésima linha.
S3: Extraia o primeiro nó em Q, digamos C. Se C não foi inserido em R, adicione-o a R, adicione a Q os vizinhos de C em ordem crescente de grau.
S4: Se Q não estiver vazio, repita S3.
S5: Se Q estiver vazio, mas houver objetos na matriz que não foram incluídos em R, 
    comece a partir de S1, mais uma vez. (Isso pode acontecer se houver gráficos separados)
S6: Encerre este algoritmo assim que todos os objetos forem incluídos em R.
S7: Finalmente, inverta os índices em R, ou seja, (troca (R [i], R[P-i + 1])). 
'''
    

def compareDegree(element):
    return element[1]

def degreesGenerator(matrix_dict):
    keys = []
    degrees = []
    for key in matrix_dict:
        keys.append(key)
        degrees.append(len(matrix_dict[key]))

    degrees_dict = dict(zip(keys, degrees))
    return degrees_dict

## Implementation of Cuthill-Mckee algorithm

def CuthillMckee(m):
    
    globalDegree = degreesGenerator(m)

    notVisited = globalDegree.copy()

    queue = []
    Rlist = []

    while len(notVisited):
        
        minNode = list(notVisited.keys())[0]

        for key in notVisited:
            if notVisited[key] < notVisited[minNode]:
                minNode = key
               
        queue.append(minNode)

        del notVisited[minNode]

        ## Simple BFS

        while len(queue)!=0:
            
            toSort = []

            for node in m[minNode]:
                
                if (node not in queue and node in notVisited):
                    
                    toSort.append((node, globalDegree[node]))
                    
                    del notVisited[node]
            
            toSort.sort(key=compareDegree)

            for element in toSort:
                queue.append(element[0])
            
            Rlist.append(queue[0])
            queue.pop(0)

    label = labels(Rlist)
    w = measureBand(m, label)
          
    return Rlist, label, w

def ReverseCuthillMckee(m):
    Rlist, l, w = CuthillMckee(m)
    Rlist.reverse()
    Rreverse = Rlist
    labelReverse = labels(Rreverse)
    wReverse = measureBand(m, labelReverse)
    return Rreverse, labelReverse, wReverse

def CuthillMckeeRandom(m):
    
    globalDegree = degreesGenerator(m)

    notVisited = globalDegree.copy()

    queue = []
    Rlist = []
    
    while len(notVisited):
        
        minNode = random.choices(list(notVisited.keys()))[0]   
        queue.append(minNode)
        del notVisited[minNode]

        ## Simple BFS

        while len(queue)!=0:
            
            toSort = []

            for node in m[minNode]:
                
                if (node not in queue and node in notVisited):
                    
                    toSort.append((node, globalDegree[node]))
                    
                    del notVisited[node]
            
            toSort.sort(key=compareDegree)

            for element in toSort:
                queue.append(element[0])
            
            Rlist.append(queue[0])
            queue.pop(0)
    
    label = labels(Rlist)
    w = measureBand(m, label)
            
    return Rlist, label, w

def ReverseCuthillMckeeRandom(m):
    Rrandom, l, w = CuthillMckeeRandom(m)
    Rrandom.reverse()
    RreverseRandom = Rrandom
    labelReverseRandom = labels(RreverseRandom)
    wReverseRandom = measureBand(m, labelReverseRandom)
    return Rrandom, labelReverseRandom, wReverseRandom

def CuthillMckeeMaxDegree(m):
    
    globalDegree = degreesGenerator(m)

    notVisited = globalDegree.copy()

    queue = []
    Rlist = []

    while len(notVisited):
        
        maxNode = list(notVisited.keys())[0]

        for key in notVisited:
            if notVisited[key] > notVisited[maxNode]:
                maxNode = key
               
        queue.append(maxNode)

        del notVisited[maxNode]

        ## Simple BFS

        while len(queue)!=0:
            
            toSort = []

            for node in m[maxNode]:
                
                if (node not in queue and node in notVisited):
                    
                    toSort.append((node, globalDegree[node]))
                    
                    del notVisited[node]
            
            toSort.sort(key=compareDegree)

            for element in toSort:
                queue.append(element[0])
            
            Rlist.append(queue[0])
            queue.pop(0)

    label = labels(Rlist)
    w = measureBand(m, label)
          
    return Rlist, label, w

def ReverseCuthillMckeeMaxDegree(m):
    Rlist, l, w = CuthillMckeeMaxDegree(m)
    Rlist.reverse()
    RreverseMax = Rlist
    labelReverseMax = labels(RreverseMax)
    wReverse = measureBand(m, labelReverseMax)
    return RreverseMax, labelReverseMax, wReverse




###### measure width band ########

def labels(R):
    f = defaultdict(int)
    label = 1
    for node in R:
        f[node] = label
        label=label+1
    return f

def measureBand(adj_dict, F):
    width = 0
    for key in adj_dict:
        for node in adj_dict[key]:
            temp = abs(F[key] - F[node])
            if temp > width:
                width = temp
            
    return width


########### MAIN // Drive code #########

# teste_dicionario = { 0:[1,4], 1:[0,2,4], 2:[1,3, 7], 3:[2,4,5], 4:[0,1,3,6], 5:[3], 6:[4,7], 7:[2,6] }

# Rlist_teste = CuthillMckeeInit(teste_dicionario, 0)

# f_teste = labels(Rlist_teste)

# width_teste = measureBand(teste_dicionario, f_teste)

# # print(f_teste)

# # qtd_nodes, qtd_edges, edges, neighbours, lista_adj = readInstances.load_instance("/home/joao/Documents/CEFET/IC/Bandwidth-reduction/Codes/oficial/data/662_bus.mtx")

# # Rlist, label, width = ReverseCuthillMckee(neighbours)


# print("Permutation order of objects: ", Rlist_teste)
# print("Width Band: ", width_teste)