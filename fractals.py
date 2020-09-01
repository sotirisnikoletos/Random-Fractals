import numpy as np
#------------------------------------------------------------------------
def neighbors(i, j, grid_size):	
	list=[]
	if ((j + grid_size - 1) % grid_size) <= j: #upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto deksia meros
		list.append([i,(j + grid_size - 1) % grid_size])#to ekxoroume sthn lissta
	if ((j + 1) % grid_size) >= j:#upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto aristero meros
		list.append([i,(j + 1) % grid_size])
	if ((i + grid_size - 1) % grid_size) <= i:#upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto katw meros
		list.append([(i + grid_size - 1) % grid_size, j])            #dhlwsh sunarthsh
	if ((i + 1) % grid_size)>= i:#upologizoume an to swmatidio den vriskete sta akra kai sugkekrimena sto panw meros
		list.append ([(i + 1) % grid_size, j])	
	arr1 = np.array(list)
	return (arr1)
	
def count_neighbors(i, j, grid):
	idx = neighbors(i, j, grid.shape[0])
	return np.sum(grid[idx[:, 0], idx[:, 1]])
#-----------------------------------------------------------------------------
# Define the grid size
grid_size = 50

# Create a square grid of empty sites
grid = np.full((grid_size , grid_size), False) 

# Find all empty sites
empty_sites_idx = np.argwhere(grid==False)                                       #arxikopohsh tou can_move wste na mporei na mpei sth while kai kanei epanalipseis me vash an mporoun na kounithon ta swmathdia

# Select randomly an empty site 
new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]

# Convert indices to tuple
new_empty_site = tuple(new_empty_site)

# Place a new particle
grid[new_empty_site] = True 
idx = np.argwhere(grid==True)
can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
count=0# mia metavlith gia na vlepoume posa stoixeia exoun mpei 
#-----------------------------------------------------------------------------------

while can_move.size:
	p=0.4
	if np.random.rand() > p:
		continue
	empty_sites_idx = np.argwhere(grid==False) # Find all empty sites
	# Select randomly an empty site 
	new_empty_site = empty_sites_idx[np.random.randint(empty_sites_idx.shape[0])]
	# Convert indices to tuple
	new_empty_site = tuple(new_empty_site)
	# Place a new particle
	grid[new_empty_site] = True 	

	

	# Find the indices of all particles that can move
	idx = np.argwhere(grid==True)
	can_move = idx[[count_neighbors(x[0], x[1], grid) == 0 for x in idx]]
	q = 1

	for i_j in can_move:
		if np.random.rand() > q:
			continue
		i, j = tuple(i_j)
		
		# Select a random movement
		_r = np.random.rand()
		if _r < 0.14:
			grid[i, (j + grid_size - 1) % grid_size] = True #up
		elif _r < 0.32:
			grid[i, (j + 1) % grid_size] = True #down
		elif _r < 0.75:
			grid[(i + grid_size - 1) % grid_size , j] = True #left
		else:
			grid[(i + 1) % grid_size,j] = True #right
		grid[i, j] = False


repetitions = 1000
min_box_size = 3
max_box_size = 7
counts = dict ( zip ( range ( min_box_size , max_box_size + 1) , [0] * ( max_box_size - min_box_size + 1)))
squares = dict ( zip ( range ( min_box_size , max_box_size + 1) , [0] * ( max_box_size - min_box_size + 1)))
for _ in range(repetitions): 
	# Select a random box size
	box_size = np.random.randint(min_box_size , max_box_size + 1)
	# Select a random position
	i = np.random.randint(grid_size - box_size)
	j = np.random.randint(grid_size - box_size)

	particles = np.sum(grid[i: i + box_size , j: j + box_size])
	counts[box_size] += particles
	squares[box_size] += 1
# Calculate mean values
for box_size in squares.keys():
	counts[box_size] /= squares[box_size]
	'''log(counts[box_size]) /= log(squares[box_size])
	print (log(counts[box_size]))'''
from matplotlib import pyplot as plt
aux = np.argwhere(grid == True)
for k in aux:
	count+=1
print (count)
x, y = aux.T
plt.scatter(x, y)
plt.pause(1e+9)
plt.clf()
plt.ion()

