#lc_GoogleOnsiteSoftwareEngineer_TravellingSalesperson.py
#An interviewee was asked to implement the Travelling Salesperson Problem using Best-First Search with Brand-and-Bound Pruning 
#ALgorithm
#Problem: Determine an optimal tour in a weighted, directed graph. The weight are non-negative numbers
#Inputs: a weighted, directed graph, and n, the number of vertices in the graph. 
#The graph is represented by a two-dimensional array W, which has both its row and columns indexed from 1 to n, 
#where W[i][j] is the weight on the edge from the ith vertex to the jth vertex.
#Outputs: variable minlength, whose value is the length of an optimal tour, and variable opttour, whose value is an optimal tour. 

#Here was the pseudocode she/he came up with for the main routine. 
#In addition to this pseudocode, she/he was tasked with writing the two supporting subroutines: length() and bound(). 
#She/he ran out of time before getting to these subroutines.
#However, she/he was pretty much confident function length() is supposed to return the length of the tour u.path, 
#and the function bound() returns the bound for a node using the considerations above.
