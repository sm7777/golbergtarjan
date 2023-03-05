# Goldberg-Tarjan Push-Relabel algorithm for maximum flow
#
# Andrew V. Goldberg and Robert E. Tarjan. “A New Approach to the Maximum-Flow
# Problem”. In: Journal of the Association for Computing Machinery 35.4 (1988)


def able_to_push(vertex, vertices, arcs, neighbors):
    neighbor_list = neighbors[vertex]
    full_neighbors = 0
    downstream_neighbors = 0

    for neighbor in neighbor_list:

        if(neighbor[1] == 1):
            break

        residual_capacity = arcs[(vertex, neighbor[0])][1] - arcs[(vertex, neighbor[0])][0]
        if(residual_capacity > 0 and vertices[vertex][1] == vertices[neighbor[0]][1] + 1):
            return neighbor
        
        if(residual_capacity == 0):
            full_neighbors += 1
        
        downstream_neighbors += 1
    
    if(full_neighbors == downstream_neighbors and vertices[vertex][1] == vertices[neighbor[0]][1] + 1):
        return neighbor

    return (-1, -1)

def push(active_vertex, neighbor_to_push, vertices, arcs, backflow_arcs):

    if(neighbor_to_push[1] == 0): #when flowing downstream
        residual_capacity = arcs[(active_vertex, neighbor_to_push[0])][1] - arcs[(active_vertex, neighbor_to_push[0])][0]
        delta_flow = min(vertices[active_vertex][0], residual_capacity)
        preflow = arcs[(active_vertex, neighbor_to_push[0])]
        preflow[0] += delta_flow
        arcs[(active_vertex, neighbor_to_push[0])] = preflow
    else: #when pushing back to source
        delta_flow = vertices[active_vertex][0]
        backflow_arcs[(active_vertex, neighbor_to_push[0])] = delta_flow
        if(neighbor_to_push[0] == 0):
            remove_backflow(arcs, backflow_arcs)


    vertices[active_vertex][0] -= delta_flow
    vertices[neighbor_to_push[0]][0] += delta_flow
    
    return

def relabel(vertex, vertices):
    vertices[vertex][1] += 1
    return

def initialize_vertices(num_vertices, source):

    vertices = []
    #vertex: (excess flow, height)

    for i in range(0, num_vertices):
        if(i == source):
            vertex = [0, num_vertices]
        else:
            vertex = [0, 0]
        vertices.append(vertex)

    return vertices

def initialize_arcs(edges, source):
    
    arcs = {}
    #key: [u, v] <-- edge
    #value stored: [preflow, capacity]

    for edge in edges:
        if(edge[0] == source):
            arcs[(edge[0], edge[1])] = [edge[2], edge[2]]
        else:
            arcs[(edge[0], edge[1])] = [0, edge[2]]

    return arcs

def initialize_neighbors(edges):

    neighbors = {}

    end = 1
    for start in range(0, 2):
        for edge in edges:
            neighbor_list = []
            if(edge[start] not in neighbors):
                neighbor_list.append((edge[end], start))
            else:
                neighbor_list = neighbors[edge[start]]
                neighbor_list.append((edge[end], start))
            
            neighbors[edge[start]] = neighbor_list
        end -= 1

    return neighbors

def remove_backflow(arcs, backflow_arcs):
    for (v, u) in backflow_arcs:
        preflow = arcs[(u, v)][0] - backflow_arcs[(v, u)]
        arcs[(u, v)][0] = preflow

    backflow_arcs.clear()

def max_flow(num_vertices, edges, source, sink):

    vertices = initialize_vertices(num_vertices, source)
    arcs = initialize_arcs(edges, source)
    backflow_arcs = {}
    neighbors = initialize_neighbors(edges)
    active_vertices = set()
    for i, j in neighbors[source]:
        active_vertices.add(i)

    for vertex in active_vertices:
        vertices[vertex][0] = arcs[(source, vertex)][0]

    
    while(len(active_vertices) > 0):

        neighbor_to_push = able_to_push(list(active_vertices)[0], vertices, arcs, neighbors)
        if(neighbor_to_push[0] > -1):
            push(list(active_vertices)[0], neighbor_to_push, vertices, arcs, backflow_arcs) 
        else:
            relabel(list(active_vertices)[0], vertices)

        if(vertices[list(active_vertices)[0]][0] == 0):
            active_vertices.discard(list(active_vertices)[0])

        if(neighbor_to_push[0] > 0 and neighbor_to_push[0] != sink):
            active_vertices.add(neighbor_to_push[0])

        
    return (vertices[sink][0], arcs, vertices)