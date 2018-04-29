#F. Derek Roman -      GitHub Profile Name:    CodeNamor
#SWDV - 610-3W:          Data Structures Week 7 Assignment        Crossing the River

#class for defining the state of the missionaries and cannibals
class State(object):
    #initalize the object
  def __init__(self, missionaries, cannibals, boats):
    self.missionaries = missionaries
    self.cannibals = cannibals
    self.boats = boats
  # state succession
  def successors(self):
    if self.boats == 1:
      sgn = -1
      direction = "from the original shore to the new shore"
    else:
      sgn = 1
      direction = "back from the new shore to the original shore"
    for m in range(3):
      for c in range(3):
        newState = State(self.missionaries+sgn*m, self.cannibals+sgn*c, self.boats+sgn*1);
        if m+c >= 1 and m+c <= 2 and newState.isValid():    # check whether action and resulting state are valid
          action = "take %d missionaries and %d cannibals %s. %r" % ( m, c, direction, newState) 
          yield action, newState
    #are the values valid?        
  def isValid(self):
    # inital check of the problem variables
    if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3 or (self.boats != 0 and self.boats != 1):
      return False   
    # do the cannibals outnumber the missionaries on the original shore?
    if self.cannibals > self.missionaries and self.missionaries > 0:    
      return False
    #do the cannibals outnumber the missionaries on the new shore?
    if self.cannibals < self.missionaries and self.missionaries < 3: 
      return False
    return True
    #return values for the goals
  def is_goal_state(self):
    return self.cannibals == 0 and self.missionaries == 0 and self.boats == 0

  def __repr__(self):
    return "< State (%d, %d, %d) >" % (self.missionaries, self.cannibals, self.boats)