import sys
import time
from mf_common import read_lower_triangular_matrix, create_full_matrix

def clique_heuristic(graph):
    max_clique = []
    n = len(graph)
    vertices = set(range(n))

    while vertices:
        # Step 1: Start with an arbitrary vertex
        v = vertices.pop()
        clique = {v}
        neighbors = set(graph[v])

        # Step 2: Iteratively expand the clique
        while neighbors:
            # Find the vertex with the most connections to the current clique
            u = max(neighbors, key=lambda u: sum(1 for w in clique if graph[u][w]))

            # Check if u can be added to the clique
            if all(graph[u][w] for w in clique):
                clique.add(u)
                neighbors |= set(graph[u]) - clique  # Update neighbors to include unprocessed vertices

            neighbors.remove(u)  # Remove u from neighbors as it's processed

        # Step 3: Update the maximum clique
        if len(clique) > len(max_clique):
            max_clique = list(clique)

        vertices -= clique  # Remove vertices in the clique from consideration

    return max_clique

if __name__ == "__main__":
# Example usage:
    # adjacency_matrix = [
    #     [0, 1, 1, 0],
    #     [1, 0, 1, 1],
    #     [1, 1, 0, 1],
    #     [0, 1, 1, 0]
    # ]


    if len(sys.argv) != 2:
        print("Usage: python script_name.py file_path")
        sys.exit(1)

    file_path = sys.argv[1]

    lower_triangular_matrix = read_lower_triangular_matrix(file_path)
    # comp_edges(lower_triangular_matrix)
    full_matrix = create_full_matrix(lower_triangular_matrix)

    # print_matrix(full_matrix)
    start_time = time.time()
    max = clique_heuristic(full_matrix)
    elapsed_time = time.time() - start_time
    print("H clique:", max )
    print("H clique Size:", len(max) )
    print("Time:", elapsed_time )
