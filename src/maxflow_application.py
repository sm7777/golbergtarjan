from maxflow import*
import sys

f = open(sys.argv[1], "r")
lines = f.readlines()

edges = []

for i in range(0, len(lines)):
    if i == 0:
        num_vertices = int(lines[i])
    elif i == 1:
        source = int(lines[i])
    elif i == 2:
        sink = int(lines[i])
    else:
        edge_string = lines[i].split(',')
        edge = tuple(map(int, edge_string))
        edges.append(edge)



output = max_flow(num_vertices, edges, source, sink)
maximum = str(output[0])

print("\nMaximum Flow: " + maximum + "\n")
print("Flow in Arcs at End (Preflow / Capacity): \n")
for i, j in output[1]:
    print("Arc " +"(" + str(i) + "," + str(j) + "): " + str(output[1][i, j][0]) + " / " + str(output[1][i, j][1]))

print("\nExcess Flow and Height of Vertex at End (Excess Flow | Height):\n")
for i in range(0, len(output[2])):
    if i == 0:
        print("Source:      " + str(output[2][i][0]) + " | " + str(output[2][i][1]))
    elif i == len(output[2]) - 1:
        print("Sink:       " + str(output[2][i][0]) + " | " + str(output[2][i][1]) + "\n")
    else:
        print("Vertex " + str(i) + ":    " + str(output[2][i][0]) + " | " + str(output[2][i][1]))

