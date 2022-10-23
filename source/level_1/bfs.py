from queue import Queue
from utils import Maze
from utils import Node


class BFS_Queue():
    def __init__(self):
        self.List = []
        self.Queue = Queue()
        
    def put(self, pair):
        self.List.append(pair)
        self.Queue.put(pair)

    def get(self):
        pair = self.Queue.get()
        self.List.remove(pair)
        return pair

    def checkExistState(self, state):
        for x in self.List:
            if state == x[0]:
                return True
        return False

    def empty(self):
        return self.Queue.empty()

class BFS_Maze(Maze):
    def bfsMarkedNode(self):
        """Find a solution to maze, if one exists"""

        # keep track of number of states explored
        # self.num_explored = 0

        # initialize an empty explored set
        self.explored = set()

        # initialize start node
        start = Node(self.start, parent=None, action=None)

        # check if start node is the goal node
        if start.state == self.goal:
            return start

        # contain the set of child node
        frontier = BFS_Queue()
        frontier.put((start, 0))
        self.draw_explored.append((start.state, 0))

        self.explored.add(start.state)

        # do loops until no child node to expand
        while True:
            if frontier.empty():
                raise NameError("no solution")
                
            # take a node from set
            tempNode, cur_cost = frontier.get()
            # self.explored.add(tempNode.state)
            self.draw_explored.append((tempNode.state, 1))
            # self.solution.append(tempNode.action, tempNode.state)
            # self.num_explored += 1

            for action, state in self.generateSuccessors(tempNode.state):
                if state not in self.explored and not frontier.checkExistState(state):
                    # initialzie a child node
                    child = Node(state=state, parent=tempNode, action=action)
                    if child.state == self.goal:
                        return child, cur_cost + 1
                        
                    # child.updateCost()

                    # add child node into frontier and mark it
                    frontier.put((child, cur_cost + 1))
                    self.explored.add(child.state)

                    self.draw_explored.append((child.state, 0))

        
    def bfs_Search(self):
        action = []
        cells = []
        
        tempNode, path_cost = self.bfsMarkedNode()
        
        while True:
            action.append(tempNode.action)
            cells.append(tempNode.state)
            tempNode = tempNode.parent
            if tempNode.state == self.start:
                break
        
        cells.append(self.start)
        action.reverse()
        cells.reverse()
        
        self.solution = (action, cells)
        return path_cost
        