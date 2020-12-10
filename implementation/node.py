class Node:
    def __init__(self, parent=None, position=None):
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position == other.position
    def __hash__(self):
        return (hash(self.position[0]) ^ self.position[1])

    def __repr__(self):
        return str((self.position[0], self.position[1]))

    def calculate_cost(self, parent, end_node):
        # setting g cost of child to 10 if the node is vertical or horizontal if diagonal set g = 14
        if self.position[0] == parent.position[0] or self.position[1] == parent.position[1]:
            self.g = parent.g + 10
        else:
            self.g = parent.g + 14

        # setting h cost to that of calculated by eucledian hueristics times 10
        self.h = ((end_node.position[0]-self.position[0])**2 + (end_node.position[1]-self.position[1])**2)*10
        self.f = self.g + self.h