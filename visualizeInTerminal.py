from  copy import deepcopy
import time
import os


from node import Node
neighboring_index = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
def print_per_line(graph):
	for i in graph:
		print(i)
	time.sleep(0.4)
	





def A_Star(graph, start, end, showStep=False):
    startNode = Node(None, start)
    start_t = '$'
    end_t = '&'
    path_t = '%'
    search_t = '#'
    endNode  = Node(None, end)
    open_list = set()
    closed_list = set()
    height = len(graph) -1
    width = len(graph[0]) -1
    graph_t = deepcopy(graph)
    graph_t[start[0]][start[1]] = start_t
    graph_t[end[0]][end[1]] = end_t
    print_per_line(graph_t)
    open_list.add(startNode)

    while open_list:
        currentNode = min(open_list, key=lambda i: i.f)

        open_list.remove(currentNode)
        closed_list.add(currentNode)

        if currentNode == endNode:
            path = []
            while currentNode:
                path.append(currentNode)
                currentNode = currentNode.parent
            for i in path:
            	os.system('clear')
            	graph_t[i.position[0]][i.position[1]] = path_t
            	print_per_line(graph_t)
            return path[::-1]


        neighbors = []
        for i in neighboring_index:
            neighbor_index = currentNode.position[0]+i[0], currentNode.position[1]+i[1]
            if not((min(neighbor_index[0], neighbor_index[1]) < 0) or neighbor_index[0] > height or neighbor_index[1] > width):
                if graph[neighbor_index[0]][neighbor_index[1]] == 0:
                    neighbors.append(Node(currentNode, neighbor_index))
        os.system('clear')
        for i in neighbors:
        	graph_t[i.position[0]][i.position[1]] = search_t
        	print_per_line(graph_t)
        	os.system('clear')

        for neighbor in neighbors:
            if not(neighbor in closed_list):
                if neighbor.position[0] == currentNode.position[0] or neighbor.position[1] == currentNode.position[1]:
                    new_g = currentNode.g + 10
                else:
                    new_g = currentNode.g + 14

                if neighbor in open_list:
                    if new_g < neighbor.g:
                        neighbor.calculate_cost(currentNode, endNode)
                        neighbor.parent = currentNode
                else:
                    neighbor.parent = currentNode
                    neighbor.calculate_cost(currentNode, endNode)
                    open_list.add(neighbor)
    return 'No path found'


