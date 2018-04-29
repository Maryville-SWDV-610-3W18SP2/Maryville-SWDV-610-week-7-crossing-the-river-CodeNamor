#F. Derek Roman -      GitHub Profile Name:    CodeNamor
#SWDV - 610-3W:          Data Structures Week 7 Assignment        Crossing the River

#import the state class
from state import State
from Node import Node
from collections import deque
import time
#implement a breadth first search for solving the problem
def breadth_first_tree_search(initial_state):
  initial_node = Node(
                      parent_node=None,
                      state=initial_state,
                      action=None,
                      depth=0)
  #first in first out using a deque on the inital node
  comb = deque([initial_node])
  num_expansions = 0
  max_depth = -1
  while True:
    node = comb.popleft()
    if node.state.is_goal_state():
      solution = node.extract_solution()
      return solution
    num_expansions += 1
    comb.extend(node.expand())

def main():
    #define the inital state of 3 cannibals, 3 missionaries and 1 boat
  initial_state = State(3,3,1)
  #implement a BFS to find the solution
  solution = breadth_first_tree_search(initial_state)
  #check if there is a solution
  if solution is None:
      #if no solution
    print("no solution")
  else:
      #otherwise print out the solution steps
    print("solution (%d steps):" % len(solution))
    for step in solution:
        #formattted printing for each solution step
      print("%s" % step)

main()



