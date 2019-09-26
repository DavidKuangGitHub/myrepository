#py_ListComprehensions_viaHackerrank_com_ws.py Example Input 
#1
#1
#1
#2
#Example Output:
#[[0,0,0], [0,0,1],[0,1,0],[1,0,0],[1,1,1]]
#Another Example would be 2 2 2 2 each digit following by an enter

print("Enter 4 integers with certain conditions x+y+z <> n: ")
x, y, z, n = int(input()), int(input()),int(input()),int(input())
print("Results:")
#print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n])
print([[a,b,c] 
    for a in range(0,x+1) 
        for b in range(0,y+1) 
            for c in range(0,z+1) 
                if a + b + c != n])
