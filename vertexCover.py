import sys
import time
from mf_common import create_full_matrix , read_lower_triangular_matrix, print_matrix,print_to_file

'''
This code relies on the relationship between the clique, vertex cover, and indpendent set of a graph.
Steps:
    1. Get lower triangular adjacency matrix (representing graph G) from file
    2. Turn it into a full adjacency matrix
    3. Find its complement graph
    4. Construct the vertex cover of the complement graph
    5. Find the independent set of the complement graph = max clique of G
'''

# Builds a complement matrix by initializing a matrix (of same size) with zeros
# then traversing adj matrix and flipping 0's (in adj matrix) to ones in the complement
def find_complement(adj_matrix):
    num_vertices = len(adj_matrix)
    complement_matrix = [[0]*num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and adj_matrix[i][j] == 0:
                complement_matrix[i][j] = 1

    return complement_matrix
# end complement

# Traversing the adjacency matrix looking for pairs of ndoes that have a connection,
# Adds the node with fewer edjges to the vertex cover (if it is not in it already)
def find_vertex_cover(adj_matrix):
    num_vertices = len(adj_matrix)
    vertex_cover = set()

    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if adj_matrix[i][j] == 1 and i not in vertex_cover and j not in vertex_cover:
                # Choose the vertex with fewer incident edges to include in the cover
                if adj_matrix[i].count(1) < adj_matrix[j].count(1):
                    vertex_cover.add(i)
                else:
                    vertex_cover.add(j)

    return vertex_cover
# end find vertex cover

'''
    Follows these steps to find a max clique:
    3. Find its complement graph
    4. Construct the vertex cover of the complement graph
    5. Find the independent set of the complement graph = max clique of G
'''
def find_max_clique(adj_matrix):
    complement_matrix = find_complement(adj_matrix)
    # print("Complement graph:", complement_matrix)

    vertex_cover = find_vertex_cover(complement_matrix)
    # print("Vertex cover:", vertex_cover)

    num_vertices = len(adj_matrix)
    independent_set = set(range(num_vertices)) - vertex_cover

    return independent_set
# end find max clique

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
    max_clique = find_max_clique(full_matrix)
    elapsed_time = time.time() - start_time

    print("Maximum clique:", max_clique )
    print("Maximum clique Size:", len(max_clique) )
    print("Time:", elapsed_time )

    output_file_name = "Max_Output\Vertex_Cover.txt"
    print_to_file(output_file_name,file_path, elapsed_time, max_clique)