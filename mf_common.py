import pickle
import os

# Reads in a lower triangular matrix from a file, skipping the first number which is a 
# node/vertex indicator, then adds each clean line to a lower triangular matrix to return
def read_lower_triangular_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    matrix = []

    # Skip the first line if it contains only one number
    if len(lines[0].split()) == 1:
        lines.pop(0)

    for line in lines:
        parts = line.split()[1:]  # Skip the first number
        row = [int(part) for part in parts]
        matrix.append(row)

    return matrix
# end read lower 

# Given a lower triangular matrix represented by a list of lists, this function makes it
# a symmetrical matrix, and thus full matrix by copying the lower values to the upper 
# portion
def create_full_matrix(lower_triangle_matrix): # O(N)
    size = len(lower_triangle_matrix)

    # Create a full matrix and fill it using the lower triangular matrix
    full_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i + 1):
            full_matrix[i][j] = lower_triangle_matrix[i][j]
            full_matrix[j][i] = lower_triangle_matrix[i][j]

    return full_matrix
# end full matrix

# prints a list of lists, which is the format my lower triangular and full matrix are
def print_matrix(matrix): 
    count = 0
    for row in matrix:
        if count >= 20:
            break
        print(row)
        count += 1
# end print matrix

def print_to_file(file_name, source_file, runtime, maxClique):
    with open(file_name, 'a') as output_file:
         output_file.write("\n\nGraph from: " + str(source_file))
         output_file.write("\nMaximum clique: " + str(maxClique))
         output_file.write("\nMaximum clique Size:"+ str(len(maxClique)) )
         output_file.write("\nTime:"+ str(runtime) )
# end print to file

def save_full_matrix(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def load_full_matrix(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

# tries saving full graph instead of making it every time. Feel free to 
# use read_lower and create_full in main instead to save space
def load_data(graph_file):
    pkl_file = graph_file + ".pkl"
    if os.path.exists(pkl_file):  # Check if the .pkl file exists
        print("Found it!")
        with open(pkl_file, 'rb') as file:
            data = pickle.load(file)
    else:
        lower_triangular_matrix = read_lower_triangular_matrix(graph_file)
        data = create_full_matrix(lower_triangular_matrix)
        with open(pkl_file, 'wb') as file:
            pickle.dump(data, file)
    return data