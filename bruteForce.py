import sys
import time
from mf_common import read_lower_triangular_matrix, create_full_matrix

def print_matrix(matrix): 
    count = 0
    for row in matrix:
        if count >= 20:
            break
        print(row)
        count += 1
# end print matrix

def is_clique(graph, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if not graph[nodes[i]][nodes[j]]:
                return False
    return True

def max_clique_brute_force(graph):
    max_clique = []
    n = len(graph)
    for i in range(1, 2**n):
        subset = [j for j in range(n) if (i >> j) & 1]
        if is_clique(graph, subset) and len(subset) > len(max_clique):
            max_clique = subset
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
    max = max_clique_brute_force(full_matrix)
    elapsed_time = time.time() - start_time
    print("Maximum clique:", max )
    print("Maximum clique Size:", len(max) )
    print("Time:", elapsed_time )
