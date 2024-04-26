import sys
import time
from mf_common import create_full_matrix , read_lower_triangular_matrix, print_matrix, print_to_file

# Given a subset graph and list of nodes, for each node, this function checks
# all possible combinations of nodes in the subset to see if the subset is
# fully connected, forming a clique. If so, it returns true.
def is_clique(graph, nodes):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if not graph[nodes[i]][nodes[j]]:
                return False
    return True
# end is clique

# This function iterates over all possible subsets of a graph (2^n) using bitmasking,
# and runs each subset against the is_clique function, storing the largest clique along the way
def max_clique_brute_force(graph):
    max_clique = []
    n = len(graph)
    for i in range(1, 2**n):

        #for each node, create subset using nodes if the jth bit of i is 1
        subset = [j for j in range(n) if (i >> j) & 1] 
        if is_clique(graph, subset) and len(subset) > len(max_clique):
            max_clique = subset
    return max_clique


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script_name.py file_path")
        sys.exit(1)

    file_path = sys.argv[1]

    # read matrix from file, then build full matrix
    lower_triangular_matrix = read_lower_triangular_matrix(file_path)
    full_matrix = create_full_matrix(lower_triangular_matrix)

    # print_matrix(full_matrix)

    # Track time of max clique brute force
    start_time = time.time()
    max = max_clique_brute_force(full_matrix)
    elapsed_time = time.time() - start_time

    print("Maximum clique:", max )
    print("Maximum clique Size:", len(max) )
    print("Time:", elapsed_time )

    output_file_name = "Max_Output\Brute_Force.txt"
    print_to_file(output_file_name,file_path, elapsed_time, max)