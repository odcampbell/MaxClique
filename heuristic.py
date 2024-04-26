import sys
import time
import random
from mf_common import read_lower_triangular_matrix, create_full_matrix , print_to_file, load_data, save_full_matrix, load_full_matrix


# Runs Greedy solution x many times depending on graphs size
def num_iterations(n):
    if n <= 500:
        return 1000
    elif n <= 2500:
        return 600
    elif n <= 8000:
        return 300
    elif n <= 16000:
        return 60
    else:
        return 1
# end num iterations

# Choose a random vertex from the remaining vertices
# Add the vertex to the current clique if it's adjacent to all vertices in the clique
# Remove vertices that are not adjacent to the chosen vertex
def greedy_max_clique(adj_matrix):
    n = len(adj_matrix)
    numTimes = num_iterations(n)
    print("NumTimes: ",numTimes)
    best_clique = set()
    
    for _ in range(numTimes):
        max_clique = set()
        remaining_vertices = set(range(n))
         # Convert set to list, shuffle it, and convert back to set

        while remaining_vertices:
            # Choose a random vertex from the remaining vertices
            v = random.choice(tuple(remaining_vertices))
            remaining_vertices.remove(v)

            # Add the vertex to the current clique if it's adjacent to all vertices in the clique
            if all(adj_matrix[v][u] == 1 for u in max_clique):
                max_clique.add(v)

                # Update vertices to be only those adjacent to the current vertex
                remaining_vertices = remaining_vertices.intersection(u for u in range(n) if adj_matrix[v][u] == 1)
        
        if len(max_clique) > len(best_clique):
            best_clique = max_clique
        
        # print("\n Curr: ", max_clique)
        
    # print("\n Best: ", best_clique)

    return best_clique
# end heuristic

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script_name.py file_path")
        sys.exit(1)

    file_path = sys.argv[1]

    # Use these instead of load_data to NOT store full matrix
    # lower_triangular_matrix = read_lower_triangular_matrix(file_path)
    # full_matrix = create_full_matrix(lower_triangular_matrix)

    full_matrix = load_data(file_path)

    # print_matrix(full_matrix)
    start_time = time.time()
    max = greedy_max_clique(full_matrix)
    elapsed_time = time.time() - start_time
    print("H clique:", max )
    print("H clique Size:", len(max) )
    print("Time:", elapsed_time )

    output_file_name = "Max_Output\Heuristic.txt"
    print_to_file(output_file_name, file_path, elapsed_time, max)
