from .node import Node
neighboring_index = [(0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def A_Star(graph, start, end):
    startNode = Node(None, start)
    endNode  = Node(None, end)
    open_list = set()
    closed_list = set()
    height = len(graph) -1
    width = len(graph[0]) -1

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
            return path[::-1]


        neighbors = []
        for i in neighboring_index:
            neighbor_index = currentNode.position[0]+i[0], currentNode.position[1]+i[1]
            if not((min(neighbor_index[0], neighbor_index[1]) < 0) or neighbor_index[0] > height or neighbor_index[1] > width):
                if graph[neighbor_index[0]][neighbor_index[1]] == 0:
                    neighbors.append(Node(currentNode, neighbor_index))


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
