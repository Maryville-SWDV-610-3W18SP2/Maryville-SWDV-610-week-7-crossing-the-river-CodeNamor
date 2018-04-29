#F. Derek Roman -      GitHub Profile Name:    CodeNamor
#SWDV - 610-3W:          Data Structures Week 7 Assignment        Crossing the River
#node class for implementing the Breadth first search
class Node(object):
    #initalize the class
  def __init__(self, parent_node, state, action, depth):
    self.parent_node = parent_node
    self.state = state
    self.action = action
    self.depth = depth
  #expand when the action is triggerd for the state of the object
  def expand(self):
    for (action, succ_state) in self.state.successors():
      succ_node = Node(
                       parent_node=self,
                       state=succ_state,
                       action=action,
                       depth=self.depth + 1)
      yield succ_node
    #extract the solution when found
  def extract_solution(self):
        solution = []
        node = self
        #when the parent node is None (null)
        while node.parent_node is not None:
            solution.append(node.action)
            node = node.parent_node
            solution.reverse()
        return solution