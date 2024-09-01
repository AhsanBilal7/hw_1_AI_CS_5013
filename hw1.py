# Problem: Implement the Breadth-First Search (BFS), Depth-First Search (DFS) 
# and Greedy Best-First Search (GBFS) algorithms on the graph from Figure 1 in hw1.pdf.


# Instructions:
# 1. Represent the graph from Figure 1 in any format (e.g. adjacency matrix, adjacency list).
# 2. Each function should take in the starting node as a string. Assume the search is being performed on
#    the graph from Figure 1.
#    It should return a list of all node labels (strings) that were expanded in the order they where expanded.
#    If there is a tie for which node is expanded next, expand the one that comes first in the alphabet.
# 3. You should only modify the graph representation and the function body below where indicated.
# 4. Do not modify the function signature or provided test cases. You may add helper functions. 
# 5. Upload the completed homework to Gradescope, it must be named 'hw1.py'.

# Examples:
#     The test cases below call each search function on node 'S' and node 'A'
# -----------------------------
import math
from collections import deque
graph = {
  'A' : { 'B' : 4 , 'E' : 1},  
  'B' : { 'A' : 4 , 'C' : 2, 'F' : 2 },  
  'C' : { 'B' : 2 , 'H' : 4, 'S' : 3 },  
  'D' : { 'S' : 2 , 'L' : 8 },  
  'E' : { 'A' : 1 , 'I' : 6, 'F' : 3 },  
  'F' : { 'B' : 2 , 'E' : 3, 'J' : 6, 'K' : 4 },  
  'G' : { 'M' : 4 , 'N' : 4, 'Q' : 10 },  
  'H' : { 'C' : 4 , 'K' : 3, 'L' : 7 },  
  'I' : { 'E' : 6 , 'M' : 5, 'J' : 1 },  
  'J' : { 'I' : 1 , 'F' : 6, 'K' : 3, 'N' : 3 },  
  'K' : { 'F' : 4 , 'J' : 3, 'P' : 3, 'H' : 3, 'L' : 9 },  
  'L' : { 'H' : 7 , 'K' : 9, 'D' : 8, 'Q' : 10 },  
  'M' : { 'I' : 5 , 'G' : 4 },  
  'N' : { 'J' : 3 , 'G' : 4, 'P' : 2 },  
  'P' : { 'N' : 2 , 'K' : 3 },  
  'Q' : { 'G' : 10 , 'L' : 10 },  
  'S' : { 'C' : 3 , 'D' : 3 },  
}

cheapest_path = {
    'S' : 17,
    'A' : 10,
    'B' : 9,
    'C' : 16,
    'D' : 21,
    'G' : 0,
    'E' : 13,
    'F' : 9,
    'H' : 12,
    'I' : 9,
    'J' : 5,
    'K' : 8,
    'L' : 18,
    'M' : 3,
    'N' : 4,
    'P' : 6,
    'Q' : 9,
}
destination_node = 'G'
def lowest_value_item_in_dict(dictionary: dict) -> str:
    lowest_value = math.inf
    lowest_key = None
    for key, value in dictionary.items():
        if lowest_value > value: 
            lowest_value = value
            lowest_key = key
    return lowest_key

def BFS(start: str) -> list:
    # START: Your code here
    queue = deque() # Maintain the queue
    current_node_key = start
    temp_graph = graph.copy()
    # visited = set([])
    visited = []
    queue.append(start)
    while current_node_key != destination_node:
        current_node_key = queue.popleft()
        current_node_dict = temp_graph.pop(current_node_key)

        # print(current_node_dict)
        # current_node_dict = dict(sorted(current_node_dict.items(), key=lambda item: (item[1], item[0]), reverse=True))
        current_node_dict = dict(sorted(current_node_dict.items(), key=lambda item: (item[0]), reverse=False))
        # print(current_node_dict)
        # print("-----------")
        for node,j in current_node_dict.items():
            # node = current_node_dict.popitem()[0]
            if (node not in visited) and (node not in queue):
                queue.append(node)
                # print("Current: ", current_node_key)
        visited.append(current_node_key)
        if destination_node in current_node_dict.keys():
            visited.append(destination_node)
            break

        print(visited, queue)
        # else:
    print("===== BFS Result ======")
    print(visited)
    print("========================")
    return visited
    # END: Your code here


def DFS(start: str) -> list:
    # START: Your code here
    queue = deque() # Maintain the queue
    current_node_key = start
    temp_graph = graph.copy()
    # visited = set([])
    visited = []
    queue.append(start)
    while current_node_key != destination_node:
        current_node_key = queue.pop()
        current_visiting_node_dict = temp_graph.pop(current_node_key)
        current_visiting_node_dict = dict(sorted(current_visiting_node_dict.items(), key= lambda item: item[0], reverse=True))
        for node, key in current_visiting_node_dict.items():
            if node not in visited:
                queue.append(node)
        
        
        print("Current: ", current_node_key)
        visited.append(current_node_key)
        if destination_node in current_visiting_node_dict.keys():
            visited.append(destination_node)
            break
    
    print("===== DFS Result ======")
    print(visited)
    print("========================")
    return visited
    # END: Your code here


def GBFS(start: str) -> list:
    queue = deque() # Maintain the queue
    current_node_key = start
    temp_graph = graph.copy()
    # visited = set([])
    visited = [start]
    queue.append(start)
    # START: Your code here
    while current_node_key != destination_node:
        # straight_line_distance_nodeto_goal = cheapest_path[current_node_key]
        current_node_dict = temp_graph.pop(current_node_key)
        current_node_dict = dict(sorted(current_node_dict.items(), key= lambda item : (cheapest_path[item[0]]), reverse= False)) # Ascending Order
        current_node_key = list(current_node_dict.keys())[0]
        visited.append(current_node_key)
    print("===== GBFS Result ======")
    print(visited)
    print("========================")
    return visited
    # END: Your code here



# test cases - DO NOT MODIFY THESE
def run_tests():
    # Test case 1: BFS starting from node 'A'
    assert BFS('A') == ['A', 'B', 'E', 'C', 'F', 'I', 'H', 'S', 'J', 'K', 'M', 'G'], "Test case 1 failed"
    
    # Test case 2: BFS starting from node 'S'
    assert BFS('S') == ['S', 'C', 'D', 'B', 'H', 'L', 'A', 'F', 'K', 'Q', 'G'], "Test case 2 failed"

    # Test case 3: DFS starting from node 'A'
    assert DFS('A') == ['A', 'B', 'C', 'H', 'K', 'F', 'E', 'I', 'J', 'N', 'G'], "Test case 3 failed"
    
    # Test case 4: DFS starting from node 'S'
    assert DFS('S') == ['S', 'C', 'B', 'A', 'E', 'F', 'J', 'I', 'M', 'G'], "Test case 4 failed"

    # Test case 5: GBFS starting from node 'A'
    assert GBFS('A') == ['A', 'B', 'F', 'J', 'N', 'G'], "Test case 5 failed"
    
    # Test case 6: GBFS starting from node 'S'
    assert GBFS('S') == ['S', 'C', 'B', 'F', 'J', 'N', 'G'], "Test case 6 failed"

    
    
    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
