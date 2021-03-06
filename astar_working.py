# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
	g = 0

	open = [[g,init[0],init[1]]]

	g = g + cost

	for d in range(len(delta)):
		x = delta[d][0]
		y = delta[d][1]
		if grid[x][y] == 0:
			if init[0]+x >= 0:
				x = init[0]+x
				if init[1]+y >= 0:
					y = init[1]+y
					open.append([g,x,y])
	# for i in range(len(open)):
		# if open[i][0] == 0:
			# open.pop([i])
	return open