import networkx as nx 
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices:"))

if n <= 3:
    print("Number of vertices must be greater than 3.")
else:
    G = nx.complete_graph(n)
    print("\nEdges of the complete graph:")
    print(list(G.edges()))
    nx.draw(G, with_labels=True)
    plt.title(f"Complete Graph with {n} vertices") 
    plt.show()   