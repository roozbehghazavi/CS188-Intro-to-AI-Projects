# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem, but doesn't implement
	any of the methods (in object-oriented terminology: an abstract class).

	You do not need to change anything in this class, ever.
	"""

	def getStartState(self):
		"""
		Returns the start state for the search problem.
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
		  state: Search state

		Returns True if and only if the state is a valid goal state.
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
		  state: Search state

		For a given state, this should return a list of triples, (successor,
		action, stepCost), where 'successor' is a successor to the current
		state, 'action' is the action required to get there, and 'stepCost' is
		the incremental cost of expanding to that successor.
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.
		The sequence must be composed of legal moves.
		"""
		util.raiseNotDefined()


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	from game import Directions
	s = Directions.SOUTH
	w = Directions.WEST
	return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print("Start:", problem.getStartState())
	print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
	print("Start's successors:", problem.getSuccessors(problem.getStartState()))
	"""
	"*** YOUR CODE HERE ***"
	from util import Stack
	from game import Directions

	#agar noghte shoroo goal bood list khali az action ha bar migardoonim.
	if(problem.isGoalState(problem.getStartState())):
		return []

	#implement kardane (poshte)
	my_stack=Stack()
	#visited
	seen_list=list()
	#result
	res=list()

	#avalin node ra be dakhele stack push mikonim
	my_stack.push((problem.getStartState(),list()))
	
	while(True):
		#agar poshte khali bood list khali az action ha return mishavad
		if(my_stack.isEmpty()):
			return list()

		#dar in marhale elem barabare (x,y) va res barabare list jahat ha ast.
		elem,res= my_stack.pop()

		#agar elem goal bood masir return shavad
		if(problem.isGoalState(elem)):
			return res
		
		#ezafe kardane elem be list visited
		seen_list.append(elem)   
		#peida kardane hamsaye haye elem + jahat haye anha         
		successors=problem.getSuccessors(elem)

		if(len(successors)!=0):
			for i in successors:
				if(i[0] not in seen_list):
					#i[0] hamsaye va i[1] jahat hamsaye ast
					my_stack.push((i[0],res+[i[1]]))

		# print(successors)

	

def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""
	"*** YOUR CODE HERE ***"
	from util import Queue
	from game import Directions

	#Implement kardane saf
	my_queue = Queue()
	#Implement kardane visited list
	seen_list = list()
	#Result
	res=list()

	#avalin node ra be dakhele queue push mikonim
	my_queue.push((problem.getStartState(),list()))
	
	while(True):
	
		#agar saf khali bood list khali az action ha return mishavad
		if my_queue.isEmpty():
			return list()
			
		#dar in marhale elem barabare (x,y) va res barabare list jahat ha ast.
		elem, res = my_queue.pop()
	   
		#agar elem goal bood masir return shavad
		if problem.isGoalState(elem):
			return res

		#ezafe kardane elem be list visited
		seen_list.append(elem)
		#peida kardane hamsaye haye elem + jahat haye anha
		successors = problem.getSuccessors(elem)

		if(len(successors)!=0):
			for i in successors:
				#i[0] hamsaye va i[1] jahat hamsaye ast
				if (i[0] not in seen_list and i[0] not in (j[0] for j in my_queue.list)):
					my_queue.push((i[0],res + [i[1]]))

def uniformCostSearch(problem):
	"""Search the node of least total cost first."""
	"*** YOUR CODE HERE ***"
	from util import PriorityQueue
	from game import Directions

	#Implement kardane saf olaviat
	my_Pqueue = PriorityQueue()
	#Implement kardane visited list
	seen_list = list()
	#Result
	res=list()

	#avalin node ra be dakhele priority queue push mikonim
	my_Pqueue.push((problem.getStartState(),list()),0)
	
	while(True):
	
		#agar saf olaviat khali bood list khali az action ha return mishavad
		if my_Pqueue.isEmpty():
			return list()
			
		#dar in marhale elem barabare (x,y) va res barabare list jahat ha ast.
		elem, res = my_Pqueue.pop()
	   
		#agar elem goal bood masir return shavad
		if problem.isGoalState(elem):
			return res

		#ezafe kardane elem be list visited
		seen_list.append(elem)
		#peida kardane hamsaye haye elem + jahat haye anha
		successors = problem.getSuccessors(elem)

		for i in successors:
			if (i[0] not in seen_list) and (i[0] not in (j[2][0] for j in my_Pqueue.heap)):
				#i[1]= jahate successor
				cost = problem.getCostOfActions(res + [i[1]])
				my_Pqueue.push((i[0], res + [i[1]]),cost)

			if (i[0] not in seen_list) and (i[0] in (j[2][0] for j in my_Pqueue.heap)):
				for s in my_Pqueue.heap:
					if(i[0] == s[2][0]):
						newCost = problem.getCostOfActions(res + [i[1]])
						if(s[0]>newCost):
							my_Pqueue.update((i[0], res + [i[1]]),newCost)
			
			else:
				pass

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"
	from util import PriorityQueue
	from game import Directions

	#Implement kardane saf olaviat
	my_Pqueue = PriorityQueue()
	#Implement kardane visited list
	seen_list = list()
	#Result
	res=list()

	#avalin node ra be dakhele priority queue push mikonim
	my_Pqueue.push((problem.getStartState(),list()),0)
	
	while(True):
	
		#agar saf olaviat khali bood list khali az action ha return mishavad
		if my_Pqueue.isEmpty():
			return list()
			
		#dar in marhale elem barabare (x,y) va res barabare list jahat ha ast.
		elem, res = my_Pqueue.pop()
	   
		#agar elem goal bood masir return shavad
		if problem.isGoalState(elem):
			return res

		#ezafe kardane elem be list visited
		seen_list.append(elem)
		#peida kardane hamsaye haye elem + jahat haye anha
		successors = problem.getSuccessors(elem)

		# manande ucs ama cost + heuristic made nazar ast
		for i in successors:
			if (i[0] not in seen_list) and (i[0] not in (j[2][0] for j in my_Pqueue.heap)):
				#i[1]= jahate successor
				#g(n)+h(n)
				cost = problem.getCostOfActions(res + [i[1]])+heuristic(i[0],problem)
				my_Pqueue.push((i[0], res + [i[1]]),cost)

			if (i[0] not in seen_list) and (i[0] in (j[2][0] for j in my_Pqueue.heap)):
				for s in my_Pqueue.heap:
					if(i[0] == s[2][0]):
						newCost = problem.getCostOfActions(res + [i[1]])+heuristic(i[0],problem)
						if(s[0]>newCost):
							my_Pqueue.update((i[0], res + [i[1]]),newCost)
			
			else:
				pass


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
