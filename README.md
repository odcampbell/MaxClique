# MaxClique

## Setting up your local git repo with this remote repo:
1. Use this command to make a copy of the remote repository:

    1. **git clone https://github.com/odcampbell/MaxClique.git**

    2. You should now have the folder MaxClique

2. Navigate into that folder with command: **cd MaxClique**

3. You should now see all of the code for this project.


## About
This project contains three python files **bruteForce.py**, **vectorCover.py**, and **heuristic.py** that take one file as input in a lower triangular adjacency matrix form of 0's and 1's, with the first number in each row representing the vertex.
Some sample graphs are located in the **Graphs** folder, and code output will go to both the screen and output files in **Max_Output**.

Brute Force gets unreasonably slow handling graphs with over 25 vertices.
Vertex cover performs quickly but outputs poor cliques.

## Heuristic

### Attempts
My heuristic, a greedy approach, performs quickly and outputs okay cliques (really bad cliques but not as bad as vertex cover). I tried a few different algorithms, including one similar to Prims that looked for maximal instead maximum cliques. Once I realized that, I tried others like bron_kerbosh but that wasn't a fast enough solution for my liking, rivaling my non optimized brute force solution in slowness.

### Greedy
I settled with a greedy approach that chooses a random vertex, compares it to current clique, adds it to the clique if it fits, then tries all of its neighbors until no more vertices are left to check.

Since this solution can differ based on the order of nodes chosen, I decided to tweak it a bit by adding in a different number of iterations based on the node size, randomizing the vertex selection instead of going from 1-n each time, and keeping track of my largest clique.

This makes it perform a little better than my prior greedy approach which only ran one time on the graph and only randomized the inital node selection instead of all of them. Id like to explore more optimization techniques to see what we can get out of a greedy heuristic in the future.

Also, the heurstic code will use the python pickle module to save the full matrix version of any graph you run. This is to reduce setup time for running the code. If you'd rather not use the extra (2x) space and just rebuild the matrix each time, just comment out the line in heuristic.py that reads: **full_matrix = load_data(file_path)**

## Example Run Commands

py heuristic.py Graphs/G3000.adjmat
py vertexCover.py Graphs/G3000.adjmat
py bruteForce.py Graphs/test24.adjmat  