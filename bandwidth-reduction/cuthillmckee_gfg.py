# C++ program for Implementation of
# Reverse Cuthill Mckee Algorithm
from collections import deque as Queue

import read_Instances as ri
globalDegree = []


def findIndex(a, x):
	for i in range(len(a)):
		if a[i][0] == x:
			return i
	return -1


class ReorderingSSM:
	__matrix = []
	# Constructor and Destructor
	def __init__(self, m):
		self.__matrix = m

	# class methods

	# Function to generate degree of all the nodes
	def degreeGenerator(self):

		degrees = []

		for i in range(len(self.__matrix)):
			count = 0
			for j in range(len(self.__matrix[0])):
				count += self.__matrix[i][j]

			degrees.append(count)

		return degrees

	# Implementation of Cuthill-Mckee algorithm
	def CuthillMckee(self):
		global globalDegree
		degrees = self.degreeGenerator()

		globalDegree = degrees

		Q = Queue()
		R = []
		notVisited = []

		for i in range(len(degrees)):
			notVisited.append((i, degrees[i]))

		# Vector notVisited helps in running BFS
		# even when there are dijoind graphs
		while len(notVisited):

			minNodeIndex = 0

			for i in range(len(notVisited)):
				if notVisited[i][1] < notVisited[minNodeIndex][1]:
					minNodeIndex = i

			Q.append(notVisited[minNodeIndex][0])

			notVisited.pop(findIndex(notVisited, notVisited[Q[0]][0]))

			# Simple BFS
			while Q:

				toSort = []

				for i in range(len(self.__matrix[0])):
					if (
						i != Q[0]
						and self.__matrix[Q[0]][i] == 1
						and findIndex(notVisited, i) != -1
					):
						toSort.append(i)
						notVisited.pop(findIndex(notVisited, i))

				toSort.sort(key=lambda x: globalDegree[x])

				for i in range(len(toSort)):
					Q.append(toSort[i])

				R.append(Q[0])
				Q.popleft()

		return R

	# Implementation of reverse Cuthill-Mckee algorithm
	def ReverseCuthillMckee(self):

		cuthill = self.CuthillMckee()

		n = len(cuthill)

		if n % 2 == 0:
			n -= 1

		n = n // 2

		for i in range(n + 1):
			j = cuthill[len(cuthill) - 1 - i]
			cuthill[len(cuthill) - 1 - i] = cuthill[i]
			cuthill[i] = j

		return cuthill


# Driver Code
# if __name__ == "__main__":
num_rows = 10

# matrix = [[0.0] * num_rows for _ in range(num_rows)]

# This is the test graph,
# check out the above graph photo

# matrix[0] = [0, 1, 0, 0, 0, 0, 1, 0, 1, 0]
# matrix[1] = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
# matrix[2] = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
# matrix[3] = [0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
# matrix[4] = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1]
# matrix[5] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# matrix[6] = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# matrix[7] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
# matrix[8] = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
# matrix[9] = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]

nome_arquivo = "/home/joaovitor/Documents/TCC/research-cefet/bandwidth-reduction/data/494_bus.mtx"
nnodes, nedges, edges, neighbours, lista_adj, matrix = ri.load_instance(nome_arquivo)



m = ReorderingSSM(matrix)

r = m.ReverseCuthillMckee()

print("Permutation order of objects:", r)

