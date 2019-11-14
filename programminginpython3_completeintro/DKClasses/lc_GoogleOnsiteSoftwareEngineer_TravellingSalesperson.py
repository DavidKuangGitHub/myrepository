#lc_GoogleOnsiteSoftwareEngineer_TravellingSalesperson.py
#An interviewee was asked to implement the Travelling Salesperson Problem using Best-First Search with Brand-and-Bound Pruning ALgorithm
#Problem: Determine an optimal tour in a weighted, directed graph. The weight are non-negative numbers
#Inputs: a weighted, directed graph, and n, the number of vertices in the graph. The graph is represented by a two-dimensional array W, which has both its row and columns indexed from 1 to n, where W[i][j] is the weight on the edge from the ith vertex to the jth vertex.
#Outputs: variable minlength, whose value is the length of an optimal tour, and variable opttour, whose value is an optimal tour. 

#Here was the pseudocode she/he came up with for the main routine. In addition to this pseudocode, she/he was tasked with writing the two supporting subroutines: length() and bound(). 
#She/he ran out of time before getting to these subroutines.
#However, she/he was pretty much confident function length() is supposed to return the length of the tour u.path, and the function bound() returns the bound for a node using the considerations above.

#David: TSP(Travelling SalesPerson Problem) Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns the origin city. 
# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
V = 5 
"""V = 4"""
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    while True: 
        # store current Path weight(cost) 
        current_pathweight = 0
        # compute current path weight 
        k = s 
        for i in range(len(vertex)): 
            current_pathweight += graph[k][vertex[i]] 
            k = vertex[i] 
        current_pathweight += graph[k][s] 
        print("k= ", k, "   i= ", i)
        # update minimum 
        """print("Before min_path = ", min_path)"""
        min_path = min(min_path, current_pathweight) 
        print("After comparation, the newly-updated min_path has value of ", min_path)
        if not next_permutation(vertex): 
            break
    return min_path 
# next_permutation implementation 
def next_permutation(L): 
    n = len(L) 
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]: 
        i -= 1
    if i == -1: 
        return False
    j = i + 1
    while j < n and L[j] > L[i]: 
        j += 1
    j -= 1
    L[i], L[j] = L[j], L[i] 
    left = i + 1
    right = n - 1
    while left < right: 
        L[left], L[right] = L[right], L[left] 
        left += 1
        right -= 1
    return True
# Driver Code 
if __name__ == "__main__": 
    # matrix representation of graph 
    """graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]] """
    graph = [[0, 10, 15, 20, 100], [10, 0, 35, 25, 101], 
            [15, 35, 0, 30, 1],[20, 25, 30, 0, 2], [100, 101, 1,2,0]] 
            
    s = 0
    print(travellingSalesmanProblem(graph, s)) 
